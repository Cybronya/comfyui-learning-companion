"""
知识匹配器

从用户问题中识别「用户在问哪个节点/主题」，把自然语言问题映射到检索关键词。

设计要点：
    1. 主题用别名聚合。ComfyUI 里同一功能有多个节点类型
       （ControlNetApply / ControlNetApplyAdvanced / ControlNetLoaderModelOnly），
       归到一个主题下，避免只认单个类名。
    2. 中英文混排。问题里既有英文类名也有中文口语（"权重"、"控制"、"风格"）。
    3. 兜底：主题表没覆盖的词，用知识库自身的键名再做一次子串匹配。
"""

from typing import List, Dict, Any


class KnowledgeMatcher:
    """
    问题关键词提取器
    """

    # 主题 -> (触发词, 该主题覆盖的节点类型)
    TOPICS: Dict[str, Dict[str, List[str]]] = {
        "ControlNet": {
            "words": [
                "controlnet", "control net",
                "控制", "权重", "weight", "strength",
                "线稿", "姿势", "深度图", "depth", "canny", "openpose",
                "不自然", "太死", "僵硬", "过强", "控制过强", "构图僵硬",
            ],
            "nodes": [
                "ControlNetApply",
                "ControlNetApplyAdvanced",
                "ControlNetLoader",
                "ControlNetLoaderModelOnly",
            ],
        },
        "KSampler": {
            # 症状词（脸崩、过曝、糊等）多是采样参数导致，归到采样主题下召回
            "words": [
                "ksampler", "sampler", "采样", "采样器",
                "steps", "步数", "cfg", "guidance", "denoise", "seed", "种子",
                "euler", "dpmpp", "ddim",
                "脸崩", "脸部异常", "人脸", "面部", "五官",
                "过曝", "死黑", "噪点", "糊", "细节差", "脏",
            ],
            "nodes": [
                "KSampler",
                "KSamplerAdvanced",
                "KSamplerSelect",
                "SamplerCustom",
            ],
        },
        "VAE": {
            "words": [
                "vae", "decode", "encode", "latent", "潜空间", "解码", "编码",
                "色偏", "偏色", "色带", "暗斑", "解码错误",
            ],
            "nodes": [
                "VAEDecode",
                "VAEEncode",
                "VAEDecodeTiled",
                "VAEEncodeTiled",
            ],
        },
        "LoRA": {
            "words": [
                "lora", "loraloader", "风格", "角色", "微调", "style",
                "不像", "不像本人", "权重过高", "过拟合",
            ],
            "nodes": [
                "LoraLoader",
                "LoraLoaderModelOnly",
            ],
        },
        "Checkpoint": {
            "words": [
                "checkpoint", "ckpt", "sdxl", "sd1.5", "sd15", "flux",
                "模型", "底模", "大模型",
            ],
            "nodes": [
                "CheckpointLoaderSimple",
                "UNETLoader",
                "DualCLIPLoader",
            ],
        },
        "IPAdapter": {
            "words": [
                "ipadapter", "ip adapter", "参考图", "图生图", "img2img",
            ],
            "nodes": [
                "IPAdapterApply",
                "IPAdapterUnifiedLoader",
                "PrepImageForClipVision",
            ],
        },
        "Upscale": {
            "words": [
                "upscale", "放大", "高清", "超分", "hires", "高清修复",
                "latent upscale",
            ],
            "nodes": [
                "LatentUpscale",
                "ImageUpscaleWithModel",
                "UpscaleModelLoader",
            ],
        },
        "CLIPTextEncode": {
            "words": [
                "clip", "prompt", "提示词", "正向", "反向", "negative",
                "文本编码", "text encode", "conditioning",
            ],
            "nodes": [
                "CLIPTextEncode",
            ],
        },
        "Resolution": {
            "words": [
                "分辨率", "resolution", "尺寸", "size",
                "width", "height", "宽", "高", "空latent", "latent image",
            ],
            "nodes": [
                "EmptyLatentImage",
                "EmptySD3LatentImage",
            ],
        },
        "SaveImage": {
            "words": ["保存", "save", "output", "输出", "预览", "preview"],
            "nodes": ["SaveImage", "PreviewImage"],
        },
    }

    def match(self, text: str, extra_keys: List[str] = None) -> List[str]:
        """
        从文本中提取主题关键词

        Args:
            text: 用户问题
            extra_keys: 额外的候选词（通常是知识库的键名），
                        主题表没命中时用它做子串兜底匹配

        Returns:
            命中的主题列表
        """
        if not text:
            return []

        lowered = text.lower()
        result = []

        for topic, config in self.TOPICS.items():
            for word in config["words"]:
                if word.lower() in lowered:
                    result.append(topic)
                    break

        # 兜底：知识库里存在但主题表未覆盖的键名
        if extra_keys:
            for key in extra_keys:
                if key in result:
                    continue
                if key.lower() in lowered:
                    result.append(key)

        return list(dict.fromkeys(result))

    def nodes_for(self, topic: str) -> List[str]:
        """
        取某主题覆盖的节点类型

        Args:
            topic: 主题名

        Returns:
            节点类型列表
        """
        config = self.TOPICS.get(topic)
        return list(config["nodes"]) if config else []

    def topics_for_node(
        self,
        node_type: str,
        exact_only: bool = False
    ) -> List[str]:
        """
        反查：某个节点类型属于哪些主题

        分两档，因为「精确命中」和「类名片段命中」的可信度差别很大：
            ControlNetApplyAdvanced  → ControlNet  （片段命中，属同一功能族）
            WanVideoSampler         → KSampler     （片段命中，但完全是另一个节点）

        Args:
            node_type: 节点类型，如 ControlNetApplyAdvanced
            exact_only: 只返回精确命中（登记在 nodes 列表里的）主题。
                        缺口检测用它判断「我们是否真的懂这个节点」——
                        仅有片段命中说明只有同族的通用知识，不等于懂这个节点。

        Returns:
            主题列表
        """
        matched = []
        for topic, config in self.TOPICS.items():
            if node_type in config["nodes"]:
                matched.append(topic)

        if matched or exact_only:
            return matched

        # 兜底按类名片段匹配，覆盖未登记的变体
        lowered = node_type.lower()
        for topic, config in self.TOPICS.items():
            for word in config["words"]:
                if word.lower() in lowered:
                    matched.append(topic)
                    break

        return matched

    def index_keywords_for_node(self, node_type: str) -> List[str]:
        """
        取某节点类型应挂到索引上的全部关键词

        Args:
            node_type: 节点类型

        Returns:
            关键词列表
        """
        keywords = [node_type]
        keywords.extend(self.topics_for_node(node_type))

        # 附加 learning_topics 风格的话题词（steps / cfg / prompt 等）
        for topic, config in self.TOPICS.items():
            if topic in keywords:
                continue
            for word in config["words"]:
                if word.lower() in node_type.lower():
                    keywords.append(word)

        return list(dict.fromkeys(keywords))

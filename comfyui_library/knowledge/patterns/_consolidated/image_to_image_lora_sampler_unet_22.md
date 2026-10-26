---
name: image_to_image_lora_sampler_unet_22
type: Image To Image
frequency: 18
level: moderate
coverage: 0.895
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-多图角度生成器_1990322262794530817.json, 图片生成/图生图/Qwen-Image-Edit-2509 图像编辑 图像替换 多图融合 在线免费应用 免费下载部署_1982283626857545730.json, 图片生成/图生图/Qwen-Image-Edit千问转角度镜头转换_1990070283493101570.json, 图片生成/图生图/image_qwen_image_edit_2509-三图人物+动物+场景融合_1970991494343598082.json, 图片生成/图生图/image_qwen_image_edit_2509-双图人物姿态控制_1970987586586058753.json, 图片生成/图生图/image_qwen_image_edit_2509-双图人物指定换装和饰品_1970981672911020033.json, 图片生成/图生图/image_qwen_image_edit_2509-提示词改变主体_1970979185940406274.json, 图片生成/图生图/qwen Edit_2028751468630646786.json, 图片生成/图生图/qwen2509_1997815157244014594.json, 图片生成/图生图/【橘子AI】Qwen Image Edit Plus 单图+多图编辑_1971464154261471234.json, 图片生成/图生图/一句话提取衣服_1990645950131691522.json, 视频生成/图生视频/一键佩戴饰品+生成讲解视频_1989475956505104385.json, 视频生成/图生视频/一键换图片背景+生成烧菜视频_1987684744014049282.json, 视频生成/图生视频/一键生成和小时候的自己对话_1987671585945489409.json, 视频生成/图生视频/三图参考生成两个人物对话视频_1987680109538816002.json, 视频生成/图生视频/指定人物对话_1987680874936381442.json, 视频生成/图生视频/生成人物视角转换视频_1987676437924745217.json, 视频生成/文生视频/一句话生成和小时候的自己对话_1987677418305556481.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_22

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-多图角度生成器_1990322262794530817.json、图片生成/图生图/Qwen-Image-Edit-2509 图像编辑 图像替换 多图融合 在线免费应用 免费下载部署_1982283626857545730.json、图片生成/图生图/Qwen-Image-Edit千问转角度镜头转换_1990070283493101570.json、图片生成/图生图/image_qwen_image_edit_2509-三图人物+动物+场景融合_1970991494343598082.json、图片生成/图生图/image_qwen_image_edit_2509-双图人物姿态控制_1970987586586058753.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 16/18 个有
- `SaveImage` —— 15/18 个有
- `RH_Sora2_I2V` —— 8/18 个有
- `SaveVideo` —— 8/18 个有
- `PrimitiveStringMultiline` —— 5/18 个有
- `easy imageSize` —— 2/18 个有
- `ImageListToImageBatch` —— 1/18 个有
- `QwenMultiangleCameraNode` —— 1/18 个有
- `ShowText|pysssss` —— 1/18 个有
- `VHS_SelectImages` —— 1/18 个有
- `easy promptList` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 18 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 18 | 68% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，18 个样本
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足

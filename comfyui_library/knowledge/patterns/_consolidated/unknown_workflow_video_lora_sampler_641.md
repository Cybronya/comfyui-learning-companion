---
name: unknown_workflow_video_lora_sampler_641
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.929333
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, DisableNoise, EmptyHunyuanLatentVideo, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmas, UNETLoader, VAEDecode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [图片生成/文生图/[🛫书墨]wan2.2图像反推文生图_1952356133568745474.json, 图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json, 图片生成/文生图/文生图-wan2.2图像反推文生图_1954793772753182722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_641

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/[🛫书墨]wan2.2图像反推文生图_1952356133568745474.json、图片生成/文生图/wan2.2洗稿文生图_1985878501448396802.json、图片生成/文生图/文生图-wan2.2图像反推文生图_1954793772753182722.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `EmptyHunyuanLatentVideo`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

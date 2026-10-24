---
name: text_to_image_lora_sampler_clip_138
type: Text To Image
frequency: 11
level: weak
coverage: 0.884182
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ColorMatch, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2影视资产生成V1_2103524349650235394.json, 图片生成/文生图/Krea2影视资产生成工作流，文生图影视素材快速产出工具_2103978065222266882.json, 图片生成/文生图/krea2上传剧本自动提取生成角色资产 角色设定批量产出_2109364306587508738.json, 图片生成/文生图/krea2上传剧本自动提取生成角色资产_2081945873101185026.json, 图片生成/文生图/krea2上传剧本自动提取生成角色资产_2082631048692846594.json, 图片生成/文生图/krea2影视资产生成_2080971161210544130.json, 图片生成/文生图/krea2角色资产生成-有剧本即可自动化生成_2081247228685017089.json, 图片生成/文生图/krea2角色资产生成_2081907438109941762.json, 图片生成/文生图/minimax h3-krea2角色资产生成-剧本自动化生成_2094446589719957506.json, 图片生成/文生图/剧本自动提取角色资产｜krea2文生图反推提示词生成_2092597301486379010.json, 数字人/数字人/krea2影视资产生成四视图_2094753229727944705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_138

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Krea2影视资产生成V1_2103524349650235394.json、图片生成/文生图/Krea2影视资产生成工作流，文生图影视素材快速产出工具_2103978065222266882.json、图片生成/文生图/krea2上传剧本自动提取生成角色资产 角色设定批量产出_2109364306587508738.json、图片生成/文生图/krea2上传剧本自动提取生成角色资产_2081945873101185026.json、图片生成/文生图/krea2上传剧本自动提取生成角色资产_2082631048692846594.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatch`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 10/11 个有
- `ImageScaleToTotalPixels` —— 9/11 个有
- `RH_LLMAPI_Pro_Node` —— 7/11 个有
- `easy showAnything` —— 7/11 个有
- `JjkText` —— 3/11 个有
- `solarL_SaveImagesToZip` —— 3/11 个有
- `孤海注释` —— 3/11 个有
- `ImageScaleBy` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `ModelAttentionBackend` —— 2/11 个有
- `LatentUpscaleBy` —— 1/11 个有
- `MultiTextConcatenate` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 11 | 20% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 0.43 - 1 | 11 | 83% |
| 宽度 | 1024 | 80 - 1024 | 11 | 45% |
| 高度 | 1024 | 80 - 1024 | 11 | 45% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 0.43 - 1，11 个样本，取值集中（一致性 83%）
- 宽度 中位数 1024，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 45%
- 高度 中位数 1024，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 45%
- 高发问题（15/11 个样本）：Steps较低可能导致细节不足

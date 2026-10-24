---
name: image_to_image_sampler_clip_unet_114
type: Image To Image
frequency: 4
level: moderate
coverage: 0.96075
common_nodes: [CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2图生图_1994304916818771969.json, 图片生成/图生图/Flux2洗图工作流_1993561388627017729.json, 图片生成/图生图/SRPO-flux图生图_1981704184250671106.json, 图片生成/图生图/Z-image图生图_1993973986677768194.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_114

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2图生图_1994304916818771969.json、图片生成/图生图/Flux2洗图工作流_1993561388627017729.json、图片生成/图生图/SRPO-flux图生图_1981704184250671106.json、图片生成/图生图/Z-image图生图_1993973986677768194.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `FluxGuidance` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `Latent Noise Injection` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.5 | 0.3 - 0.5 | 4 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.5，观测区间 0.3 - 0.5，4 个样本，取值集中（一致性 81%）

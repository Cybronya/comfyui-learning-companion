---
name: unknown_workflow_sampler_unet_vae_108
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.789556
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json, 图片生成/图生图/AI图像创作丨Qwen-Image-2.1丨参考图生成_2113557651341799425.json, 图片生成/图生图/Head Swap_ qwen image2.1 Local Transfer换头_2113428071536742402.json, 图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json, 图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105113064805855234.json, 图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105490232509558786.json, 图片生成/图生图/一键换头-qwen image2.1最新迁移_2107910635219668994.json, 图片生成/图生图/服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273.json, 图片生成/文生图/Qwen image 2.1图片编辑(提示词增强）_2101808961656811521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_108

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json、图片生成/图生图/AI图像创作丨Qwen-Image-2.1丨参考图生成_2113557651341799425.json、图片生成/图生图/Head Swap_ qwen image2.1 Local Transfer换头_2113428071536742402.json、图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json、图片生成/图生图/Qwen_image_2.1图片编辑(提示词增强_2105113064805855234.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `ImageConcatMulti` —— 8/9 个有
- `ImageResizeKJv2` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `BatchImagesNode` —— 5/9 个有
- `TextGenerateLTX2Prompt` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `AddLabel` —— 4/9 个有
- `CR Text` —— 4/9 个有
- `ComfySwitchNode` —— 4/9 个有
- `GetNode` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `InvertMask` —— 2/9 个有
- `JoinImageWithAlpha` —— 2/9 个有
- `LoadBackgroundRemovalModel` —— 2/9 个有
- `RemoveBackground` —— 2/9 个有
- `JDCN_StringToList` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 8 - 50 | 9 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 1024 - 1440 | 9 | 88% |
| 高度 | 1024 | 1024 - 2560 | 9 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 8 - 50，9 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1440，9 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 2560，9 个样本

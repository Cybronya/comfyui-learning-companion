---
name: unknown_workflow_sampler_unet_vae_94
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.835714
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/反推提示词/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json, 图片生成/图生图/2101946565576454146.json, 图片生成/图生图/2101987550209593345.json, 图片生成/图生图/2102212076977606658.json, 图片生成/图生图/2102302487393951746.json, 图片生成/图生图/2102302931948228610.json, 图片生成/图生图/2103497645263249410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_94

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Qwen+image+2.1图片编辑(提示词增强）_2103497645263249410.json、图片生成/图生图/2101946565576454146.json、图片生成/图生图/2101987550209593345.json、图片生成/图生图/2102212076977606658.json、图片生成/图生图/2102302487393951746.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `SaveImageAdvanced` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `ImageMergeNode` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2

---
name: unknown_workflow_inpaint_upscale_sampler_4
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.81
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, CropWithPadInfo, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), ImageAndMaskPreview, InpaintCrop, InpaintStitch, KSampler, LoadImage, PrimitiveStringMultiline, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, WujiCleaner, WujiUpscaler]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移局部重绘遮罩精细化改图图像编辑_2004168242325299202.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2004148282525949953.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2097877408404828161.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2099411318628511745.json, 图片生成/图生图/局部重绘_2075453429752881154.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移局部重绘遮罩精细化改图图像编辑_2004168242325299202.json、图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2004148282525949953.json、图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2097877408404828161.json、图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2099411318628511745.json、图片生成/图生图/局部重绘_2075453429752881154.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `InpaintCrop`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`
- `WujiCleaner`
- `WujiUpscaler`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

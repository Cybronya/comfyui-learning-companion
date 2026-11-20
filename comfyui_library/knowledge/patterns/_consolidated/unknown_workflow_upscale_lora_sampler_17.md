---
name: unknown_workflow_upscale_lora_sampler_17
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.815154
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2.0版Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2027989847570391041.json, 图片生成/图生图/DG_2511编辑模型+局部重绘+放大_2011612354831716354.json, 图片生成/图生图/FireRed-Image零偏移遮罩精细化改图_2042559810339606529.json, 图片生成/图生图/Gordon局部重绘_2017061492624986114.json, 图片生成/图生图/Qwen-Eidt  局部重绘图像编辑_2013548378524753921.json, 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑自用_2013925887216984065.json, 图片生成/图生图/Qwen-Eidt-局部重绘_2011482958997229570.json, 图片生成/图生图/Qwen-局部重绘_2029471727851409410.json, 图片生成/图生图/单图编辑+遮罩区域+局部重绘-Qwen Edit2511_2004473094637056001.json, 图片生成/文生图/DG(已整理)_2511+单图和双图+遮罩+放大参考-贴回_1990625154751488001.json, 平台全量/Qwen edit 真实换装 无遮罩控制 全自动换装+SeedVR2高清放大 加速版_2026531977721028610.json, 平台全量/Qwen-Eidt-2511局部重绘图像编辑_2018658355283238914.json, 平台全量/局部重绘 Qwen-Eidt-2511+SeedVR2.5 零偏移遮罩精细化改图 局部重绘 图像编辑_2006187411239342081.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/2.0版Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2027989847570391041.json、图片生成/图生图/DG_2511编辑模型+局部重绘+放大_2011612354831716354.json、图片生成/图生图/FireRed-Image零偏移遮罩精细化改图_2042559810339606529.json、图片生成/图生图/Gordon局部重绘_2017061492624986114.json、图片生成/图生图/Qwen-Eidt  局部重绘图像编辑_2013548378524753921.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 12/13 个有
- `FluxKontextMultiReferenceLatentMethod` —— 11/13 个有
- `ImageAndMaskPreview` —— 11/13 个有
- `InpaintCrop` —— 11/13 个有
- `InpaintStitch` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 9/13 个有
- `GetNode` —— 3/13 个有
- `Seed (rgthree)` —— 3/13 个有
- `SetNode` —— 3/13 个有
- `ImageScaleBy` —— 2/13 个有
- `InpaintCropImproved` —— 2/13 个有
- `InpaintStitchImproved` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `QwenEditAdaptiveLongestEdge` —— 2/13 个有
- `ControlNetInpaintingAliMamaApply` —— 1/13 个有
- `ControlNetLoader` —— 1/13 个有
- `GrowMaskWithBlur` —— 1/13 个有
- `ImageConcatMulti` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足

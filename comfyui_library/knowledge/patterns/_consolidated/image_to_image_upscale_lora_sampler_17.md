---
name: image_to_image_upscale_lora_sampler_17
type: Image To Image
frequency: 9
level: strong
coverage: 0.814
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, DF_Integer, DrawMaskOnImage, Get Image Size, ImageCASharpening+, ImageResize+, ImageUpscaleWithModel, ImpactMinMax, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImageMask, LoraLoaderModelOnly, MaskBlur+, MaskFillHoles, ModelSamplingAuraFlow, PreviewImage, RunningHub Deepcleaner, SaveImage, SeedVR2, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万能图片去水印加高清_2063449783058132993.json, 图片生成/图生图/万能图片去水印加高清_2064504134509879297.json, 图片生成/图生图/万能图片去水印加高清_2065255472411799554.json, 图片生成/图生图/万能图片去水印加高清支持上传遮罩图_2085991720520609794.json, 图片生成/图生图/万能图片去水印加高清支持上传遮罩图_2086270345568411650.json, 图片生成/图生图/万能图片去水印加高清（支持上传遮罩图)-邻家AI大女孩_2045453860990357505.json, 图片生成/图生图/万能图片去水印加高清（支持上传遮罩图）_2039934030212239362.json, 图片生成/图生图/万能图片去水印加高清（支持上传遮罩图）_2046204045819387906.json, 图片生成/文生图/万能图片去水印加高清（支持上传遮罩图）_2046065715639226369.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/万能图片去水印加高清_2063449783058132993.json、图片生成/图生图/万能图片去水印加高清_2064504134509879297.json、图片生成/图生图/万能图片去水印加高清_2065255472411799554.json、图片生成/图生图/万能图片去水印加高清支持上传遮罩图_2085991720520609794.json、图片生成/图生图/万能图片去水印加高清支持上传遮罩图_2086270345568411650.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DF_Integer`
- `DrawMaskOnImage`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `ImpactMinMax`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImageMask`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `MaskFillHoles`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SeedVR2`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

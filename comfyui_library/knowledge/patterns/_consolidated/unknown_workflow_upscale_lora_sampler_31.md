---
name: unknown_workflow_upscale_lora_sampler_31
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9095
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DepthAnythingPreprocessor, DualCLIPLoader, FluxGuidance, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LayerFilter: FilmV2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/FULX超真实的自拍遮脸美女_1917444203784376322.json, "图片生成/图生图/FULX超真实的自拍遮脸美女制造机2分钟一个美女,可调胸部，是否遮挡。IPHONE手机出图质量超级高_1910876504568594434.json", 图片生成/图生图/【RICK团队】Supir+TTP分块放大 8K_1905171404461887489.json, "图片生成/图生图/美女制造机2分钟一个美女,可调胸部，是否遮挡。_1922527404701663234.json", "图片生成/图生图/美女制造机2分钟一个美女,可调胸部，是否遮挡。_1947332611867824129.json", 图片生成/文生图/【魅影勾魂】【文生性感美女图】_1908502827172569090.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FULX超真实的自拍遮脸美女_1917444203784376322.json、图片生成/图生图/FULX超真实的自拍遮脸美女制造机2分钟一个美女,可调胸部，是否遮挡。IPHONE手机出图质量超级高_1910876504568594434.json、图片生成/图生图/【RICK团队】Supir+TTP分块放大 8K_1905171404461887489.json、图片生成/图生图/美女制造机2分钟一个美女,可调胸部，是否遮挡。_1922527404701663234.json、图片生成/图生图/美女制造机2分钟一个美女,可调胸部，是否遮挡。_1947332611867824129.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DepthAnythingPreprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LayerFilter: FilmV2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 5/6 个有
- `CLIPTextEncodeFlux` —— 5/6 个有
- `CR Latent Batch Size` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `LayerUtility: TextJoin` —— 5/6 个有
- `RH_Captioner` —— 5/6 个有
- `StringConstantMultiline` —— 5/6 个有
- `VAEDecode` —— 5/6 个有
- `RH_Translator` —— 4/6 个有
- `TeaCache` —— 4/6 个有
- `EmptyLatentImage` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `CFGGuider` —— 2/6 个有
- `ApplyFBCacheOnModel` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `SUPIR_Upscale` —— 1/6 个有
- `easy imageListToImageBatch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_upscale_lora_sampler_101
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.93
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, ConditioningCombine, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageResize+, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoader, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/视频首帧【图片】风格化转绘  楚门的AI世界_1925126473337008130.json, 图片生成/图生图/🦖TTP 保细节放大_1894331074686922754.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_101

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/视频首帧【图片】风格化转绘  楚门的AI世界_1925126473337008130.json、图片生成/图生图/🦖TTP 保细节放大_1894331074686922754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `ConditioningCombine`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RH_Captioner`
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
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ApplyIPAdapterFlux` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `IPAdapterFluxLoader` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | - | 1 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_controlnet_upscale_face_detailer_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9605
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Latent Batch Size, CXH_DownloadAndLoadFlorence2Model, ControlNetApplySD3, ControlNetLoader, DepthAnythingPreprocessor, DualCLIPLoader, FaceDetailer, Fast Groups Bypasser (rgthree), Florence2Run, FluxGuidance, Image Comparer (rgthree), ImageConcanate, ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/最新六连出图人物一致性_1917848975217459202.json, 图片生成/图生图/最新六连出图人物一致性_1927579088175652865.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/最新六连出图人物一致性_1917848975217459202.json、图片生成/图生图/最新六连出图人物一致性_1927579088175652865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Latent Batch Size`
- `CXH_DownloadAndLoadFlorence2Model`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `DualCLIPLoader`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

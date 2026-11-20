---
name: unknown_workflow_upscale_sampler_clip_70
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9295
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DetailDaemonSamplerNode, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptySD3LatentImage, FL_ImageSlicer, Float, Florence2Run, FluxGuidance, FluxKontextImageScale, GetImageSize+, Image Comparer (rgthree), ImageConcanateOfUtils, ImageScaleBy, Images to RGB, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingFlux, PreviewImage, RHHiddenNodes, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/🥎老照片一键修复【带放大高清修复】🤹_1962324256732418050.json, 平台全量/🤹一键老照片修复 _ 智能高清复原_1996024400996712449.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/🥎老照片一键修复【带放大高清修复】🤹_1962324256732418050.json、平台全量/🤹一键老照片修复 _ 智能高清复原_1996024400996712449.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DetailDaemonSamplerNode`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FL_ImageSlicer`
- `Float`
- `Florence2Run`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageConcanateOfUtils`
- `ImageScaleBy`
- `Images to RGB`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RHHiddenNodes`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

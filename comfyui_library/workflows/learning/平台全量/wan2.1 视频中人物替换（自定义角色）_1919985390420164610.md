---
key: 平台全量/wan2.1 视频中人物替换（自定义角色）_1919985390420164610.json
name: wan2.1 视频中人物替换（自定义角色）_1919985390420164610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 视频中人物替换（自定义角色）_1919985390420164610.json
hash: e6c7c93c80925679
coverage: 0.648352
learned_at: 2026-11-14 01:19:03
nodes: [SegsToCombinedMask, ImpactImageBatchToImageList, MediaPipeFaceMeshToSEGS, AnyLineArtPreprocessor_aux, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, MaskToImage, ImageBlend, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), GetNode, GetNode, GetNode, CFGZeroStar, ModelSamplingSD3, GetNode, MarkdownNote, MarkdownNote, SkipLayerGuidanceDiT, CLIPVisionEncode, CLIPTextEncode, UNetTemporalAttentionMultiply, DWPreprocessor, KSampler, GrowMaskWithBlur, VAEDecode, Color Correct (mtb), MarkdownNote, GetNode, ImageListToImageBatch, ImageBlend, MediaPipe-FaceMeshPreprocessor, ImageToMask, MaskToImage, ImageConcatMulti, VHS_VideoCombine, GetNode, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, DepthAnything_V2, Reroute, Reroute, Reroute, Reroute, VHS_LoadVideo, MarkdownNote, UNETLoader, MarkdownNote, CLIPLoader, VAELoader, CLIPVisionLoader, DownloadAndLoadDepthAnythingV2Model, CLIPTextEncode, ImageResizeKJ, ImageResizeKJ, SetNode, WanFunControlToVideo, SetNode, LoadImage, GetImageSizeAndCount, VHS_VideoCombine, GetNode, SetNode, VRAM_Debug, GetImageSizeAndCount, GetNode, ImageResizeKJ, ImageBlend, ImageResizeKJ, ImageResizeKJ, ImageBlend, ImageBlend, ImageResizeKJ, ImageBlend, ImageResizeKJ, EmptyImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 887940314022891, "steps": 25}
---

# 平台全量/wan2.1 视频中人物替换（自定义角色）_1919985390420164610.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 视频中人物替换（自定义角色）_1919985390420164610.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（91 个）：
- `SegsToCombinedMask`
- `ImpactImageBatchToImageList`
- `MediaPipeFaceMeshToSEGS`
- `AnyLineArtPreprocessor_aux`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `MaskToImage`
- `ImageBlend`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGZeroStar`
- `ModelSamplingSD3`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SkipLayerGuidanceDiT`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `UNetTemporalAttentionMultiply`
- `DWPreprocessor`
- `KSampler` ★核心
- `GrowMaskWithBlur`
- `VAEDecode` ★核心
- `Color Correct (mtb)`
- `MarkdownNote`
- `GetNode`
- `ImageListToImageBatch`
- `ImageBlend`
- `MediaPipe-FaceMeshPreprocessor`
- `ImageToMask`
- `MaskToImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `DepthAnything_V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_LoadVideo`
- `MarkdownNote`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `DownloadAndLoadDepthAnythingV2Model`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `ImageResizeKJ`
- `SetNode`
- `WanFunControlToVideo`
- `SetNode`
- `LoadImage`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `VRAM_Debug`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `ImageBlend`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageBlend`
- `ImageBlend`
- `ImageResizeKJ`
- `ImageBlend`
- `ImageResizeKJ`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `887940314022891`
- `steps` = `25`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（59/91）

**有卡**：`SegsToCombinedMask`、`ImpactImageBatchToImageList`、`MediaPipeFaceMeshToSEGS`、`AnyLineArtPreprocessor_aux`、`VHS_VideoCombine`、`MaskToImage`、`ImageBlend`、`Label (rgthree)`、`CFGZeroStar`、`ModelSamplingSD3`、`SkipLayerGuidanceDiT`、`CLIPVisionEncode`、`CLIPTextEncode`、`UNetTemporalAttentionMultiply`、`DWPreprocessor`、`KSampler`、`GrowMaskWithBlur`、`VAEDecode`、`Color Correct (mtb)`、`ImageListToImageBatch`、`MediaPipe-FaceMeshPreprocessor`、`ImageToMask`、`ImageConcatMulti`、`DepthAnything_V2`、`VHS_LoadVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`DownloadAndLoadDepthAnythingV2Model`、`ImageResizeKJ`、`WanFunControlToVideo`、`LoadImage`、`GetImageSizeAndCount`、`VRAM_Debug`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、DepthAnything_V2

---
key: 视频生成/图生视频/【首帧+控制网】MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1919653290769059842.json
name: 【首帧+控制网】MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1919653290769059842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1919653290769059842.json
hash: 67d326552f3a9dea
coverage: 0.578947
learned_at: 2026-10-15 22:29:41
nodes: [Reroute, VHS_VideoCombine, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CLIPTextEncode, MarkdownNote, EmptyImage, ImageBlend, ImageResizeKJ, GetNode, DWPreprocessor, GetImageSizeAndCount, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, Reroute, DepthAnythingV2Preprocessor, ImageResizeKJ, ImageResizeKJ, easy clearCacheAll, easy clearCacheAll, Reroute, MaskToImage, ImageBlend, SetNode, Fast Groups Bypasser (rgthree), ImageBlend, ImageResizeKJ, VRAM_Debug, ImageBlend, VHS_VideoCombine, ImageListToImageBatch, SegsToCombinedMask, MediaPipe-FaceMeshPreprocessor, ImpactImageBatchToImageList, MediaPipeFaceMeshToSEGS, Note, CR Text Input Switch, Note, Note, Note, ModelSamplingSD3, UNetTemporalAttentionMultiply, GetNode, CFGZeroStar, GetNode, SetNode, DownloadAndLoadDepthAnythingV2Model, SetNode, CLIPVisionLoader, SetNode, VAELoader, SetNode, CLIPLoader, UNETLoader, SetNode, LoraLoaderModelOnly, Note, GetNode, GetNode, easy clearCacheAll, Note, VHS_VideoCombine, LayerMask: PersonMaskUltra V2, MaskPreview+, PreviewImage, CR Upscale Image, PreviewImage, PreviewImage, VAEDecodeTiled, SkipLayerGuidanceDiT, LoadImage, RMBG, LoadImage, KSampler, DisplayText_Zho, LayerUtility: CropByMask, JWImageResizeByLongerSide, Primitive integer [Crystools], Primitive integer [Crystools], ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ReActorFaceSwap, SetNode, PreviewImage, ImageResizeKJ, VHS_LoadVideo, GetNode, VHS_VideoCombine, GetNode, RH_Captioner, SetNode, SetNode, VRAM_Debug, CLIPVisionEncode, SetNode, GetNode, ImageResizeKJ, GetNode, GetNode, WanFunControlToVideo, easy clearCacheAll, GetNode, CR Text, VHS_VideoCombine]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 404805651086029, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/【首帧+控制网】MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1919653290769059842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1919653290769059842.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `Reroute`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `EmptyImage`
- `ImageBlend`
- `ImageResizeKJ`
- `GetNode`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Reroute`
- `DepthAnythingV2Preprocessor`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `Reroute`
- `MaskToImage`
- `ImageBlend`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `ImageBlend`
- `ImageResizeKJ`
- `VRAM_Debug`
- `ImageBlend`
- `VHS_VideoCombine`
- `ImageListToImageBatch`
- `SegsToCombinedMask`
- `MediaPipe-FaceMeshPreprocessor`
- `ImpactImageBatchToImageList`
- `MediaPipeFaceMeshToSEGS`
- `Note`
- `CR Text Input Switch`
- `Note`
- `Note`
- `Note`
- `ModelSamplingSD3`
- `UNetTemporalAttentionMultiply`
- `GetNode`
- `CFGZeroStar`
- `GetNode`
- `SetNode`
- `DownloadAndLoadDepthAnythingV2Model`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `Note`
- `VHS_VideoCombine`
- `LayerMask: PersonMaskUltra V2`
- `MaskPreview+`
- `PreviewImage`
- `CR Upscale Image`
- `PreviewImage`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `SkipLayerGuidanceDiT`
- `LoadImage`
- `RMBG`
- `LoadImage`
- `KSampler` ★核心
- `DisplayText_Zho`
- `LayerUtility: CropByMask`
- `JWImageResizeByLongerSide`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ReActorFaceSwap`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJ`
- `VHS_LoadVideo`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `RH_Captioner`
- `SetNode`
- `SetNode`
- `VRAM_Debug`
- `CLIPVisionEncode`
- `SetNode`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `WanFunControlToVideo`
- `easy clearCacheAll`
- `GetNode`
- `CR Text`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `404805651086029`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（66/114）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`EmptyImage`、`ImageBlend`、`ImageResizeKJ`、`DWPreprocessor`、`GetImageSizeAndCount`、`DepthAnythingV2Preprocessor`、`easy clearCacheAll`、`MaskToImage`、`VRAM_Debug`、`ImageListToImageBatch`、`SegsToCombinedMask`、`MediaPipe-FaceMeshPreprocessor`、`ImpactImageBatchToImageList`、`MediaPipeFaceMeshToSEGS`、`CR Text Input Switch`、`ModelSamplingSD3`、`UNetTemporalAttentionMultiply`、`CFGZeroStar`、`DownloadAndLoadDepthAnythingV2Model`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerMask: PersonMaskUltra V2`、`MaskPreview+`、`CR Upscale Image`、`VAEDecodeTiled`、`SkipLayerGuidanceDiT`、`LoadImage`、`RMBG`、`KSampler`、`DisplayText_Zho`、`LayerUtility: CropByMask`、`JWImageResizeByLongerSide`、`Primitive integer [Crystools]`、`ImageConcatMulti`、`ReActorFaceSwap`、`VHS_LoadVideo`、`RH_Captioner`、`CLIPVisionEncode`、`WanFunControlToVideo`、`CR Text`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、DepthAnythingV2Preprocessor

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

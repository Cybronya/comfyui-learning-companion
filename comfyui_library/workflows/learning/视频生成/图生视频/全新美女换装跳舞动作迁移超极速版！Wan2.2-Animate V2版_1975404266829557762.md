---
key: 视频生成/图生视频/全新美女换装跳舞动作迁移超极速版！Wan2.2-Animate V2版_1975404266829557762.json
name: 全新美女换装跳舞动作迁移超极速版！Wan2.2-Animate V2版_1975404266829557762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/全新美女换装跳舞动作迁移超极速版！Wan2.2-Animate V2版_1975404266829557762.json
hash: ccc051c9cc4754e2
coverage: 0.855769
learned_at: 2026-10-15 22:32:08
nodes: [WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, CLIPVisionLoader, WanVideoVAELoader, ImageCropByMaskAndResize, CLIPVisionLoader, Note, SimpleMath+, WanVideoBlockSwap, Note, DWPreprocessor, JWInteger, JWInteger, PrimitiveStringMultiline, VHS_LoadVideo, WanVideoClipVisionEncode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoSampler, MarkdownNote, LoadImage, PixelPerfectResolution, FaceMaskFromPoseKeypoints, WanVideoModelLoader, RHHiddenNodes, WanVideoTextEncodeCached, SetNode, VHS_VideoInfo, GetNode, VHS_VideoCombine, LayerMask: ObjectDetectorYOLO8, LayerMask: SAM2Ultra, LayerUtility: ColorImage V2, LayerMask: ObjectDetectorYOLO8, LayerMask: ObjectDetectorYOLO8, LayerMask: SAM2Ultra, LayerMask: SAM2Ultra, MaskPreview+, MaskPreview+, LayerMask: MaskGrow, ImageResizeKJ, SubtractMask, CLIPVisionLoader, LayerMask: LoadBiRefNetModelV2, LayerMask: BiRefNetUltraV2, PreviewImage, ImageResizeKJ, ImageResizeKJ, PreviewImage, AddMask, MaskPreview+, AddMask, LayerMask: PersonMaskUltra V2, PreviewImage, LayerUtility: CropByMask, LayerStyle: ColorOverlay V2, StyleModelLoader, LayerMask: MaskGrow, MaskToImage, SubtractMask, Mask Threshold Region, ReduxAdvanced, VAEDecode, PreviewImage, TeaCache, FluxGuidance, KSampler, CLIPTextEncode, VAELoader, CR Text, Switch any [Crystools], PreviewImage, GetImageSize+, ImageToMask, PreviewImage, ImageConcanate, LayerUtility: ColorImage V2, InpaintModelConditioning, ImageCrop+, ImageConcanate, UpscaleModelLoader, ImageConcanate, PreviewImage, PreviewImage, LoadImage, LoadImage, MaskToImage, ImageResizeKJ, Switch any [Crystools], ImageConcanate, easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, PreviewImage, DualCLIPLoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, RHHiddenNodes, RHHiddenNodes, UNETLoader, ImpactInt]
patterns: []
missing: []
parameters: {"cfg": 1.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 229085726986818, "steps": 25}
---

# 视频生成/图生视频/全新美女换装跳舞动作迁移超极速版！Wan2.2-Animate V2版_1975404266829557762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975404266829557762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `ImageCropByMaskAndResize`
- `CLIPVisionLoader`
- `Note`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `Note`
- `DWPreprocessor`
- `JWInteger`
- `JWInteger`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `WanVideoClipVisionEncode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `LoadImage`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `WanVideoModelLoader`
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `SetNode`
- `VHS_VideoInfo`
- `GetNode`
- `VHS_VideoCombine`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: SAM2Ultra`
- `LayerUtility: ColorImage V2`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: SAM2Ultra`
- `LayerMask: SAM2Ultra`
- `MaskPreview+`
- `MaskPreview+`
- `LayerMask: MaskGrow`
- `ImageResizeKJ`
- `SubtractMask`
- `CLIPVisionLoader`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: BiRefNetUltraV2`
- `PreviewImage`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `PreviewImage`
- `AddMask`
- `MaskPreview+`
- `AddMask`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `LayerUtility: CropByMask`
- `LayerStyle: ColorOverlay V2`
- `StyleModelLoader`
- `LayerMask: MaskGrow`
- `MaskToImage`
- `SubtractMask`
- `Mask Threshold Region`
- `ReduxAdvanced`
- `VAEDecode` ★核心
- `PreviewImage`
- `TeaCache`
- `FluxGuidance`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CR Text`
- `Switch any [Crystools]`
- `PreviewImage`
- `GetImageSize+`
- `ImageToMask`
- `PreviewImage`
- `ImageConcanate`
- `LayerUtility: ColorImage V2`
- `InpaintModelConditioning`
- `ImageCrop+`
- `ImageConcanate`
- `UpscaleModelLoader`
- `ImageConcanate`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `MaskToImage`
- `ImageResizeKJ`
- `Switch any [Crystools]`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `PreviewImage`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `RHHiddenNodes`
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `ImpactInt`

## 关键参数

- `seed` = `229085726986818`
- `steps` = `25`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（89/104）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageCropByMaskAndResize`、`SimpleMath+`、`WanVideoBlockSwap`、`DWPreprocessor`、`JWInteger`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`LoadImage`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`WanVideoModelLoader`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`VHS_VideoInfo`、`VHS_VideoCombine`、`LayerMask: ObjectDetectorYOLO8`、`LayerMask: SAM2Ultra`、`LayerUtility: ColorImage V2`、`MaskPreview+`、`LayerMask: MaskGrow`、`ImageResizeKJ`、`SubtractMask`、`LayerMask: LoadBiRefNetModelV2`、`LayerMask: BiRefNetUltraV2`、`AddMask`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropByMask`、`LayerStyle: ColorOverlay V2`、`StyleModelLoader`、`MaskToImage`、`Mask Threshold Region`、`ReduxAdvanced`、`VAEDecode`、`TeaCache`、`FluxGuidance`、`KSampler`、`CLIPTextEncode`、`VAELoader`、`CR Text`、`Switch any [Crystools]`、`GetImageSize+`、`ImageToMask`、`ImageConcanate`、`InpaintModelConditioning`、`ImageCrop+`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance

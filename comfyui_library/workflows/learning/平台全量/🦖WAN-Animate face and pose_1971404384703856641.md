---
key: 平台全量/🦖WAN-Animate face and pose_1971404384703856641.json
name: 🦖WAN-Animate face and pose_1971404384703856641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🦖WAN-Animate face and pose_1971404384703856641.json
hash: 9088793d3fea7ea7
coverage: 0.975
learned_at: 2026-11-14 02:55:45
nodes: [VHS_VideoInfo, PixelPerfectResolution, VideoInputPreprocessor, FaceProcessorLoader, ApplyFaceProcessor, LayerUtility: ImageMaskScaleAsV2, MasksToMaskList, OpenposePreprocessor, DWPreprocessor, FaceMaskFromPoseKeypoints, MyOpenPoseNode, RH_Captioner, JoinStrings, GetImageSizeAndCount, ImpactImageBatchToImageList, LayerUtility: CropByMask V2, ImageListToImageBatch, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, ImageConcatMulti, ImageConcatMulti, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoEncode, WanVideoUni3C_embeds, CLIPVisionLoader, WanVideoUni3C_ControlnetLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, WanVideoAnimateEmbeds, LoadImage, PrimitiveStringMultiline, Int, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, SimpleMath+, VHS_LoadVideo, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/🦖WAN-Animate face and pose_1971404384703856641.json

> 来源文件 `comfyui_library/workflows/平台全量/🦖WAN-Animate face and pose_1971404384703856641.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `VHS_VideoInfo`
- `PixelPerfectResolution`
- `VideoInputPreprocessor`
- `FaceProcessorLoader`
- `ApplyFaceProcessor`
- `LayerUtility: ImageMaskScaleAsV2`
- `MasksToMaskList`
- `OpenposePreprocessor`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `MyOpenPoseNode`
- `RH_Captioner`
- `JoinStrings`
- `GetImageSizeAndCount`
- `ImpactImageBatchToImageList`
- `LayerUtility: CropByMask V2`
- `ImageListToImageBatch`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `CLIPVisionLoader`
- `WanVideoUni3C_ControlnetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `WanVideoAnimateEmbeds`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Int`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SimpleMath+`
- `VHS_LoadVideo`
- `WanVideoModelLoader`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`VHS_VideoInfo`、`PixelPerfectResolution`、`VideoInputPreprocessor`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`LayerUtility: ImageMaskScaleAsV2`、`MasksToMaskList`、`OpenposePreprocessor`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`MyOpenPoseNode`、`RH_Captioner`、`JoinStrings`、`GetImageSizeAndCount`、`ImpactImageBatchToImageList`、`LayerUtility: CropByMask V2`、`ImageListToImageBatch`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`CLIPVisionLoader`、`WanVideoUni3C_ControlnetLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`LoadImage`、`Int`、`WanVideoSampler`、`VHS_VideoCombine`、`SimpleMath+`、`VHS_LoadVideo`、`WanVideoModelLoader`

**用到的条目**：LoadImage、MyOpenPoseNode、OpenposePreprocessor、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode

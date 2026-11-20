---
key: 平台全量/视频单人姿势匹配_WanAnimate2.2_1990625748220350465.json
name: 视频单人姿势匹配_WanAnimate2.2_1990625748220350465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频单人姿势匹配_WanAnimate2.2_1990625748220350465.json
hash: f4edba78e3d30136
coverage: 0.434211
learned_at: 2026-11-14 02:35:51
nodes: [MarkdownNote, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, CLIPVisionLoader, WanVideoSetLoRAs, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, Note, Note, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoAnimateEmbeds, GetNode, WanVideoTextEncodeCached, VHS_VideoInfo, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, WanVideoClipVisionEncode, ImageResizeKJv2, Note, WanVideoLoraSelectMulti, WanVideoSampler, FaceMaskFromPoseKeypoints, GetNode, GetNode, PixelPerfectResolution, VHS_VideoCombine, OnnxDetectionModelLoader, GetNode, Reroute, ImageCropByMaskAndResize, CR Prompt Text, DWPreprocessor, GetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, SetNode, Fast Groups Bypasser (rgthree), SetNode, PoseAndFaceDetection, DrawViTPose, LoadImage, JWInteger, JWInteger, WanVideoDecode, GetImageRangeFromBatch, GetNode, SetNode, WanVideoBlockSwap, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/视频单人姿势匹配_WanAnimate2.2_1990625748220350465.json

> 来源文件 `comfyui_library/workflows/平台全量/视频单人姿势匹配_WanAnimate2.2_1990625748220350465.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（76 个）：
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoTextEncodeCached`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GetNode`
- `Reroute`
- `ImageCropByMaskAndResize`
- `CR Prompt Text`
- `DWPreprocessor`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `GetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`

## 知识

覆盖率 **43%**（33/76）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`VHS_VideoInfo`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`OnnxDetectionModelLoader`、`ImageCropByMaskAndResize`、`CR Prompt Text`、`DWPreprocessor`、`ImageConcatMulti`、`PoseAndFaceDetection`、`DrawViTPose`、`LoadImage`、`JWInteger`、`WanVideoDecode`、`GetImageRangeFromBatch`、`WanVideoBlockSwap`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs

---
key: 视频生成/图生视频/【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+kj循环+Sec遮罩_1985641855952068610.json
name: 【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+kj循环+Sec遮罩_1985641855952068610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+kj循环+Sec遮罩_1985641855952068610.json
hash: b25f85872c17a843
coverage: 0.4
learned_at: 2026-10-15 22:32:52
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, OnnxDetectionModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoTorchCompileSettings, PoseAndFaceDetection, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, Reroute, Reroute, Reroute, Reroute, Reroute, easy int, Reroute, Reroute, Reroute, Reroute, WanVideoDecode, Reroute, Reroute, Reroute, Reroute, Reroute, easy showAnything, WanVideoLoraSelectMulti, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, Reroute, Reroute, Reroute, Reroute, Reroute, VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, WanVideoDecode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, PreviewImage, easy showAnything, INTConstant, INTConstant, SeCModelLoader, SeCVideoSegmentation, WanVideoModelLoader, Reroute, PoseAndFaceDetection, ImageFromBatch, SeCModelLoader, WanVideoModelLoader, INTConstant, INTConstant, GrowMaskWithBlur, DrawMaskOnImage, Reroute, Reroute, DrawMaskOnImage, Reroute, PrimitiveInt, WanVideoVAELoader, WanVideoVAELoader, ImageFromBatch, PrimitiveInt, ImageResizeKJv2, ImageResizeKJv2, easy int, Reroute, VHS_VideoCombine, PlaySound|pysssss, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoBlockSwap, Reroute, VHS_VideoCombine, DrawMaskOnImage, WanVideoBlockSwap, WanVideoSampler, PlaySound|pysssss, VHS_VideoCombine, DrawMaskOnImage, WanVideoLoraSelectMulti, PreviewImage, Reroute, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, GrowMaskWithBlur, LoadImage, Reroute, WanVideoTextEncodeCached, Reroute, WanVideoTextEncodeCached, Reroute, InvertMask, SeCVideoSegmentation, InvertMask, VHS_LoadVideo, OnnxDetectionModelLoader, YOLOModelLoader, GroundingDinoModelLoader_SDPose, GetImageSizeAndCount, Reroute, Reroute, SDPoseOODLoader, YOLOModelLoader, GroundingDinoModelLoader_SDPose, VHS_VideoCombine, SDPoseOODLoader, GetImageSizeAndCount, Reroute, PointsEditor, PreviewImage, Note, Reroute, Note, VHS_VideoCombine, VHS_LoadVideo, PointsEditor, PreviewImage, BlockifyMask, Reroute, ImageCompositeMasked, VHS_VideoCombine, easy imageRemBg, Reroute, SDPoseOODProcessor, Reroute, VHS_VideoCombine, ImageCompositeMasked, VHS_VideoCombine, easy imageRemBg, SDPoseOODProcessor, Reroute, Reroute, Reroute, LayerUtility: TextBox, LoadImage, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), LayerUtility: TextBox, SaveText]
patterns: []
missing: []
---

# 视频生成/图生视频/【前瞻预览】Wan 2.2 animate究极形态 暴力骨骼动捕SDPose+kj循环+Sec遮罩_1985641855952068610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985641855952068610.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（225 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `OnnxDetectionModelLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `PoseAndFaceDetection`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy int`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoDecode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `WanVideoLoraSelectMulti`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoDecode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `easy showAnything`
- `INTConstant`
- `INTConstant`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `WanVideoModelLoader`
- `Reroute`
- `PoseAndFaceDetection`
- `ImageFromBatch`
- `SeCModelLoader`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `GrowMaskWithBlur`
- `DrawMaskOnImage`
- `Reroute`
- `Reroute`
- `DrawMaskOnImage`
- `Reroute`
- `PrimitiveInt`
- `WanVideoVAELoader`
- `WanVideoVAELoader`
- `ImageFromBatch`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy int`
- `Reroute`
- `VHS_VideoCombine`
- `PlaySound|pysssss`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Reroute`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `WanVideoLoraSelectMulti`
- `PreviewImage`
- `Reroute`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `GrowMaskWithBlur`
- `LoadImage`
- `Reroute`
- `WanVideoTextEncodeCached`
- `Reroute`
- `WanVideoTextEncodeCached`
- `Reroute`
- `InvertMask`
- `SeCVideoSegmentation`
- `InvertMask`
- `VHS_LoadVideo`
- `OnnxDetectionModelLoader`
- `YOLOModelLoader`
- `GroundingDinoModelLoader_SDPose`
- `GetImageSizeAndCount`
- `Reroute`
- `Reroute`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `GroundingDinoModelLoader_SDPose`
- `VHS_VideoCombine`
- `SDPoseOODLoader`
- `GetImageSizeAndCount`
- `Reroute`
- `PointsEditor`
- `PreviewImage`
- `Note`
- `Reroute`
- `Note`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `PointsEditor`
- `PreviewImage`
- `BlockifyMask`
- `Reroute`
- `ImageCompositeMasked`
- `VHS_VideoCombine`
- `easy imageRemBg`
- `Reroute`
- `SDPoseOODProcessor`
- `Reroute`
- `VHS_VideoCombine`
- `ImageCompositeMasked`
- `VHS_VideoCombine`
- `easy imageRemBg`
- `SDPoseOODProcessor`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: TextBox`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: TextBox`
- `SaveText`

## 知识

覆盖率 **40%**（90/225）

**有卡**：`OnnxDetectionModelLoader`、`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`INTConstant`、`SeCModelLoader`、`SeCVideoSegmentation`、`WanVideoModelLoader`、`ImageFromBatch`、`GrowMaskWithBlur`、`DrawMaskOnImage`、`WanVideoVAELoader`、`ImageResizeKJv2`、`PlaySound|pysssss`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoTextEncodeCached`、`InvertMask`、`VHS_LoadVideo`、`YOLOModelLoader`、`GroundingDinoModelLoader_SDPose`、`GetImageSizeAndCount`、`SDPoseOODLoader`、`PointsEditor`、`BlockifyMask`、`ImageCompositeMasked`、`easy imageRemBg`、`SDPoseOODProcessor`、`LayerUtility: TextBox`、`SaveImage`、`SaveText`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

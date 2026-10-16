---
key: 视频生成/图生视频/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_2018160297319604226.json
name: Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_2018160297319604226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2018160297319604226.json
hash: a329e1d776411013
coverage: 0.35567
learned_at: 2026-10-15 22:34:53
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GetImageSizeAndCount, OnnxDetectionModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageFromBatch, WanVideoModelLoader, WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GrowMaskWithBlur, Reroute, Reroute, Reroute, Reroute, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoVAELoader, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, Reroute, Reroute, Reroute, WanVideoBlockSwap, Reroute, Reroute, easy int, WanVideoAnimateEmbeds, SeCVideoSegmentation, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Reroute, Reroute, DrawMaskOnImage, BlockifyMask, Reroute, SeCModelLoader, WanVideoTextEncodeCached, Reroute, WanVideoDecode, Reroute, VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, PreviewImage, easy showAnything, PrimitiveInt, INTConstant, INTConstant, VHS_LoadVideo, PreviewImage, PointsEditor, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GetImageSizeAndCount, OnnxDetectionModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageFromBatch, WanVideoModelLoader, WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GrowMaskWithBlur, Reroute, Reroute, Reroute, Reroute, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoVAELoader, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, Reroute, Reroute, Reroute, WanVideoBlockSwap, Reroute, Reroute, easy int, SeCVideoSegmentation, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Reroute, Reroute, DrawMaskOnImage, BlockifyMask, Reroute, SeCModelLoader, WanVideoTextEncodeCached, Reroute, WanVideoDecode, Reroute, VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, PreviewImage, easy showAnything, PrimitiveInt, INTConstant, INTConstant, VHS_LoadVideo, PointsEditor, PreviewImage, WanVideoAnimateEmbeds, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_2018160297319604226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018160297319604226.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（194 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageFromBatch`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `PoseAndFaceDetection`
- `DrawViTPose`
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
- `GrowMaskWithBlur`
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
- `WanVideoVAELoader`
- `Reroute`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoBlockSwap`
- `Reroute`
- `Reroute`
- `easy int`
- `WanVideoAnimateEmbeds`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `DrawMaskOnImage`
- `BlockifyMask`
- `Reroute`
- `SeCModelLoader`
- `WanVideoTextEncodeCached`
- `Reroute`
- `WanVideoDecode`
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `PreviewImage`
- `easy showAnything`
- `PrimitiveInt`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `PreviewImage`
- `PointsEditor`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageFromBatch`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `PoseAndFaceDetection`
- `DrawViTPose`
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
- `GrowMaskWithBlur`
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
- `WanVideoVAELoader`
- `Reroute`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoBlockSwap`
- `Reroute`
- `Reroute`
- `easy int`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `DrawMaskOnImage`
- `BlockifyMask`
- `Reroute`
- `SeCModelLoader`
- `WanVideoTextEncodeCached`
- `Reroute`
- `WanVideoDecode`
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `PreviewImage`
- `easy showAnything`
- `PrimitiveInt`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `PointsEditor`
- `PreviewImage`
- `WanVideoAnimateEmbeds`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **36%**（69/194）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`DrawViTPose`、`GrowMaskWithBlur`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoBlockSwap`、`easy int`、`WanVideoAnimateEmbeds`、`SeCVideoSegmentation`、`VHS_VideoCombine`、`DrawMaskOnImage`、`BlockifyMask`、`SeCModelLoader`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ImageResizeKJv2`、`INTConstant`、`VHS_LoadVideo`、`PointsEditor`、`WanVideoLoraSelectMulti`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

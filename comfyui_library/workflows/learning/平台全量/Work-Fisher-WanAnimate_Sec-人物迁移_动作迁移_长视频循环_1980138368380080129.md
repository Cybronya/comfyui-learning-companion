---
key: 平台全量/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1980138368380080129.json
name: Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1980138368380080129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1980138368380080129.json
hash: 1d5d076c75fa594e
coverage: 0.352332
learned_at: 2026-11-14 01:07:24
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GetImageSizeAndCount, OnnxDetectionModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageFromBatch, WanVideoModelLoader, WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GrowMaskWithBlur, Reroute, Reroute, Reroute, Reroute, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoVAELoader, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, Reroute, Reroute, Reroute, WanVideoBlockSwap, Reroute, Reroute, easy int, WanVideoAnimateEmbeds, SeCVideoSegmentation, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Reroute, Reroute, DrawMaskOnImage, BlockifyMask, Reroute, SeCModelLoader, WanVideoTextEncodeCached, Reroute, WanVideoDecode, Reroute, VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, PreviewImage, easy showAnything, PrimitiveInt, INTConstant, INTConstant, LoadImage, VHS_LoadVideo, PreviewImage, PointsEditor, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GetImageSizeAndCount, OnnxDetectionModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageFromBatch, WanVideoModelLoader, WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GrowMaskWithBlur, Reroute, Reroute, Reroute, Reroute, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoVAELoader, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, Reroute, Reroute, Reroute, WanVideoBlockSwap, Reroute, Reroute, easy int, SeCVideoSegmentation, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Reroute, Reroute, DrawMaskOnImage, BlockifyMask, Reroute, SeCModelLoader, WanVideoTextEncodeCached, Reroute, WanVideoDecode, Reroute, VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, PreviewImage, easy showAnything, PrimitiveInt, INTConstant, INTConstant, LoadImage, VHS_LoadVideo, PointsEditor, PreviewImage, WanVideoAnimateEmbeds, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 平台全量/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1980138368380080129.json

> 来源文件 `comfyui_library/workflows/平台全量/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_1980138368380080129.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（193 个）：
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
- `LoadImage`
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
- `LoadImage`
- `VHS_LoadVideo`
- `PointsEditor`
- `PreviewImage`
- `WanVideoAnimateEmbeds`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **35%**（68/193）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`DrawViTPose`、`GrowMaskWithBlur`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoBlockSwap`、`easy int`、`WanVideoAnimateEmbeds`、`SeCVideoSegmentation`、`VHS_VideoCombine`、`DrawMaskOnImage`、`BlockifyMask`、`SeCModelLoader`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ImageResizeKJv2`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`、`PointsEditor`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs

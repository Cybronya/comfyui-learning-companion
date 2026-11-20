---
key: 平台全量/Wan2.2 Animate V2全自动视频人物替换_1978460418932887554.json
name: Wan2.2 Animate V2全自动视频人物替换_1978460418932887554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate V2全自动视频人物替换_1978460418932887554.json
hash: e5d6dfcfe47b432c
coverage: 1
learned_at: 2026-11-14 01:04:52
nodes: [WanVideoTorchCompileSettings, WanVideoClipVisionEncode, CLIPVisionLoader, SimpleMath+, INTConstant, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoSampler, LoadImage, VHS_LoadVideo, ImageResizeKJv2, INTConstant, INTConstant, GrowMask, BlockifyMask, PoseAndFaceDetection, WanVideoVAELoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, OnnxDetectionModelLoader, DownloadAndLoadSAM2Model, Sam2Segmentation, DrawViTPose, ACE_ImageFaceCrop, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelectMulti, VHS_VideoCombine, DrawMaskOnImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate V2全自动视频人物替换_1978460418932887554.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate V2全自动视频人物替换_1978460418932887554.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `SimpleMath+`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `GrowMask`
- `BlockifyMask`
- `PoseAndFaceDetection`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `OnnxDetectionModelLoader`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `DrawViTPose`
- `ACE_ImageFaceCrop`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `DrawMaskOnImage`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`SimpleMath+`、`INTConstant`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`LoadImage`、`VHS_LoadVideo`、`ImageResizeKJv2`、`GrowMask`、`BlockifyMask`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`DrawViTPose`、`ACE_ImageFaceCrop`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`DrawMaskOnImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader

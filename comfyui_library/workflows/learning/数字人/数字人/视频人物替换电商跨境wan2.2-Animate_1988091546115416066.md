---
key: 数字人/数字人/视频人物替换电商跨境wan2.2-Animate_1988091546115416066.json
name: 视频人物替换电商跨境wan2.2-Animate_1988091546115416066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频人物替换电商跨境wan2.2-Animate_1988091546115416066.json
hash: 160bd3d062a1ac3c
coverage: 0.55
learned_at: 2026-10-26 02:04:48
nodes: [GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GetNode, WanVideoDecode, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, GetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, Note, WanVideoTextEncodeCached, GetNode, GetNode, VHS_VideoCombine, GetNode, CLIPVisionLoader, SetNode, INTConstant, SetNode, INTConstant, ImageResizeKJv2, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, DrawViTPose, GetImageSizeAndCount, easy float, SetNode, ConvertAny2Int, SeCVideoSegmentation, WanVideoLoraSelectMulti, GrowMaskWithBlur, BlockifyMask, SetNode, DrawMaskOnImage, SetNode, GetNode, SeCModelLoader, GetNode, GetNode, Text, easy showAnything, Note, LoadImage, PointsEditor, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, easy cleanGpuUsed, WanVideoAnimateEmbeds, easy cleanGpuUsed, WanVideoSampler, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/视频人物替换电商跨境wan2.2-Animate_1988091546115416066.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频人物替换电商跨境wan2.2-Animate_1988091546115416066.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（80 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `Note`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `easy float`
- `SetNode`
- `ConvertAny2Int`
- `SeCVideoSegmentation`
- `WanVideoLoraSelectMulti`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `SeCModelLoader`
- `GetNode`
- `GetNode`
- `Text`
- `easy showAnything`
- `Note`
- `LoadImage`
- `PointsEditor`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **55%**（44/80）

**有卡**：`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`WanVideoDecode`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`INTConstant`、`ImageResizeKJv2`、`DrawViTPose`、`easy float`、`ConvertAny2Int`、`SeCVideoSegmentation`、`WanVideoLoraSelectMulti`、`GrowMaskWithBlur`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`Text`、`LoadImage`、`PointsEditor`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

---
key: 视频生成/图生视频/Animate影视二创（单人版）V1.0_2037017744700346369.json
name: Animate影视二创（单人版）V1.0_2037017744700346369.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037017744700346369.json
hash: 02f0b208c784ce9e
coverage: 0.507042
learned_at: 2026-10-15 22:35:54
nodes: [DrawViTPose, Bookmark (rgthree), WanVideoAnimateEmbeds, WanVideoClipVisionEncode, GetNode, easy sam3VideoModelExtraConfig, DrawMaskOnImage, VHS_VideoCombine, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, easy sam3ModelLoader, GrowMaskWithBlur, GetNode, GetNode, PoseAndFaceDetection, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, WanVideoBlockSwap, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoSampler, GetNode, WanVideoDecode, SetNode, GetNode, PlaySound|pysssss, easy sam3VideoSegmentation, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, SetNode, SetNode, VHS_VideoCombine, INTConstant, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoModelLoader, CLIPVisionLoader, WanVideoTextEncodeCached, WanVideoVAELoader, VHS_LoadVideo, LoadImage, easy framesEditor, INTConstant, INTConstant, BlockifyMask, BlockifyMask]
patterns: []
missing: []
---

# 视频生成/图生视频/Animate影视二创（单人版）V1.0_2037017744700346369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037017744700346369.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（71 个）：
- `DrawViTPose`
- `Bookmark (rgthree)`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `GetNode`
- `easy sam3VideoModelExtraConfig`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `easy sam3ModelLoader`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `PlaySound|pysssss`
- `easy sam3VideoSegmentation`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `LoadImage`
- `easy framesEditor`
- `INTConstant`
- `INTConstant`
- `BlockifyMask`
- `BlockifyMask`

## 知识

覆盖率 **51%**（36/71）

**有卡**：`DrawViTPose`、`Bookmark (rgthree)`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`easy sam3VideoModelExtraConfig`、`DrawMaskOnImage`、`VHS_VideoCombine`、`ImageResizeKJv2`、`easy sam3ModelLoader`、`GrowMaskWithBlur`、`PoseAndFaceDetection`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`PlaySound|pysssss`、`easy sam3VideoSegmentation`、`OnnxDetectionModelLoader`、`INTConstant`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LoadImage`、`easy framesEditor`、`BlockifyMask`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

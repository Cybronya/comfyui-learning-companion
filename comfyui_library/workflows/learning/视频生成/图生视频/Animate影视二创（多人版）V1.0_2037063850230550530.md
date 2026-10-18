---
key: 视频生成/图生视频/Animate影视二创（多人版）V1.0_2037063850230550530.json
name: Animate影视二创（多人版）V1.0_2037063850230550530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Animate影视二创（多人版）V1.0_2037063850230550530.json
hash: d9bfbf87a39f875f
coverage: 0.517857
learned_at: 2026-10-15 22:35:54
nodes: [Bookmark (rgthree), VHS_VideoCombine, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, PoseAndFaceDetection, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoSampler, GetNode, WanVideoDecode, SetNode, PlaySound|pysssss, OnnxDetectionModelLoader, GetNode, GetNode, SetNode, INTConstant, INTConstant, INTConstant, ImageResizeKJv2, easy imageSizeBySide, DWPreprocessor, SetNode, GetNode, GetNode, ResizeImageMaskNode, GetNode, VHS_VideoCombine, SetNode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, GetNode, GetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, SetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoTextEncodeCached, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Animate影视二创（多人版）V1.0_2037063850230550530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037063850230550530.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `Bookmark (rgthree)`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PoseAndFaceDetection`
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
- `PlaySound|pysssss`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `easy imageSizeBySide`
- `DWPreprocessor`
- `SetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **52%**（29/56）

**有卡**：`Bookmark (rgthree)`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`PlaySound|pysssss`、`OnnxDetectionModelLoader`、`INTConstant`、`ImageResizeKJv2`、`easy imageSizeBySide`、`DWPreprocessor`、`ResizeImageMaskNode`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

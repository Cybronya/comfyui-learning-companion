---
key: 数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json
name: 表情迁移 - Wan2.1_1966784793595850754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json
hash: 2ddb54e32911aa5e
coverage: 0.707317
learned_at: 2026-10-26 02:04:42
nodes: [WanVideoModelLoader, Anything Everywhere, GetNode, WanVideoSampler, INTConstant, INTConstant, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoDecode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, SetNode, GetNode, ImageResizeKJv2, PreviewImage, CLIPVisionLoader, GetNode, LoadImage, SetNode, INTConstant, GetNode, ImageResizeKJv2, GetNode, FantasyPortraitModelLoader, FantasyPortraitFaceDetector, WanVideoAddFantasyPortrait, easy cleanGpuUsed, WanVideoTorchCompileSettings, FantasyPortraitModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoContextOptions, VHS_LoadVideo, SimpleMath+, easy showAnything, VHS_VideoCombine, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetNode]
patterns: []
missing: []
---

# 数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `WanVideoModelLoader`
- `Anything Everywhere`
- `GetNode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `CLIPVisionLoader`
- `GetNode`
- `LoadImage`
- `SetNode`
- `INTConstant`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `FantasyPortraitModelLoader`
- `FantasyPortraitFaceDetector`
- `WanVideoAddFantasyPortrait`
- `easy cleanGpuUsed`
- `WanVideoTorchCompileSettings`
- `FantasyPortraitModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoContextOptions`
- `VHS_LoadVideo`
- `SimpleMath+`
- `easy showAnything`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `GetNode`

## 知识

覆盖率 **71%**（29/41）

**有卡**：`WanVideoModelLoader`、`WanVideoSampler`、`INTConstant`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoDecode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`CLIPVisionLoader`、`LoadImage`、`FantasyPortraitModelLoader`、`FantasyPortraitFaceDetector`、`WanVideoAddFantasyPortrait`、`easy cleanGpuUsed`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`WanVideoContextOptions`、`VHS_LoadVideo`、`SimpleMath+`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

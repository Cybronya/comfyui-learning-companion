---
key: 视频生成/图生视频/Wan2.1 Fun FLF2V 首尾帧生视频 Kijai_1930856714751684610.json
name: Wan2.1 Fun FLF2V 首尾帧生视频 Kijai_1930856714751684610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 Fun FLF2V 首尾帧生视频 Kijai_1930856714751684610.json
hash: bf19d673ac5e5a5f
coverage: 0.714286
learned_at: 2026-10-15 22:30:07
nodes: [WanVideoTextEmbedBridge, CLIPTextEncode, CLIPLoader, CLIPTextEncode, Note, WanVideoVRAMManagement, Note, Note, Note, LoadWanVideoT5TextEncoder, Note, Note, Note, WanVideoTorchCompileSettings, Note, CLIPVisionLoader, WanVideoTeaCache, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, WanVideoDecode, SetNode, VHS_VideoCombine, WanVideoVAELoader, SetNode, ImageResize+, ImageResize+, WanVideoClipVisionEncode, WanVideoSampler, WanVideoSLG, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoImageToVideoEncode, LoadImage, WanVideoTextEncode, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 Fun FLF2V 首尾帧生视频 Kijai_1930856714751684610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930856714751684610.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoTextEmbedBridge`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `WanVideoVRAMManagement`
- `Note`
- `Note`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `Note`
- `CLIPVisionLoader`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `SetNode`
- `ImageResize+`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `WanVideoTextEncode`
- `LoadImage`

## 知识

覆盖率 **71%**（25/35）

**有卡**：`WanVideoTextEmbedBridge`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoVRAMManagement`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`ImageResize+`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode

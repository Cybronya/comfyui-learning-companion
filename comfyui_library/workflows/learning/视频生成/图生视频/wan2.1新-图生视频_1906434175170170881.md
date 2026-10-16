---
key: 视频生成/图生视频/wan2.1新-图生视频_1906434175170170881.json
name: wan2.1新-图生视频_1906434175170170881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1906434175170170881.json
hash: 84e22a3ca3e6c1fd
coverage: 0.576271
learned_at: 2026-10-15 22:29:27
nodes: [WanVideoBlockSwap, Note, Note, Note, Note, Note, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, WanVideoExperimentalArgs, GetNode, SetNode, GetNode, JoinStrings, JoinStrings, SetNode, Note, GetNode, GetNode, WanVideoTextEncode, GetNode, GetNode, WanVideoVRAMManagement, WanVideoImageClipEncode, SetNode, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoSLG, SetNode, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoTeaCache, String Literal, String Literal, VHS_VideoCombine, String Literal, easy float, String Literal, easy int, easy int, String Literal, Bookmark (rgthree), Note Plus (mtb), String Literal, String Literal, MarkdownNote, easy int, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, LoadImage, easy seed, easy positive]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1新-图生视频_1906434175170170881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1906434175170170881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（59 个）：
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoExperimentalArgs`
- `GetNode`
- `SetNode`
- `GetNode`
- `JoinStrings`
- `JoinStrings`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `WanVideoVRAMManagement`
- `WanVideoImageClipEncode`
- `SetNode`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `SetNode`
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoTeaCache`
- `String Literal`
- `String Literal`
- `VHS_VideoCombine`
- `String Literal`
- `easy float`
- `String Literal`
- `easy int`
- `easy int`
- `String Literal`
- `Bookmark (rgthree)`
- `Note Plus (mtb)`
- `String Literal`
- `String Literal`
- `MarkdownNote`
- `easy int`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `LoadImage`
- `easy seed`
- `easy positive`

## 知识

覆盖率 **58%**（34/59）

**有卡**：`WanVideoBlockSwap`、`WanVideoExperimentalArgs`、`JoinStrings`、`WanVideoTextEncode`、`WanVideoVRAMManagement`、`WanVideoImageClipEncode`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`String Literal`、`VHS_VideoCombine`、`easy float`、`easy int`、`Bookmark (rgthree)`、`Note Plus (mtb)`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`LoadImage`、`easy seed`、`easy positive`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode

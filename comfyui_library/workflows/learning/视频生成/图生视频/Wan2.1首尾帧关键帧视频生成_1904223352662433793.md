---
key: 视频生成/图生视频/Wan2.1首尾帧关键帧视频生成_1904223352662433793.json
name: Wan2.1首尾帧关键帧视频生成_1904223352662433793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1904223352662433793.json
hash: e1635c352bd88be2
coverage: 0.545455
learned_at: 2026-10-15 22:29:25
nodes: [LoadImage, GetNode, GetNode, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, LoadWanVideoClipTextEncoder, SetNode, LoadWanVideoT5TextEncoder, ImageResize+, GetNode, WanVideoTextEncode, WanVideoTeaCache, WanVideoModelLoader, WanVideoVAELoader, Anything Everywhere, WanVideoVRAMManagement, WanVideoTorchCompileSettings, ImageResize+, Note, WanVideoSampler, WanVideoDecode, RIFE VFI, VHS_VideoCombine, GetNode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1首尾帧关键帧视频生成_1904223352662433793.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1904223352662433793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（33 个）：
- `LoadImage`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadWanVideoClipTextEncoder` ★核心
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `ImageResize+`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `WanVideoVRAMManagement`
- `WanVideoTorchCompileSettings`
- `ImageResize+`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `RIFE VFI`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **55%**（18/33）

**有卡**：`LoadImage`、`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`ImageResize+`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoVRAMManagement`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoDecode`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

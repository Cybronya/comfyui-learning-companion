---
key: 视频生成/文生视频/Wan2.1 FusionX文生视频工作流_1961757456491810818.json
name: Wan2.1 FusionX文生视频工作流_1961757456491810818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1 FusionX文生视频工作流_1961757456491810818.json
hash: 77938127ddbc07f8
coverage: 0.789474
learned_at: 2026-10-15 22:43:43
nodes: [WanVideoSLG, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTeaCache, WanVideoSampler, WanVideoBlockSwap, easy showAnything, SimpleMath+, Note, Note, WanVideoTorchCompileSettings, MarkdownNote, WanVideoDecode, Int, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 FusionX文生视频工作流_1961757456491810818.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1961757456491810818.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（19 个）：
- `WanVideoSLG`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `easy showAnything`
- `SimpleMath+`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `WanVideoDecode`
- `Int`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`WanVideoSLG`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`Int`、`WanVideoEmptyEmbeds`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、Int、VHS_VideoCombine、WanVideoBlockSwap

---
key: 视频生成/文生视频/Wan2.1 Kijai 文生视频_1947899164087713793.json
name: Wan2.1 Kijai 文生视频_1947899164087713793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1947899164087713793.json
hash: 593537dd59c0146b
coverage: 0.75
learned_at: 2026-10-15 22:43:32
nodes: [WanVideoDecode, WanVideoTeaCache, WanVideoEnhanceAVideo, VHS_VideoCombine, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoTorchCompileSettings, Note, WanVideoVRAMManagement, Note, WanVideoEmptyEmbeds, WanVideoBlockSwap, Note, Note, Note, WanVideoModelLoader, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 Kijai 文生视频_1947899164087713793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1947899164087713793.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（20 个）：
- `WanVideoDecode`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `Note`
- `WanVideoVRAMManagement`
- `Note`
- `WanVideoEmptyEmbeds`
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoVRAMManagement`、`WanVideoEmptyEmbeds`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader

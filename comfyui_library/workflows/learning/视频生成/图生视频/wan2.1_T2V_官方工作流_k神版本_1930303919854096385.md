---
key: 视频生成/图生视频/wan2.1_T2V_官方工作流_k神版本_1930303919854096385.json
name: wan2.1_T2V_官方工作流_k神版本_1930303919854096385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1_T2V_官方工作流_k神版本_1930303919854096385.json
hash: bf66f53d3b5308c3
coverage: 0.68
learned_at: 2026-10-15 22:30:05
nodes: [CLIPTextEncode, Note, CLIPTextEncode, WanVideoTextEmbedBridge, CLIPLoader, WanVideoVRAMManagement, Note, Note, Note, WanVideoModelLoader, Note, Note, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoTextEncode, WanVideoBlockSwap, WanVideoEnhanceAVideo, WanVideoTeaCache, Note, Note, WanVideoSampler, WanVideoVAELoader, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1_T2V_官方工作流_k神版本_1930303919854096385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930303919854096385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `WanVideoTextEmbedBridge`
- `CLIPLoader`
- `WanVideoVRAMManagement`
- `Note`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **68%**（17/25）

**有卡**：`CLIPTextEncode`、`WanVideoTextEmbedBridge`、`CLIPLoader`、`WanVideoVRAMManagement`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、CLIPLoader、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、VHS_VideoCombine

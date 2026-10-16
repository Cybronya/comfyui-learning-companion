---
key: 视频生成/文生视频/wan2.2文生视频(KJ版)_1951284821798670338.json
name: wan2.2文生视频(KJ版)_1951284821798670338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1951284821798670338.json
hash: 8c6cf59eae22dd5f
coverage: 0.892857
learned_at: 2026-10-15 22:43:37
nodes: [WanVideoModelLoader, WanVideoDecode, RIFE VFI, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoVAELoader, INTConstant, INTConstant, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, WanVideoEmptyEmbeds, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, LoadWanVideoT5TextEncoder, WanVideoTextEncode, MarkdownNote, WanVideoSampler, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2文生视频(KJ版)_1951284821798670338.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951284821798670338.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（28 个）：
- `WanVideoModelLoader`
- `WanVideoDecode`
- `RIFE VFI`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoEmptyEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `MarkdownNote`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心

## 知识

覆盖率 **89%**（25/28）

**有卡**：`WanVideoModelLoader`、`WanVideoDecode`、`RIFE VFI`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`INTConstant`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

---
key: 视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2050481503284539394.json
name: WAN2.2-4步极速版_文生视频-KJ版工作流_2050481503284539394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2050481503284539394.json
hash: 8d96278d3bda8e1a
coverage: 1
learned_at: 2026-10-15 22:47:04
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, CreateCFGScheduleFloatList, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2050481503284539394.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2050481503284539394.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（16 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、VHS_VideoCombine

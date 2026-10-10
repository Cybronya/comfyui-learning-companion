---
key: 视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2017851048295145474.json
name: WAN2.2-4步极速版_文生视频-KJ版工作流_2017851048295145474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2017851048295145474.json
hash: 706abacd6870afb9
coverage: 0.75
learned_at: 2026-10-11 03:16:49
nodes: [WanVideoDecode, WanVideoVAELoader, Note, Reroute, Reroute, Note, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoEmptyEmbeds, WanVideoTextEncode, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2017851048295145474.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2017851048295145474.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（20 个）：
- `WanVideoDecode`
- `WanVideoVAELoader`
- `Note`
- `Reroute`
- `Reroute`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `MarkdownNote`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、VHS_VideoCombine

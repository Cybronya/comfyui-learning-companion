---
key: 视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2046206194833952769.json
name: WAN2.2-6步极速版-图生视频-KJ版工作流_2046206194833952769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2046206194833952769.json
hash: 1d78c5cbb8e0ccf7
coverage: 0.809524
learned_at: 2026-10-15 22:36:56
nodes: [LoadWanVideoT5TextEncoder, Reroute, WanVideoTorchCompileSettings, Reroute, Note, Note, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, LoadImage, WanVideoTextEncode, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2046206194833952769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046206194833952769.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `LoadWanVideoT5TextEncoder`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `Reroute`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`LoadImage`、`WanVideoTextEncode`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

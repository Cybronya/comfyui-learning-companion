---
key: 视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2017911981818253314.json
name: WAN2.2-6步极速版-图生视频-KJ版工作流_2017911981818253314.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2017911981818253314.json
hash: c82fa58db045472f
coverage: 0.772727
learned_at: 2026-10-15 22:34:51
nodes: [LoadWanVideoT5TextEncoder, WanVideoDecode, Reroute, WanVideoTorchCompileSettings, Reroute, Note, VHS_VideoCombine, Note, WanVideoImageToVideoEncode, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, MarkdownNote, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2017911981818253314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017911981818253314.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `Reroute`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `MarkdownNote`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

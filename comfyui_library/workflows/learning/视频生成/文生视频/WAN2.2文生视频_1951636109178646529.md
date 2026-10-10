---
key: 视频生成/文生视频/WAN2.2文生视频_1951636109178646529.json
name: WAN2.2文生视频_1951636109178646529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2文生视频_1951636109178646529.json
hash: a8b60e8432dd9220
coverage: 1
learned_at: 2026-10-10 23:06:03
nodes: [WanVideoDecode, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, VHS_VideoCombine, WanVideoEmptyEmbeds, MuyeTextEditOutput]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.2文生视频_1951636109178646529.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2文生视频_1951636109178646529.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（22 个）：
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `MuyeTextEditOutput`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`WanVideoDecode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoEmptyEmbeds`、`MuyeTextEditOutput`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

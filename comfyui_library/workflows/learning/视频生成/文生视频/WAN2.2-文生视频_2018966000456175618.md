---
key: 视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json
name: WAN2.2-文生视频_2018966000456175618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json
hash: d6f02f6a1036f6b1
coverage: 1
learned_at: 2026-10-15 22:47:04
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoEmptyEmbeds, Float to Int, WanVideoTextEncode, Int, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoVAELoader, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, Float, MathExpression_UTK, MuyeTextEditOutput]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（26 个）：
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
- `WanVideoEmptyEmbeds`
- `Float to Int`
- `WanVideoTextEncode`
- `Int`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Float`
- `MathExpression_UTK`
- `MuyeTextEditOutput`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoEmptyEmbeds`、`Float to Int`、`WanVideoTextEncode`、`Int`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`、`Float`、`MathExpression_UTK`、`MuyeTextEditOutput`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

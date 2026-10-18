---
key: 视频生成/文生视频/Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json
name: Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json
hash: c13c7c96299df4b5
coverage: 0.83871
learned_at: 2026-10-15 22:43:35
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoEmptyEmbeds, CreateCFGScheduleFloatList, WanVideoSampler, easy seed, Reroute, Reroute, WanVideoSampler, DF_Integer, DF_Integer, DF_Integer, DF_Integer, WanVideoDecode, DF_Integer, WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, MathExpression|pysssss, WanVideoTextEncode, PrimitiveStringMultiline, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, Reroute, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950379943495647234.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（31 个）：
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Reroute`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoEmptyEmbeds`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `easy seed`
- `Reroute`
- `Reroute`
- `WanVideoSampler` ★核心
- `DF_Integer`
- `DF_Integer`
- `DF_Integer`
- `DF_Integer`
- `WanVideoDecode`
- `DF_Integer`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `WanVideoTextEncode`
- `PrimitiveStringMultiline`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Reroute`
- `VHS_VideoCombine`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`easy seed`、`DF_Integer`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect

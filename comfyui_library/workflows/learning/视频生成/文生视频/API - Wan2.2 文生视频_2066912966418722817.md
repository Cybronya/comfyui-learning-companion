---
key: 视频生成/文生视频/API - Wan2.2 文生视频_2066912966418722817.json
name: API - Wan2.2 文生视频_2066912966418722817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/API - Wan2.2 文生视频_2066912966418722817.json
hash: 0f520998e821860f
coverage: 0.944444
learned_at: 2026-10-15 22:44:01
nodes: [DF_Integer, Note, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoVAELoader, WanVideoSampler, CreateCFGScheduleFloatList, MathExpression|pysssss, INTConstant, SimpleMath+, easy int, PrimitiveNode, WanVideoDecode, GetImageSizeAndCount, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, JWInteger, JWInteger, Text _O]
patterns: []
missing: []
---

# 视频生成/文生视频/API - Wan2.2 文生视频_2066912966418722817.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/API - Wan2.2 文生视频_2066912966418722817.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `DF_Integer`
- `Note`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `MathExpression|pysssss`
- `INTConstant`
- `SimpleMath+`
- `easy int`
- `PrimitiveNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `JWInteger`
- `JWInteger`
- `Text _O`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`DF_Integer`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`MathExpression|pysssss`、`INTConstant`、`SimpleMath+`、`easy int`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`JWInteger`、`Text _O`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

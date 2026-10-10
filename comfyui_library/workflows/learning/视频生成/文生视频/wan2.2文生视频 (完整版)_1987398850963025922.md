---
key: 视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json
name: wan2.2文生视频 (完整版)_1987398850963025922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json
hash: d3b6eefe3dade467
coverage: 0.826087
learned_at: 2026-10-11 02:45:03
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoDecode, WanVideoLoraSelect, Int, Int, INTConstant, INTConstant, Int, WanVideoModelLoader, WanVideoModelLoader, RIFE VFI, VHS_VideoCombine, WanVideoEmptyEmbeds, MathExpression|pysssss, WanVideoVAELoader, LoadWanVideoT5TextEncoder, MarkdownNote, CR Text, WanVideoTextEncode]
patterns: []
missing: [CR Text, MathExpression|pysssss, RIFE VFI]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（23 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `Int`
- `Int`
- `INTConstant`
- `INTConstant`
- `Int`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `MarkdownNote`
- `CR Text`
- `WanVideoTextEncode`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoLoraSelect`、`Int`、`INTConstant`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`

**缺卡**（3）：`CR Text`、`MathExpression|pysssss`、`RIFE VFI`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、Int

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识

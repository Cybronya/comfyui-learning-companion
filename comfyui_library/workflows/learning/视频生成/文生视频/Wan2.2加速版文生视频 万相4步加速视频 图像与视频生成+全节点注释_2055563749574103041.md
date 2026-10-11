---
key: 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041.json
name: Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041.json
hash: dd654a95d2da0804
coverage: 0.484848
learned_at: 2026-10-11 19:49:43
nodes: [WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, easy seed, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, MathExpression|pysssss, WanVideoEmptyEmbeds, JWInteger, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, Int, WanVideoSetLoRAs, ImpactInt, ImpactInt, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoTorchCompileSettings, Float, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoDecode, WanVideoTextEncode]
patterns: []
missing: [MathExpression|pysssss, easy seed]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（66 个）：
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy seed`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Int`
- `WanVideoSetLoRAs`
- `ImpactInt`
- `ImpactInt`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoTorchCompileSettings`
- `Float`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncode`

## 知识

覆盖率 **48%**（32/66）

**有卡**：`WanVideoVAELoader`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`JWInteger`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`Int`、`ImpactInt`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`WanVideoTorchCompileSettings`、`Float`、`LoadImage`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncode`

**缺卡**（2）：`MathExpression|pysssss`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

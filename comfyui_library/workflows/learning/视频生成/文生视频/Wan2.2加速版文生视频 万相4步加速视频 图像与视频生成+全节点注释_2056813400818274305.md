---
key: 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305.json
name: Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305.json
hash: be53885301d6bce4
coverage: 0.515152
learned_at: 2026-10-15 22:47:13
nodes: [WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, easy seed, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, MathExpression|pysssss, WanVideoEmptyEmbeds, JWInteger, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, Int, WanVideoSetLoRAs, ImpactInt, ImpactInt, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoTorchCompileSettings, Float, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoDecode, WanVideoTextEncode, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305.json`

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
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncode`
- `LoadImage`

## 知识

覆盖率 **52%**（34/66）

**有卡**：`WanVideoVAELoader`、`WanVideoModelLoader`、`easy seed`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`、`JWInteger`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`Int`、`ImpactInt`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`WanVideoTorchCompileSettings`、`Float`、`LoadImage`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

---
key: 数字人/数字人/10Eros-miniMax 8步极速生成人物资产四视图v2.0_2087065573468495873.json
name: 10Eros-miniMax 8步极速生成人物资产四视图v2.0_2087065573468495873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/10Eros-miniMax 8步极速生成人物资产四视图v2.0_2087065573468495873.json
hash: ae8a63c768ef26e4
coverage: 0.918919
learned_at: 2026-10-18 19:07:39
nodes: [ConditioningZeroOut, VAEDecode, ConditioningZeroOut, VAEDecode, ConditioningZeroOut, VAEDecode, SaveImage, ConditioningZeroOut, VAEDecode, SaveImage, CLIPLoader, VAELoader, VAELoader, KSampler, KSampler, KSampler, KSampler, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, SaveImage, Note, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, SaveImage, SaveImage, UNETLoader, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, MmuuaiGroupBypass, ImageConcatMulti]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 666, "steps": 25}
---

# 数字人/数字人/10Eros-miniMax 8步极速生成人物资产四视图v2.0_2087065573468495873.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/10Eros-miniMax 8步极速生成人物资产四视图v2.0_2087065573468495873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `SaveImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `MmuuaiGroupBypass`
- `ImageConcatMulti`

## 关键参数

- `seed` = `666`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`KSampler`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`ImageFromBatch`、`UNETLoader`、`LoraLoaderModelOnly`、`MmuuaiGroupBypass`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

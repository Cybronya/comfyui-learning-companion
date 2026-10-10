---
key: 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json
name: Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json
hash: 1e645f28cf2c1138
coverage: 0.88
learned_at: 2026-10-11 03:16:50
nodes: [Reroute, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, VAEDecode, VHS_VideoCombine, KSamplerAdvanced, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, CR Text, JWInteger, JWInteger, JWInteger, MathExpression|pysssss]
patterns: []
missing: [CR Text, MathExpression|pysssss]
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+官方版）_2019642699384627202.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `Reroute`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`KSamplerAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`JWInteger`

**缺卡**（2）：`CR Text`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识

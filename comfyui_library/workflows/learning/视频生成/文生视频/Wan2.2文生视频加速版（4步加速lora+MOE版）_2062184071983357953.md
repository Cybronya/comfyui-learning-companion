---
key: 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json
name: Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json
hash: 0ed1e55c3a6c7789
coverage: 0.913043
learned_at: 2026-10-15 22:47:15
nodes: [VHS_VideoCombine, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Note, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, PathchSageAttentionKJ, WanMoeKSampler, CLIPLoader, VAEDecode, CLIPTextEncode, CR Text, EmptyHunyuanLatentVideo, JWInteger, MathExpression|pysssss, JWInteger, JWInteger, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频加速版（4步加速lora+MOE版）_2062184071983357953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PathchSageAttentionKJ`
- `WanMoeKSampler` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VHS_VideoCombine`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`WanMoeKSampler`、`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`CR Text`、`EmptyHunyuanLatentVideo`、`JWInteger`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、EmptyHunyuanLatentVideo

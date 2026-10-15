---
key: 视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json
name: Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json
hash: c1b1f4ecac193dd4
coverage: 0.9375
learned_at: 2026-10-15 22:47:00
nodes: [PathchSageAttentionKJ, EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, JWInteger, JWInteger, INTConstant, INTConstant, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, TextConcat, CR Prompt Text, easy showAnything, JWInteger, CLIPTextEncode, easy showAnything, SDVN Any Show, CLIPTextEncode, PathchSageAttentionKJ, Qwen3_VQA, CR Prompt Text, LoraLoaderModelOnly, UNETLoader, VAEDecode, ImageFromBatch+, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextConcat`
- `CR Prompt Text`
- `easy showAnything`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `SDVN Any Show`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`JWInteger`、`INTConstant`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`TextConcat`、`CR Prompt Text`、`CLIPTextEncode`、`SDVN Any Show`、`Qwen3_VQA`、`VAEDecode`、`ImageFromBatch+`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

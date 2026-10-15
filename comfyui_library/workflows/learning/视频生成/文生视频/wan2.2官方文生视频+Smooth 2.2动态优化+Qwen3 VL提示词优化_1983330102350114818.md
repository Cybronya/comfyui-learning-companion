---
key: 视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json
name: wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json
hash: 767156d8452bbb95
coverage: 0.933333
learned_at: 2026-10-15 22:47:36
nodes: [EmptyHunyuanLatentVideo, TextConcat, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, VAEDecode, INTConstant, INTConstant, easy showAnything, SDVN Any Show, CLIPLoader, VAELoader, CR Prompt Text, JWInteger, JWInteger, JWInteger, ImageFromBatch+, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, easy showAnything, CR Prompt Text, Qwen3_VQA, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `EmptyHunyuanLatentVideo`
- `TextConcat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `easy showAnything`
- `SDVN Any Show`
- `CLIPLoader`
- `VAELoader`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `ImageFromBatch+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `easy showAnything`
- `CR Prompt Text`
- `Qwen3_VQA`
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`EmptyHunyuanLatentVideo`、`TextConcat`、`CLIPTextEncode`、`ModelSamplingSD3`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAEDecode`、`INTConstant`、`SDVN Any Show`、`CLIPLoader`、`VAELoader`、`CR Prompt Text`、`JWInteger`、`ImageFromBatch+`、`KSamplerAdvanced`、`VHS_VideoCombine`、`Qwen3_VQA`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

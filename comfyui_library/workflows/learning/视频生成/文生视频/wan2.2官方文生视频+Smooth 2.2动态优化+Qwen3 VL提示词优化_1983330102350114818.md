---
key: 视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json
name: wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json
hash: 767156d8452bbb95
coverage: 0.766667
learned_at: 2026-10-11 02:45:03
nodes: [EmptyHunyuanLatentVideo, TextConcat, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, VAEDecode, INTConstant, INTConstant, easy showAnything, SDVN Any Show, CLIPLoader, VAELoader, CR Prompt Text, JWInteger, JWInteger, JWInteger, ImageFromBatch+, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, easy showAnything, CR Prompt Text, Qwen3_VQA, CR Prompt Text]
patterns: []
missing: [ImageFromBatch+, SDVN Any Show, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SDVN Any Show` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **77%**（23/30）

**有卡**：`EmptyHunyuanLatentVideo`、`TextConcat`、`CLIPTextEncode`、`ModelSamplingSD3`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAEDecode`、`INTConstant`、`CLIPLoader`、`VAELoader`、`JWInteger`、`KSamplerAdvanced`、`VHS_VideoCombine`、`Qwen3_VQA`

**缺卡**（5）：`ImageFromBatch+`、`SDVN Any Show`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `SDVN Any Show` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

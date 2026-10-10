---
key: 视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json
name: （自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json
hash: b756448992f674ab
coverage: 0.8
learned_at: 2026-10-11 02:45:05
nodes: [PathchSageAttentionKJ, EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, JWInteger, JWInteger, SaveImage, INTConstant, INTConstant, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageFromBatch+, UNETLoader, TextConcat, VAEDecode, SaveImage, TT_img_enc, CR Prompt Text, TT_img_enc_v2, easy showAnything, JWInteger, CLIPTextEncode, Qwen3_VQA, easy showAnything, CR Prompt Text, SDVN Any Show, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, CR Prompt Text]
patterns: []
missing: [ImageFromBatch+, SDVN Any Show, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SDVN Any Show` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `SaveImage`
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageFromBatch+`
- `UNETLoader` ★核心
- `TextConcat`
- `VAEDecode` ★核心
- `SaveImage`
- `TT_img_enc`
- `CR Prompt Text`
- `TT_img_enc_v2`
- `easy showAnything`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `easy showAnything`
- `CR Prompt Text`
- `SDVN Any Show`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CR Prompt Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`JWInteger`、`SaveImage`、`INTConstant`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`TextConcat`、`VAEDecode`、`TT_img_enc`、`TT_img_enc_v2`、`CLIPTextEncode`、`Qwen3_VQA`

**缺卡**（5）：`ImageFromBatch+`、`SDVN Any Show`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `SDVN Any Show` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

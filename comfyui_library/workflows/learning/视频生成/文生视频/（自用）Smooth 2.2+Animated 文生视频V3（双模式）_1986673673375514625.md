---
key: 视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json
name: （自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json
hash: 7b12e467e98689d0
coverage: 0.75
learned_at: 2026-10-11 02:45:05
nodes: [EmptyHunyuanLatentVideo, VAELoader, CLIPLoader, JWInteger, JWInteger, SaveImage, KSamplerAdvanced, VAEDecode, SaveImage, TT_img_enc, TT_img_enc_v2, JWInteger, CLIPTextEncode, Qwen3_VQA, SDVN Any Show, CLIPTextEncode, CR Prompt Text, UNETLoader, ApplySageAttention, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, TextConcat, easy showAnything, KSamplerAdvanced, TextConcat, easy anythingIndexSwitch, easy showAnything, ApplySageAttention, wanBlockSwap, LoraLoaderModelOnly, ModelSamplingSD3, INTConstant, INTConstant, ImageFromBatch+, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, Note, CR Prompt Text, easy showAnything, CR Prompt Text, CR Prompt Text, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [ImageFromBatch+, SDVN Any Show, easy anythingIndexSwitch, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `SDVN Any Show` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `TT_img_enc`
- `TT_img_enc_v2`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `SDVN Any Show`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `UNETLoader` ★核心
- `ApplySageAttention`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TextConcat`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `TextConcat`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `ApplySageAttention`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `INTConstant`
- `INTConstant`
- `ImageFromBatch+`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `Note`
- `CR Prompt Text`
- `easy showAnything`
- `CR Prompt Text`
- `CR Prompt Text`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `beta`

## 知识

覆盖率 **75%**（36/48）

**有卡**：`EmptyHunyuanLatentVideo`、`VAELoader`、`CLIPLoader`、`JWInteger`、`SaveImage`、`KSamplerAdvanced`、`VAEDecode`、`TT_img_enc`、`TT_img_enc_v2`、`CLIPTextEncode`、`Qwen3_VQA`、`UNETLoader`、`ApplySageAttention`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`TextConcat`、`wanBlockSwap`、`LoraLoaderModelOnly`、`INTConstant`

**缺卡**（8）：`ImageFromBatch+`、`SDVN Any Show`、`easy anythingIndexSwitch`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `SDVN Any Show` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

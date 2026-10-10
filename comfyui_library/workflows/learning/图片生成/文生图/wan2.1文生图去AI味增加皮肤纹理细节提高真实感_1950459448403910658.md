---
key: wan2.1文生图去AI味增加皮肤纹理细节提高真实感_1950459448403910658.json
name: wan2.1文生图去AI味增加皮肤纹理细节提高真实感_1950459448403910658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1文生图去AI味增加皮肤纹理细节提高真实感_1950459448403910658.json
hash: ee9a5b35fc8fbe62
coverage: 0.681818
learned_at: 2026-10-10 20:59:26
nodes: [CLIPTextEncode, CLIPTextEncode, CR Text Concatenate, VAELoader, VAEDecode, CLIPSetLastLayer, EmptyHunyuanLatentVideo, SaveImage, TeaCache, MarkdownNote, MarkdownNote, MarkdownNote, KSampler, CR Prompt Text, CR Prompt Text, PathchSageAttentionKJ, MarkdownNote, UNETLoader, CLIPLoader, LoraLoader, LoraLoader, LoraLoader]
patterns: [lora]
missing: [CR Text Concatenate, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1234567890, "steps": 8, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# wan2.1文生图去AI味增加皮肤纹理细节提高真实感_1950459448403910658.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1文生图去AI味增加皮肤纹理细节提高真实感_1950459448403910658.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPSetLastLayer`
- `EmptyHunyuanLatentVideo`
- `SaveImage`
- `TeaCache`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `seed` = `1234567890`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`CLIPSetLastLayer`、`EmptyHunyuanLatentVideo`、`SaveImage`、`TeaCache`、`KSampler`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`LoraLoader`

**缺卡**（3）：`CR Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

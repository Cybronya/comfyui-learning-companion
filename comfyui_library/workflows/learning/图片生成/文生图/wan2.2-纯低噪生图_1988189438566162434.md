---
key: 图片生成/文生图/wan2.2-纯低噪生图_1988189438566162434.json
name: wan2.2-纯低噪生图_1988189438566162434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-纯低噪生图_1988189438566162434.json
hash: 277777782df06c53
coverage: 0.390244
learned_at: 2026-10-09 21:16:00
nodes: [PreviewAny, RH_Translator, RH_Captioner, CLIPLoader, VAELoader, UNETLoader, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, SetNode, SetNode, SaveImage, SetNode, VAEDecode, SetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, LoadImage, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Text Multiline, ModelSamplingSD3, easy seed, SetNode, SetNode, DF_Float, PreviewAny, Text Multiline, INTConstant, KSampler, GetNode, GetNode, SetNode, SetNode, PrimitiveInt, PrimitiveInt]
patterns: []
missing: [Text Multiline, Text Multiline, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 95494355540032, "steps": 6}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.2-纯低噪生图_1988189438566162434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1988189438566162434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（41 个）：
- `PreviewAny`
- `RH_Translator`
- `RH_Captioner`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SaveImage`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`
- `ModelSamplingSD3`
- `easy seed`
- `SetNode`
- `SetNode`
- `DF_Float`
- `PreviewAny`
- `Text Multiline`
- `INTConstant`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `seed` = `95494355540032`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **39%**（16/41）

**有卡**：`RH_Translator`、`RH_Captioner`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`LoadImage`、`ModelSamplingSD3`、`DF_Float`、`INTConstant`、`KSampler`

**缺卡**（3）：`Text Multiline`、`Text Multiline`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

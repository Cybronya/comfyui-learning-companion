---
key: 图片生成/图生图/免费开源flux kontext dev 单图编辑 LLM自能扩写一句修改图-StarAi_1938527111466385409.json
name: 免费开源flux kontext dev 单图编辑 LLM自能扩写一句修改图-StarAi_1938527111466385409
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/免费开源flux kontext dev 单图编辑 LLM自能扩写一句修改图-StarAi_1938527111466385409.json
hash: d23b45d7ada73a83
coverage: 0.941176
learned_at: 2026-10-23 12:13:06
nodes: [UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, VAELoader, ConditioningZeroOut, VAEEncode, ReferenceLatent, FluxGuidance, KSampler, VAEDecode, LoadImage, SaveImage, Note Plus (mtb), MarkdownNote, RH_LLMAPI_NODE, CLIPTextEncode, DeepTranslatorTextNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 791916363692361, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/免费开源flux kontext dev 单图编辑 LLM自能扩写一句修改图-StarAi_1938527111466385409.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/免费开源flux kontext dev 单图编辑 LLM自能扩写一句修改图-StarAi_1938527111466385409.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `Note Plus (mtb)`
- `MarkdownNote`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `791916363692361`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`KSampler`、`VAEDecode`、`LoadImage`、`SaveImage`、`Note Plus (mtb)`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

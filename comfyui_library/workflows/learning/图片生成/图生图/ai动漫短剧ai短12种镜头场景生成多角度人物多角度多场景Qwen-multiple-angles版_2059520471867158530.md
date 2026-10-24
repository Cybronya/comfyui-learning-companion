---
key: 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2059520471867158530.json
name: ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2059520471867158530
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2059520471867158530.json
hash: 86c4cc54d68424dd
coverage: 0.685714
learned_at: 2026-10-23 11:33:37
nodes: [SetNode, SetNode, SetNode, easy promptLine, GetNode, GetNode, ModelSamplingAuraFlow, CFGNorm, PlaySound|pysssss, PlaySound|pysssss, INTConstant, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, JjkText, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, UNETLoader, KSampler, VAEDecode, LayerUtility: PurgeVRAM, SetNode, PlaySound|pysssss, JjkText, CLIPLoader, VAELoader, LoadImage, SaveImage, LoadImage, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 219017731697992, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2059520471867158530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2059520471867158530.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `easy promptLine`
- `GetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `INTConstant`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `JjkText`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `PlaySound|pysssss`
- `JjkText`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `219017731697992`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（24/35）

**有卡**：`easy promptLine`、`ModelSamplingAuraFlow`、`CFGNorm`、`PlaySound|pysssss`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`UNETLoader`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

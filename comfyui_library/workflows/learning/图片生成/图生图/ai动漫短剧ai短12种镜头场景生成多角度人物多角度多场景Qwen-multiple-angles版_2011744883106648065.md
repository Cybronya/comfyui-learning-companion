---
key: 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2011744883106648065.json
name: ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2011744883106648065
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2011744883106648065.json
hash: 17df9a315ed8b8ee
coverage: 0.69697
learned_at: 2026-10-15 22:25:33
nodes: [SetNode, SetNode, SetNode, easy promptLine, GetNode, GetNode, ModelSamplingAuraFlow, CFGNorm, PlaySound|pysssss, PlaySound|pysssss, INTConstant, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, GetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, JjkText, SaveImage, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, UNETLoader, KSampler, VAEDecode, LayerUtility: PurgeVRAM, SetNode, PlaySound|pysssss, JjkText, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 984586176472452, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2011744883106648065.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2011744883106648065.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
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
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `JjkText`
- `SaveImage`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `PlaySound|pysssss`
- `JjkText`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `984586176472452`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（23/33）

**有卡**：`easy promptLine`、`ModelSamplingAuraFlow`、`CFGNorm`、`PlaySound|pysssss`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`SaveImage`、`FluxKontextMultiReferenceLatentMethod`、`UNETLoader`、`KSampler`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

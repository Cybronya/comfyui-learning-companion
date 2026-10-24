---
key: 图片生成/图生图/最强图片反推提示词工具 JoyCaption Beta One与Joy Caption2 对比_1944664271521239042.json
name: 最强图片反推提示词工具 JoyCaption Beta One与Joy Caption2 对比_1944664271521239042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强图片反推提示词工具 JoyCaption Beta One与Joy Caption2 对比_1944664271521239042.json
hash: 598b07ea9b927083
coverage: 0.775
learned_at: 2026-10-23 13:06:09
nodes: [Fast Groups Muter (rgthree), KSampler, Text List to Text, BatchCount+, UnetLoaderGGUF, VAELoader, LoraLoaderModelOnly, DualCLIPLoaderGGUF, SetNode, CLIPTextEncodeFlux, MathExpression|pysssss, easy rangeInt, VAEDecode, EmptyLatentImage, CLIPTextEncode, ImageConcanate, Joy_caption_two_load, GetNode, GetNode, ShowText|pysssss, ShowText|pysssss, JJC_JoyCaption, easy cleanGpuUsed, easy promptList, TextSplitByDelimiter, GetNode, easy cleanGpuUsed, AddLabel, ShowText|pysssss, TextSplitByDelimiter, TextSplitByDelimiter, DeepTranslatorTextNode, DeepTranslatorTextNode, ShowText|pysssss, AddLabel, ttN concat, ttN concat, LoadAndResizeImage, Joy_caption_two, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 340829639198452, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/最强图片反推提示词工具 JoyCaption Beta One与Joy Caption2 对比_1944664271521239042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强图片反推提示词工具 JoyCaption Beta One与Joy Caption2 对比_1944664271521239042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `Text List to Text`
- `BatchCount+`
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoaderGGUF`
- `SetNode`
- `CLIPTextEncodeFlux` ★核心
- `MathExpression|pysssss`
- `easy rangeInt`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `Joy_caption_two_load`
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `JJC_JoyCaption`
- `easy cleanGpuUsed`
- `easy promptList`
- `TextSplitByDelimiter`
- `GetNode`
- `easy cleanGpuUsed`
- `AddLabel`
- `ShowText|pysssss`
- `TextSplitByDelimiter`
- `TextSplitByDelimiter`
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `ShowText|pysssss`
- `AddLabel`
- `ttN concat`
- `ttN concat`
- `LoadAndResizeImage`
- `Joy_caption_two`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `340829639198452`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（31/40）

**有卡**：`KSampler`、`Text List to Text`、`BatchCount+`、`UnetLoaderGGUF`、`VAELoader`、`LoraLoaderModelOnly`、`DualCLIPLoaderGGUF`、`CLIPTextEncodeFlux`、`MathExpression|pysssss`、`easy rangeInt`、`VAEDecode`、`EmptyLatentImage`、`CLIPTextEncode`、`ImageConcanate`、`Joy_caption_two_load`、`JJC_JoyCaption`、`easy cleanGpuUsed`、`easy promptList`、`TextSplitByDelimiter`、`AddLabel`、`DeepTranslatorTextNode`、`ttN concat`、`LoadAndResizeImage`、`Joy_caption_two`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、CLIPTextEncodeFlux、DualCLIPLoaderGGUF

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/图生图/【推荐】动漫转写实真人（Z-image重绘CFG1.6）_2008549814203588610.json
name: 【推荐】动漫转写实真人（Z-image重绘CFG1.6）_2008549814203588610
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【推荐】动漫转写实真人（Z-image重绘CFG1.6）_2008549814203588610.json
hash: 709b3fb12231b665
coverage: 0.74
learned_at: 2026-10-23 11:50:10
nodes: [GetNode, MarkdownNote, GetNode, GetNode, SetNode, SetNode, TextEncodeQwenImageEdit, GetNode, GetNode, SetNode, VAEEncode, CFGNorm, ModelSamplingAuraFlow, CLIPLoader, VAELoader, ImageScaleToTotalPixels, SetNode, JWStringConcat, CR Prompt Text, CLIPLoader, easy showAnything, CR Prompt Text, easy int, KSampler, VAELoader, easy cleanGpuUsed, UNETLoader, Note, CLIPTextEncode, LazyCache, BasicGuider, LoadImage, Fast Groups Muter (rgthree), SaveImage, Qwen3_VQA, 图像缩放V2_孤海, SaveImage, VAEDecode, MemoryCleaner, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, VAEEncode, VAEDecode, SplitSigmasDenoise, RandomNoise, KSamplerSelect, UNETLoader, SamplerCustomAdvanced, FlowMatchEulerDiscreteScheduler (Custom), LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2m", "scheduler": "sgm_uniform", "seed": 36804909857204, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【推荐】动漫转写实真人（Z-image重绘CFG1.6）_2008549814203588610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【推荐】动漫转写实真人（Z-image重绘CFG1.6）_2008549814203588610.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEEncode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `SetNode`
- `JWStringConcat`
- `CR Prompt Text`
- `CLIPLoader`
- `easy showAnything`
- `CR Prompt Text`
- `easy int`
- `KSampler` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `LazyCache`
- `BasicGuider`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `Qwen3_VQA`
- `图像缩放V2_孤海`
- `SaveImage`
- `VAEDecode` ★核心
- `MemoryCleaner`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SplitSigmasDenoise`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `36804909857204`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **74%**（37/50）

**有卡**：`TextEncodeQwenImageEdit`、`VAEEncode`、`CFGNorm`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`JWStringConcat`、`CR Prompt Text`、`easy int`、`KSampler`、`easy cleanGpuUsed`、`UNETLoader`、`CLIPTextEncode`、`LazyCache`、`BasicGuider`、`LoadImage`、`SaveImage`、`Qwen3_VQA`、`图像缩放V2_孤海`、`VAEDecode`、`MemoryCleaner`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`SplitSigmasDenoise`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`FlowMatchEulerDiscreteScheduler (Custom)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

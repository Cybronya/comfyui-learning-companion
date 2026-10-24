---
key: 图片生成/图生图/Qwen-史上最强动漫转写实真人（Z-image重绘CFG1.6）_2002567462472302594.json
name: Qwen-史上最强动漫转写实真人（Z-image重绘CFG1.6）_2002567462472302594
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-史上最强动漫转写实真人（Z-image重绘CFG1.6）_2002567462472302594.json
hash: c6aed007b4aad9ce
coverage: 0.74
learned_at: 2026-10-23 11:18:57
nodes: [GetNode, MarkdownNote, GetNode, GetNode, SetNode, SetNode, TextEncodeQwenImageEdit, GetNode, GetNode, SetNode, VAEEncode, CFGNorm, ModelSamplingAuraFlow, CLIPLoader, VAELoader, ImageScaleToTotalPixels, SetNode, JWStringConcat, CR Prompt Text, CLIPLoader, easy showAnything, CR Prompt Text, easy int, KSampler, VAELoader, easy cleanGpuUsed, UNETLoader, Note, CLIPTextEncode, LazyCache, BasicGuider, LoadImage, Fast Groups Muter (rgthree), SaveImage, Qwen3_VQA, 图像缩放V2_孤海, SaveImage, VAEDecode, MemoryCleaner, LoadImage, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, VAEEncode, VAEDecode, SplitSigmasDenoise, RandomNoise, KSamplerSelect, UNETLoader, SamplerCustomAdvanced, FlowMatchEulerDiscreteScheduler (Custom)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2m", "scheduler": "sgm_uniform", "seed": 696268978743208, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-史上最强动漫转写实真人（Z-image重绘CFG1.6）_2002567462472302594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-史上最强动漫转写实真人（Z-image重绘CFG1.6）_2002567462472302594.json`

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
- `LoadImage`
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

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `696268978743208`
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

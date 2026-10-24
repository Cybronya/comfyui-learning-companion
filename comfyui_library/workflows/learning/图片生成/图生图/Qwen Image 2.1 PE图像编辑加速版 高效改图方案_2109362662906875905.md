---
key: 图片生成/图生图/Qwen Image 2.1 PE图像编辑加速版 高效改图方案_2109362662906875905.json
name: Qwen Image 2.1 PE图像编辑加速版 高效改图方案_2109362662906875905
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE图像编辑加速版 高效改图方案_2109362662906875905.json
hash: 726559591a19a266
coverage: 0.839286
learned_at: 2026-10-23 11:12:35
nodes: [CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, QwenImage21Cache, KSamplerSelect, CFGGuider, RandomNoise, SaveImageAdvanced, SamplerCustomAdvanced, VAEDecode, ImageCompare, ManualSigmas, KSampler, ComfySwitchNode, TextEncodeQwenImage21, PrimitiveBoolean, EmptyLatentImage, LoadImage, RH_QwenImagePromptEnhancer, easy showAnything, ComfySwitchNode, ResolutionSelector, PrimitiveBoolean, PreviewImage, SaveImage, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 PE图像编辑加速版 高效改图方案_2109362662906875905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE图像编辑加速版 高效改图方案_2109362662906875905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `SaveImageAdvanced`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageCompare`
- `ManualSigmas`
- `KSampler` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `PrimitiveBoolean`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `RH_QwenImagePromptEnhancer`
- `easy showAnything`
- `ComfySwitchNode`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PreviewImage`
- `SaveImage`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（47/56）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SaveImageAdvanced`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageCompare`、`ManualSigmas`、`KSampler`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`EmptyLatentImage`、`LoadImage`、`RH_QwenImagePromptEnhancer`、`ResolutionSelector`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

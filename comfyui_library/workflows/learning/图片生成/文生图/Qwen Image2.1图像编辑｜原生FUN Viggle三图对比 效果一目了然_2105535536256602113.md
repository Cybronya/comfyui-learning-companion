---
key: 图片生成/文生图/Qwen Image2.1图像编辑｜原生FUN Viggle三图对比 效果一目了然_2105535536256602113.json
name: Qwen Image2.1图像编辑｜原生FUN Viggle三图对比 效果一目了然_2105535536256602113
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1图像编辑｜原生FUN Viggle三图对比 效果一目了然_2105535536256602113.json
hash: b634e4e6824690ef
coverage: 0.942029
learned_at: 2026-10-06 22:57:50
nodes: [INTConstant, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, LoraLoaderModelOnly, BasicGuider, RandomNoise, KSamplerSelect, CustomSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, VAEDecode, VAEDecode, SaveImage, ImageConcatMulti, SaveImage, LoadImage, ImageResizeKJv2, SaveImage, T8QwenImage21FunAccPDD4Step, INTConstant, INTConstant, StringConstantMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image2.1图像编辑｜原生FUN Viggle三图对比 效果一目了然_2105535536256602113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1图像编辑｜原生FUN Viggle三图对比 效果一目了然_2105535536256602113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CustomSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `SaveImage`
- `LoadImage`
- `ImageResizeKJv2`
- `SaveImage`
- `T8QwenImage21FunAccPDD4Step`
- `INTConstant`
- `INTConstant`
- `StringConstantMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **94%**（65/69）

**有卡**：`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`LoraLoaderModelOnly`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`CustomSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ImageConcatMulti`、`LoadImage`、`ImageResizeKJv2`、`T8QwenImage21FunAccPDD4Step`、`StringConstantMultiline`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/一键运行qwen image 2.1 turbo in 最新文生图 高质量画面直出_2109773419607838722.json
name: 一键运行qwen image 2.1 turbo in 最新文生图 高质量画面直出_2109773419607838722
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一键运行qwen image 2.1 turbo in 最新文生图 高质量画面直出_2109773419607838722.json
hash: 9774ca67d1111282
coverage: 0.710526
learned_at: 2026-10-21 02:58:16
nodes: [LayerFilter: HDREffects, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, ImageCaptionNode, CR Text Input Switch (4 way), SetNode, VAELoader, CLIPLoader, SetNode, ShowText|pysssss, Fast Groups Bypasser (rgthree), EmptySD3LatentImage, Text Multiline, TextGenerate, easy positive, TextEncodeQwenImage21, VOSR2Upscale, VOSR2ModelLoader, Image Comparer (rgthree), SaveImage, GetNode, ResolutionSelector, EmptySD3LatentImage, CR Latent Input Switch, LoadImage, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, VAEDecode, GetNode, PreviewTextNode, LoraLoaderModelOnly, CLIPLoader, BasicGuider, UNETLoader, PreviewImage, SplitImageWithAlpha, easy imageChooser, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/一键运行qwen image 2.1 turbo in 最新文生图 高质量画面直出_2109773419607838722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一键运行qwen image 2.1 turbo in 最新文生图 高质量画面直出_2109773419607838722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `LayerFilter: HDREffects`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageCaptionNode`
- `CR Text Input Switch (4 way)`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `EmptySD3LatentImage`
- `Text Multiline`
- `TextGenerate`
- `easy positive`
- `TextEncodeQwenImage21`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `GetNode`
- `ResolutionSelector`
- `EmptySD3LatentImage`
- `CR Latent Input Switch`
- `LoadImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `VAEDecode` ★核心
- `GetNode`
- `PreviewTextNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `BasicGuider`
- `UNETLoader` ★核心
- `PreviewImage`
- `SplitImageWithAlpha`
- `easy imageChooser`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **71%**（54/76）

**有卡**：`LayerFilter: HDREffects`、`ImageCaptionNode`、`CR Text Input Switch (4 way)`、`VAELoader`、`CLIPLoader`、`EmptySD3LatentImage`、`Text Multiline`、`TextGenerate`、`easy positive`、`TextEncodeQwenImage21`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SaveImage`、`ResolutionSelector`、`CR Latent Input Switch`、`LoadImage`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ManualSigmas`、`VAEDecode`、`PreviewTextNode`、`LoraLoaderModelOnly`、`BasicGuider`、`UNETLoader`、`SplitImageWithAlpha`、`easy imageChooser`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

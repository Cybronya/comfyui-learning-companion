---
key: 图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json
name: Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json
hash: cd56a9a915f732cf
coverage: 0.849057
learned_at: 2026-10-21 00:43:37
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, CLIPLoader, LoadImage, StringConstantMultiline, KSampler, easy seed, UNETLoader, StringReplace, StringConstantMultiline, TextGenerate, BatchImagesNode, VAEDecode, StringFunction|pysssss, PreviewAny, PreviewAny, EmptyLatentImage, Image Comparer (rgthree), ResolutionSelector, ComfySwitchNode, LoadImage, SaveImage, TextEncodeQwenImage21, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `CLIPLoader`
- `LoadImage`
- `StringConstantMultiline`
- `KSampler` ★核心
- `easy seed`
- `UNETLoader` ★核心
- `StringReplace`
- `StringConstantMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `VAEDecode` ★核心
- `StringFunction|pysssss`
- `PreviewAny`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `ComfySwitchNode`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
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

覆盖率 **85%**（45/53）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`LoadImage`、`StringConstantMultiline`、`KSampler`、`easy seed`、`UNETLoader`、`StringReplace`、`TextGenerate`、`BatchImagesNode`、`VAEDecode`、`StringFunction|pysssss`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

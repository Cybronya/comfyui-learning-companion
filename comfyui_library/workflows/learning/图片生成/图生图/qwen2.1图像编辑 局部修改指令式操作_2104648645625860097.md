---
key: 图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json
name: qwen2.1图像编辑 局部修改指令式操作_2104648645625860097
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json
hash: 2aa92cefe6ad923b
coverage: 0.868852
learned_at: 2026-10-21 00:46:11
nodes: [QwenImage21Cache, easy seed, VAEDecode, BatchImagesNode, StringConstantMultiline, StringReplace, TextEncodeQwenImage21, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, SaveImage, CLIPLoader, KSampler, TextGenerate, StringFunction|pysssss, PreviewAny, PreviewAny, StringConstantMultiline, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `QwenImage21Cache`
- `easy seed`
- `VAEDecode` ★核心
- `BatchImagesNode`
- `StringConstantMultiline`
- `StringReplace`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `SaveImage`
- `CLIPLoader`
- `KSampler` ★核心
- `TextGenerate`
- `StringFunction|pysssss`
- `PreviewAny`
- `PreviewAny`
- `StringConstantMultiline`
- `LoadImage`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（53/61）

**有卡**：`QwenImage21Cache`、`easy seed`、`VAEDecode`、`BatchImagesNode`、`StringConstantMultiline`、`StringReplace`、`TextEncodeQwenImage21`、`ResolutionSelector`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`FluxKontextImageScale`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`TextGenerate`、`StringFunction|pysssss`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

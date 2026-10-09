---
key: 图片生成/图生图/Qwen Image 2.1扩图局部重绘图生图处理工具_2102522537514196994.json
name: Qwen Image 2.1扩图局部重绘图生图处理工具_2102522537514196994.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1扩图局部重绘图生图处理工具_2102522537514196994.json
hash: 284891ccd61143a9
coverage: 0.773585
learned_at: 2026-10-09 22:19:28
nodes: [ResolutionSelector, KSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, QwenImage21Cache, TextEncodeQwenImage21, ResizeImageMaskNode, EmptyLatentImage, ImagePadForOutpaint, DrawMaskOnImage, PreviewImage, GetImageSize, SaveImageAdvanced, VAEDecode, SaveImage, CLIPLoader, VAELoader, UNETLoader, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1扩图局部重绘图生图处理工具_2102522537514196994.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102522537514196994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `ResolutionSelector`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ResizeImageMaskNode`
- `EmptyLatentImage` ★核心
- `ImagePadForOutpaint`
- `DrawMaskOnImage`
- `PreviewImage`
- `GetImageSize`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
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

覆盖率 **77%**（41/53）

**有卡**：`ResolutionSelector`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ResizeImageMaskNode`、`EmptyLatentImage`、`ImagePadForOutpaint`、`DrawMaskOnImage`、`GetImageSize`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

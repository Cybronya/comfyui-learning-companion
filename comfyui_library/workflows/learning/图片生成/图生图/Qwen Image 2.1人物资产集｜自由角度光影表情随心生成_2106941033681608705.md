---
key: 图片生成/图生图/Qwen Image 2.1人物资产集｜自由角度光影表情随心生成_2106941033681608705.json
name: Qwen Image 2.1人物资产集｜自由角度光影表情随心生成_2106941033681608705
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物资产集｜自由角度光影表情随心生成_2106941033681608705.json
hash: 8cdbd5aa54ec56f9
coverage: 0.842857
learned_at: 2026-10-21 00:42:20
nodes: [UNETLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, ResolutionSelector, KSampler, TextEncodeQwenImage21, LoadImage, Fast Groups Bypasser (rgthree), Text Load Line From File, StringConcatenate, StringConcatenate, StringConcatenate, PreviewImage, easy showAnything, easy showAnything, easy showAnything, ImpactWildcardProcessor, Text Multiline, PrimitiveInt, ImageResizeKJv2, TTResolutionSelector, CLIPLoader, SaveImage, SaveImageKJ, VAEDecode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1人物资产集｜自由角度光影表情随心生成_2106941033681608705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物资产集｜自由角度光影表情随心生成_2106941033681608705.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `ResolutionSelector`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Text Load Line From File`
- `StringConcatenate`
- `StringConcatenate`
- `StringConcatenate`
- `PreviewImage`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ImpactWildcardProcessor`
- `Text Multiline`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `CLIPLoader`
- `SaveImage`
- `SaveImageKJ`
- `VAEDecode` ★核心
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

覆盖率 **84%**（59/70）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`ResolutionSelector`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`Text Load Line From File`、`StringConcatenate`、`ImpactWildcardProcessor`、`Text Multiline`、`ImageResizeKJv2`、`TTResolutionSelector`、`CLIPLoader`、`SaveImage`、`SaveImageKJ`、`VAEDecode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

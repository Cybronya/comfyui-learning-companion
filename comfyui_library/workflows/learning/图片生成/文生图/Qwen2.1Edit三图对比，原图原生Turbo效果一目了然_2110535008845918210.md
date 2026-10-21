---
key: 图片生成/文生图/Qwen2.1Edit三图对比，原图原生Turbo效果一目了然_2110535008845918210.json
name: Qwen2.1Edit三图对比，原图原生Turbo效果一目了然_2110535008845918210
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1Edit三图对比，原图原生Turbo效果一目了然_2110535008845918210.json
hash: 0a139830b1364bbb
coverage: 0.892857
learned_at: 2026-10-21 02:54:42
nodes: [UNETLoader, CLIPLoader, VAELoader, INTConstant, INTConstant, StringConstantMultiline, ImageResizeKJv2, TextEncodeQwenImage21, UNETLoader, KSampler, VAEDecode, SaveImage, AddLabel, ManualSigmas, KSamplerSelect, VAEDecode, SaveImage, AddLabel, AddLabel, ImageConcatMulti, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), INTConstant, SamplerCustom, LoadImage, LayerUtility: ImageRemoveAlpha, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1Edit三图对比，原图原生Turbo效果一目了然_2110535008845918210.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1Edit三图对比，原图原生Turbo效果一目了然_2110535008845918210.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `StringConstantMultiline`
- `ImageResizeKJv2`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SamplerCustom` ★核心
- `LoadImage`
- `LayerUtility: ImageRemoveAlpha`
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

覆盖率 **89%**（50/56）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`INTConstant`、`StringConstantMultiline`、`ImageResizeKJv2`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`AddLabel`、`ManualSigmas`、`KSamplerSelect`、`ImageConcatMulti`、`SamplerCustom`、`LoadImage`、`LayerUtility: ImageRemoveAlpha`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

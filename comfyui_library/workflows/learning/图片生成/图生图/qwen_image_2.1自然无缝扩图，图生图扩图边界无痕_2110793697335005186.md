---
key: 图片生成/图生图/qwen_image_2.1自然无缝扩图，图生图扩图边界无痕_2110793697335005186.json
name: qwen_image_2.1自然无缝扩图，图生图扩图边界无痕_2110793697335005186
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1自然无缝扩图，图生图扩图边界无痕_2110793697335005186.json
hash: 7bac34ba5f568b5b
coverage: 0.914894
learned_at: 2026-10-23 11:43:55
nodes: [ImpactInt, ConstrainImage|pysssss, LoadImage, SamplerCustom, ImpactInt, VAEDecode, ImpactInt, VAELoader, CLIPLoader, LayerUtility: ExtendCanvasV2, TextEncodeQwenImage21, UNETLoader, VAEEncode, KSamplerSelect, ManualSigmas, ImpactInt, ImpactInt, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_2.1自然无缝扩图，图生图扩图边界无痕_2110793697335005186.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1自然无缝扩图，图生图扩图边界无痕_2110793697335005186.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `ImpactInt`
- `ConstrainImage|pysssss`
- `LoadImage`
- `SamplerCustom` ★核心
- `ImpactInt`
- `VAEDecode` ★核心
- `ImpactInt`
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: ExtendCanvasV2`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ImpactInt`
- `ImpactInt`
- `SaveImage`
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

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **91%**（43/47）

**有卡**：`ImpactInt`、`ConstrainImage|pysssss`、`LoadImage`、`SamplerCustom`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`LayerUtility: ExtendCanvasV2`、`TextEncodeQwenImage21`、`UNETLoader`、`VAEEncode`、`KSamplerSelect`、`ManualSigmas`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 图片生成/文生图/千问Qwen2.1图片编辑神器｜文生图图生图双模式v260927新版本_2106191621074276353.json
name: 千问Qwen2.1图片编辑神器｜文生图图生图双模式v260927新版本_2106191621074276353
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问Qwen2.1图片编辑神器｜文生图图生图双模式v260927新版本_2106191621074276353.json
hash: 104bb477caa01e46
coverage: 0.880597
learned_at: 2026-10-07 02:37:23
nodes: [QwenPERewriteT8, ShowAnything|Mie, EmptyLatentImage, CLIPLoader, EnhancedLoadDiffusionModel, VAELoader_Any, TextEncodeQwenImage21, KSamplerCacheable, QwenImage21Cache, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, FastGroupsBypassSwitch, ResolutionSelector, JjkText, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [ShowAnything|Mie]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问Qwen2.1图片编辑神器｜文生图图生图双模式v260927新版本_2106191621074276353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问Qwen2.1图片编辑神器｜文生图图生图双模式v260927新版本_2106191621074276353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（67 个）：
- `QwenPERewriteT8`
- `ShowAnything|Mie`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `EnhancedLoadDiffusionModel`
- `VAELoader_Any`
- `TextEncodeQwenImage21`
- `KSamplerCacheable` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `FastGroupsBypassSwitch`
- `ResolutionSelector`
- `JjkText`
- `VAEDecode` ★核心
- `SaveImage`
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

覆盖率 **88%**（59/67）

**有卡**：`QwenPERewriteT8`、`EmptyLatentImage`、`CLIPLoader`、`EnhancedLoadDiffusionModel`、`VAELoader_Any`、`TextEncodeQwenImage21`、`KSamplerCacheable`、`QwenImage21Cache`、`LoadImage`、`FastGroupsBypassSwitch`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（1）：`ShowAnything|Mie`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

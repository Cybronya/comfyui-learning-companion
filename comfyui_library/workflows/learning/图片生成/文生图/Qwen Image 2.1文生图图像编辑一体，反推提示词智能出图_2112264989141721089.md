---
key: 图片生成/文生图/Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089.json
name: Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089.json
hash: c7739bbd2b8cfa42
coverage: 0.769231
learned_at: 2026-10-21 02:54:13
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, Reroute, LoadImage, LoadImage, GoohaiRatioAndResolution, QwenImage21SageAttentionT8, GetNode, KSampler, Image Comparer (rgthree), DF_Text_Box, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, LoadImageGoohai, VAELoader, GoohaiRouteBlocker, UNETLoader, easy ifElse, GoohaiAnyExists, LoraLoaderModelOnly, GoohaiRouteBlocker, TextEncodeQwenImage21GH, QwenImagePromptOptimizer, GoohaiDisplayAny, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图像编辑一体，反推提示词智能出图_2112264989141721089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `LoadImage`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `GoohaiRatioAndResolution`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `LoadImageGoohai`
- `VAELoader`
- `GoohaiRouteBlocker`
- `UNETLoader` ★核心
- `easy ifElse`
- `GoohaiAnyExists`
- `LoraLoaderModelOnly` ★核心
- `GoohaiRouteBlocker`
- `TextEncodeQwenImage21GH`
- `QwenImagePromptOptimizer`
- `GoohaiDisplayAny`
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

覆盖率 **77%**（50/65）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`GoohaiRatioAndResolution`、`QwenImage21SageAttentionT8`、`KSampler`、`DF_Text_Box`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`LoadImageGoohai`、`VAELoader`、`GoohaiRouteBlocker`、`UNETLoader`、`GoohaiAnyExists`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21GH`、`QwenImagePromptOptimizer`、`GoohaiDisplayAny`、`SaveImage`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

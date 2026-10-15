---
key: 图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json
name: 文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json
hash: 483e00f7963b21b7
coverage: 0.884058
learned_at: 2026-10-10 20:59:48
nodes: [CLIPLoader, VAELoader, QwenImage21SpectrumT8, TextEncodeQwenImage21GH, KSampler, VAEDecode, RestoreQwenImage21GH, SaveImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, GetNode, Image Comparer (rgthree), GoohaiRouteBlocker, GoohaiRatioAndResolution, ShowText|pysssss, QwenImagePromptOptimizer, DF_Text_Box, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, GoohaiRouteBlocker, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图图像编辑一体化｜Qwen Image 2.1 一套工作流全搞定_2105558671576100866.json`

## 结构

**节点**（69 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21SpectrumT8`
- `TextEncodeQwenImage21GH`
- `KSampler`
- `VAEDecode`
- `RestoreQwenImage21GH`
- `SaveImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader`
- `GetNode`
- `Image Comparer (rgthree)`
- `GoohaiRouteBlocker`
- `GoohaiRatioAndResolution`
- `ShowText|pysssss`
- `QwenImagePromptOptimizer`
- `DF_Text_Box`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `GoohaiRouteBlocker`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **88%**（61/69）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21SpectrumT8`、`TextEncodeQwenImage21GH`、`KSampler`、`VAEDecode`、`RestoreQwenImage21GH`、`SaveImage`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`GetNode`、`Image Comparer (rgthree)`、`GoohaiRouteBlocker`、`GoohaiRatioAndResolution`、`ShowText|pysssss`、`QwenImagePromptOptimizer`、`DF_Text_Box`、`LoadImage`、`SetNode`、`孤海注释`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`JjkText`、`LoraLoaderModelOnly`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

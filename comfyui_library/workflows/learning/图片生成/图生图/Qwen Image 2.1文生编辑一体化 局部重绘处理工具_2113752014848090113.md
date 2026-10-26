---
key: 图片生成/图生图/Qwen Image 2.1文生编辑一体化 局部重绘处理工具_2113752014848090113.json
name: Qwen Image 2.1文生编辑一体化 局部重绘处理工具_2113752014848090113
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生编辑一体化 局部重绘处理工具_2113752014848090113.json
hash: 31e2307eb21bf89a
coverage: 0.769231
learned_at: 2026-10-26 22:03:05
nodes: [LoadImage, LoadImage, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, LoadImage, LoadImage, QwenImage21SageAttentionT8, GetNode, KSampler, Image Comparer (rgthree), RestoreQwenImage21GH, VAELoader, GoohaiRouteBlocker, UNETLoader, easy ifElse, GoohaiAnyExists, GoohaiRouteBlocker, TextEncodeQwenImage21GH, QwenImagePromptOptimizer, GoohaiDisplayAny, SaveImage, LoadImageGoohai, DF_Text_Box, Reroute, Reroute, LoraLoaderModelOnly, GoohaiRatioAndResolution, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1文生编辑一体化 局部重绘处理工具_2113752014848090113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生编辑一体化 局部重绘处理工具_2113752014848090113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `RestoreQwenImage21GH`
- `VAELoader`
- `GoohaiRouteBlocker`
- `UNETLoader` ★核心
- `easy ifElse`
- `GoohaiAnyExists`
- `GoohaiRouteBlocker`
- `TextEncodeQwenImage21GH`
- `QwenImagePromptOptimizer`
- `GoohaiDisplayAny`
- `SaveImage`
- `LoadImageGoohai`
- `DF_Text_Box`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `GoohaiRatioAndResolution`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
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

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`QwenImage21SageAttentionT8`、`KSampler`、`RestoreQwenImage21GH`、`VAELoader`、`GoohaiRouteBlocker`、`UNETLoader`、`GoohaiAnyExists`、`TextEncodeQwenImage21GH`、`QwenImagePromptOptimizer`、`GoohaiDisplayAny`、`SaveImage`、`LoadImageGoohai`、`DF_Text_Box`、`LoraLoaderModelOnly`、`GoohaiRatioAndResolution`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

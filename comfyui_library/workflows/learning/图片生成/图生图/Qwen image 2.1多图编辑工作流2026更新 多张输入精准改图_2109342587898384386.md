---
key: 图片生成/图生图/Qwen image 2.1多图编辑工作流2026更新 多张输入精准改图_2109342587898384386.json
name: Qwen image 2.1多图编辑工作流2026更新 多张输入精准改图_2109342587898384386
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多图编辑工作流2026更新 多张输入精准改图_2109342587898384386.json
hash: ee4305e925217051
coverage: 0.857143
learned_at: 2026-10-23 11:14:08
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageMergeNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, PrimitiveStringMultiline, ShowText|pysssss, QwenImagePromptOptimizer, QwenImage21BlockCacheT8, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), KSampler, EmptyLatentImage, ComfySwitchNode, VAEDecode, PrimitiveBoolean, BatchImagesNode, SaveImage, ResolutionSelector, Fast Groups Muter (rgthree), SaveImage, UNETLoader, Fast Groups Bypasser (rgthree), VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1多图编辑工作流2026更新 多张输入精准改图_2109342587898384386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多图编辑工作流2026更新 多张输入精准改图_2109342587898384386.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageMergeNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `QwenImagePromptOptimizer`
- `QwenImage21BlockCacheT8`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `PrimitiveBoolean`
- `BatchImagesNode`
- `SaveImage`
- `ResolutionSelector`
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **86%**（60/70）

**有卡**：`LoadImage`、`ImageMergeNode`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`QwenImagePromptOptimizer`、`QwenImage21BlockCacheT8`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`PrimitiveBoolean`、`BatchImagesNode`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

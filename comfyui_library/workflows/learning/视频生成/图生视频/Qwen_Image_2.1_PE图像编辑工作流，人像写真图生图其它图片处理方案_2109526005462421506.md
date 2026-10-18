---
key: 视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json
name: Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json
hash: 6a3c320a7bd319d7
coverage: 0.910714
learned_at: 2026-10-18 00:23:46
nodes: [VAELoader, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, LoadImage, UNETLoader, easy showAnything, CLIPLoader, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21Cache, KSampler, easy cleanGpuUsed, SaveImage, VAEDecode, TextEncodeQwenImage21, ComfySwitchNode, ResolutionSelector, EmptyLatentImage, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `VAELoader`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `LoadImage`
- `UNETLoader` ★核心
- `easy showAnything`
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LoadImage`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **91%**（51/56）

**有卡**：`VAELoader`、`CR Prompt Text`、`LoadImage`、`QwenPERewriteT8`、`UNETLoader`、`CLIPLoader`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`QwenImage21Cache`、`KSampler`、`easy cleanGpuUsed`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

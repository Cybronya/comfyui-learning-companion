---
key: 图片生成/图生图/Qwen Image 2.1一键图片自动透明分层，精准抠图图层分离图生图工具_2103258930473422849.json
name: Qwen Image 2.1一键图片自动透明分层，精准抠图图层分离图生图工具_2103258930473422849
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1一键图片自动透明分层，精准抠图图层分离图生图工具_2103258930473422849.json
hash: 71448936e85f2874
coverage: 0.836735
learned_at: 2026-10-21 00:42:16
nodes: [easy forLoopEnd, SaveImage, CLIPLoader, VAELoader, TextEncodeQwenImage21, VAEDecode, easy forLoopEnd, KSampler, UNETLoader, PreviewAny, easy forLoopStart, Text Load Line From File, SaveImage, QwenImage21Cache, PreviewAny, PrimitiveStringMultiline, RHLLMChatNode, PreviewAny, LoadImage, CR Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1一键图片自动透明分层，精准抠图图层分离图生图工具_2103258930473422849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1一键图片自动透明分层，精准抠图图层分离图生图工具_2103258930473422849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `easy forLoopEnd`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `PreviewAny`
- `easy forLoopStart`
- `Text Load Line From File`
- `SaveImage`
- `QwenImage21Cache`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RHLLMChatNode`
- `PreviewAny`
- `LoadImage`
- `CR Text`
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

覆盖率 **84%**（41/49）

**有卡**：`easy forLoopEnd`、`SaveImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`VAEDecode`、`KSampler`、`UNETLoader`、`easy forLoopStart`、`Text Load Line From File`、`QwenImage21Cache`、`RHLLMChatNode`、`LoadImage`、`CR Text`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

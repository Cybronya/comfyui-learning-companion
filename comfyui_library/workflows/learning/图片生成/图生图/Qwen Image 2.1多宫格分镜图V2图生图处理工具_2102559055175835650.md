---
key: 图片生成/图生图/Qwen Image 2.1多宫格分镜图V2图生图处理工具_2102559055175835650.json
name: Qwen Image 2.1多宫格分镜图V2图生图处理工具_2102559055175835650.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多宫格分镜图V2图生图处理工具_2102559055175835650.json
hash: aa1c50119b7aa832
coverage: 0.866667
learned_at: 2026-10-09 22:19:29
nodes: [QwenImage21Cache, TextEncodeQwenImage21, ComfySwitchNode, KSampler, EmptyLatentImage, VAELoader, LoadImage, LoadImage, UNETLoader, CLIPLoader, UNETLoader, CLIPLoader, VAEDecode, ResolutionSelector, SaveImage, CLIPLoader, PrimitiveStringMultiline, RHLLMChatNode, ZNGB_ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextGenerateLTX2Prompt, StringConcatenate, easy showAnything, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1多宫格分镜图V2图生图处理工具_2102559055175835650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102559055175835650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `SaveImage`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `RHLLMChatNode`
- `ZNGB_ImageBatchMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `StringConcatenate`
- `easy showAnything`
- `PrimitiveStringMultiline`
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

覆盖率 **87%**（52/60）

**有卡**：`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`ResolutionSelector`、`SaveImage`、`RHLLMChatNode`、`ZNGB_ImageBatchMulti`、`TextGenerateLTX2Prompt`、`StringConcatenate`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

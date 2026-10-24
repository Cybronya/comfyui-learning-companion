---
key: 图片生成/图生图/Qwen image2.1人物写真套图，图生图批量出多角度写真_2112287252721262594.json
name: Qwen image2.1人物写真套图，图生图批量出多角度写真_2112287252721262594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1人物写真套图，图生图批量出多角度写真_2112287252721262594.json
hash: 90aa014e1c69c683
coverage: 0.84
learned_at: 2026-10-23 11:14:22
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, ProcessString, easy promptLine, LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, UNETLoader, RH_DLSS5Enhance, ComfySwitchNode, VAEDecode, PreviewImage, RHLLMChatNode, ResolutionSelector, LoadImage, Image Comparer (rgthree), SaveImage, VOSR2Upscale, VOSR2ModelLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1人物写真套图，图生图批量出多角度写真_2112287252721262594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1人物写真套图，图生图批量出多角度写真_2112287252721262594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ProcessString`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `RH_DLSS5Enhance`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `RHLLMChatNode`
- `ResolutionSelector`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
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

覆盖率 **84%**（42/50）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`ProcessString`、`easy promptLine`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`RH_DLSS5Enhance`、`VAEDecode`、`RHLLMChatNode`、`ResolutionSelector`、`LoadImage`、`SaveImage`、`VOSR2Upscale`、`VOSR2ModelLoader`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

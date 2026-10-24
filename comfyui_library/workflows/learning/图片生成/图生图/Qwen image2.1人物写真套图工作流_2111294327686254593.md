---
key: 图片生成/图生图/Qwen image2.1人物写真套图工作流_2111294327686254593.json
name: Qwen image2.1人物写真套图工作流_2111294327686254593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1人物写真套图工作流_2111294327686254593.json
hash: 93a48931d41d4215
coverage: 0.708333
learned_at: 2026-10-23 11:14:21
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, ProcessString, easy promptLine, LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, UNETLoader, RH_DLSS5Enhance, ComfySwitchNode, VAEDecode, PreviewImage, 孤海注释, MarkdownNote, RHLLMChatNode, MarkdownNote, ResolutionSelector, LoadImage, Image Comparer (rgthree), SaveImage, VOSR2Upscale, VOSR2ModelLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Qwen image2.1人物写真套图工作流_2111294327686254593.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1人物写真套图工作流_2111294327686254593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
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
- `孤海注释`
- `MarkdownNote`
- `RHLLMChatNode`
- `MarkdownNote`
- `ResolutionSelector`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VOSR2Upscale`
- `VOSR2ModelLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`ProcessString`、`easy promptLine`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`RH_DLSS5Enhance`、`VAEDecode`、`RHLLMChatNode`、`ResolutionSelector`、`LoadImage`、`SaveImage`、`VOSR2Upscale`、`VOSR2ModelLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

---
key: 图片生成/图生图/Qwen image2.1人像写真-自动分镜-多图-工作流_2116772222831513601.json
name: Qwen image2.1人像写真-自动分镜-多图-工作流_2116772222831513601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1人像写真-自动分镜-多图-工作流_2116772222831513601.json
hash: e8ad1be7cd09f025
coverage: 0.826087
learned_at: 2026-11-02 19:12:48
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, ProcessString, easy promptLine, LoraLoaderModelOnly, CLIPLoader, VAELoader, Anything Everywhere3, UNETLoader, ComfySwitchNode, VAEDecode, RHLLMChatNode, MarkdownNote, LoadImage, JjkText, ImageScaleBy, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, easy int, GoohaiRatioAndResolution]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Qwen image2.1人像写真-自动分镜-多图-工作流_2116772222831513601.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1人像写真-自动分镜-多图-工作流_2116772222831513601.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
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
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `RHLLMChatNode`
- `MarkdownNote`
- `LoadImage`
- `JjkText`
- `ImageScaleBy`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `easy int`
- `GoohaiRatioAndResolution`

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

覆盖率 **83%**（19/23）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`ProcessString`、`easy promptLine`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`RHLLMChatNode`、`LoadImage`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`easy int`、`GoohaiRatioAndResolution`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

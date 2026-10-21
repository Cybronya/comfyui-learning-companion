---
key: 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json
name: 多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json
hash: f71c883863bd455e
coverage: 0.909091
learned_at: 2026-10-21 00:51:54
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, VAELoader, QwenImage21Cache, KSampler, easy imageConcat, easy imageConcat, easy imageConcat, ResolutionSelector, SaveImage, SaveImage, LoadImage, JjkText, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 680076780953518, "steps": 50, "width": 1024}
---

# 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy imageConcat`
- `easy imageConcat`
- `easy imageConcat`
- `ResolutionSelector`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `JjkText`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `680076780953518`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`easy imageConcat`、`ResolutionSelector`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

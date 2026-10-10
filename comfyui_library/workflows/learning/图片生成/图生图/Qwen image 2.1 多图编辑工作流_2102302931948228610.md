---
key: 图片生成/图生图/Qwen image 2.1 多图编辑工作流_2102302931948228610.json
name: Qwen image 2.1 多图编辑工作流_2102302931948228610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑工作流_2102302931948228610.json
hash: f971d0d8a40580cc
coverage: 0.8
learned_at: 2026-10-10 20:48:08
nodes: [VAEDecode, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, VAELoader, UNETLoader, LoadImage, PrimitiveBoolean, CLIPLoader, BatchImagesNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextGenerateLTX2Prompt, LoadImage, SaveImage, ResolutionSelector, Fast Groups Muter (rgthree), ImageMergeNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, TextEncodeQwenImage21, LoraLoaderModelOnly, MarkdownNote, Note, Fast Groups Muter (rgthree), LoadImage, SaveImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 270644153823002, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 多图编辑工作流_2102302931948228610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑工作流_2102302931948228610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveBoolean`
- `CLIPLoader`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `SaveImage`
- `ResolutionSelector`
- `Fast Groups Muter (rgthree)`
- `ImageMergeNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `Note`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `270644153823002`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（36/45）

**有卡**：`VAEDecode`、`CLIPLoader`、`LoadImage`、`VAELoader`、`UNETLoader`、`PrimitiveBoolean`、`BatchImagesNode`、`TextGenerateLTX2Prompt`、`SaveImage`、`ResolutionSelector`、`ImageMergeNode`、`KSampler`、`QwenImage21Cache`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

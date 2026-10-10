---
key: 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json
name: Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json
hash: d615f943b9ffcbb7
coverage: 0.793103
learned_at: 2026-10-10 20:48:08
nodes: [UNETLoader, CLIPLoader, easy showAnything, EmptyLatentImage, ComfySwitchNode, 孤海注释, SaveImage, VAEDecode, TextEncodeQwenImage21, KSampler, CLIPLoader, TextGenerateLTX2Prompt, VAELoader, PrimitiveBoolean, ResolutionSelector, BatchImagesNode, 孤海注释, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1006117707807533, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `孤海注释`
- `SaveImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `VAELoader`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `BatchImagesNode`
- `孤海注释`
- `PrimitiveStringMultiline`
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
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1006117707807533`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`KSampler`、`TextGenerateLTX2Prompt`、`VAELoader`、`PrimitiveBoolean`、`ResolutionSelector`、`BatchImagesNode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

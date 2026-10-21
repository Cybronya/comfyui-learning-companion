---
key: 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json
name: Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json
hash: 7f18d43415c670a2
coverage: 0.793103
learned_at: 2026-10-21 00:42:55
nodes: [UNETLoader, CLIPLoader, easy showAnything, LoadImage, EmptyLatentImage, ComfySwitchNode, 孤海注释, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAEDecode, TextEncodeQwenImage21, KSampler, CLIPLoader, TextGenerateLTX2Prompt, VAELoader, PrimitiveBoolean, ResolutionSelector, BatchImagesNode, 孤海注释, 孤海注释, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 226540578544794, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy showAnything`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `孤海注释`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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
- `孤海注释`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `226540578544794`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoadImage`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`KSampler`、`TextGenerateLTX2Prompt`、`VAELoader`、`PrimitiveBoolean`、`ResolutionSelector`、`BatchImagesNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

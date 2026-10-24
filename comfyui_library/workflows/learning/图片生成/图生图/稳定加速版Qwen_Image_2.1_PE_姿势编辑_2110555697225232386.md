---
key: 图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json
name: 稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json
hash: 0ed292688ae57947
coverage: 0.833333
learned_at: 2026-10-23 13:20:11
nodes: [Note, CLIPLoader, VAELoader, Note, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, UNETLoader, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, Note, KSampler, VAEDecode, easy cleanGpuUsed, QwenPERewriteT8, CR Prompt Text, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/稳定加速版Qwen_Image_2.1_PE_姿势编辑_2110555697225232386.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `Note`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`LoadImage`、`QwenImage21Cache`、`UNETLoader`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`QwenPERewriteT8`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

---
key: 图片生成/图生图/pandy-Qwen2.1-JM3D全身公仔_2114275920147214337.json
name: pandy-Qwen2.1-JM3D全身公仔_2114275920147214337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/pandy-Qwen2.1-JM3D全身公仔_2114275920147214337.json
hash: bca5c086d6a5445d
coverage: 0.782609
learned_at: 2026-10-26 22:04:14
nodes: [VAEDecode, BatchImagesNode, LoadImage, EmptyLatentImage, ComfySwitchNode, PrimitiveStringMultiline, CLIPLoader, TextEncodeQwenImage21, easy showAnything, VAELoader, LoadImage, SaveImage, PrimitiveBoolean, TextGenerateLTX2Prompt, CLIPLoader, UNETLoader, SamplerCustom, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, ResolutionSelector, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/pandy-Qwen2.1-JM3D全身公仔_2114275920147214337.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/pandy-Qwen2.1-JM3D全身公仔_2114275920147214337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAEDecode` ★核心
- `BatchImagesNode`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `VAELoader`
- `LoadImage`
- `SaveImage`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`VAEDecode`、`BatchImagesNode`、`LoadImage`、`EmptyLatentImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`VAELoader`、`SaveImage`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`UNETLoader`、`SamplerCustom`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`ResolutionSelector`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

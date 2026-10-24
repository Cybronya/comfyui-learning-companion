---
key: 图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json
name: Qwen Image 2.1 turbo 光影迁移_2112413229950521345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json
hash: dfb30d8090f60b73
coverage: 0.882353
learned_at: 2026-10-23 11:12:40
nodes: [ResolutionSelector, EmptyLatentImage, ComfySwitchNode, CLIPLoader, VAELoader, SaveImage, SamplerCustom, KSamplerSelect, ManualSigmas, UNETLoader, PrimitiveBoolean, TextEncodeQwenImage21, LoraLoaderModelOnly, VAEDecode, LoadImage, LoadImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`SaveImage`、`SamplerCustom`、`KSamplerSelect`、`ManualSigmas`、`UNETLoader`、`PrimitiveBoolean`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`VAEDecode`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

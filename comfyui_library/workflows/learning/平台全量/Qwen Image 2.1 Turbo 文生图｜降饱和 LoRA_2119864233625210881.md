---
key: 平台全量/Qwen Image 2.1 Turbo 文生图｜降饱和 LoRA_2119864233625210881.json
name: Qwen Image 2.1 Turbo 文生图｜降饱和 LoRA_2119864233625210881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1 Turbo 文生图｜降饱和 LoRA_2119864233625210881.json
hash: cfdfd4161bbc0483
coverage: 0.789474
learned_at: 2026-11-14 00:49:53
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, CLIPLoader, VAELoader, easy showAnything, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, SaveImage, SaveImageAdvanced, KSamplerSelect, ManualSigmas, SamplerCustom, UNETLoader, LoraLoaderModelOnly, Note, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Qwen Image 2.1 Turbo 文生图｜降饱和 LoRA_2119864233625210881.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1 Turbo 文生图｜降饱和 LoRA_2119864233625210881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `ResolutionSelector`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `SaveImage`
- `SaveImageAdvanced`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustom` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `MarkdownNote`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`SaveImage`、`SaveImageAdvanced`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustom`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

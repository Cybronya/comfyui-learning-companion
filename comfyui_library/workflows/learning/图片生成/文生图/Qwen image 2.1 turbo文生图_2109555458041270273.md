---
key: 图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json
name: Qwen image 2.1 turbo文生图_2109555458041270273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json
hash: a23d34a7ff829e09
coverage: 0.875
learned_at: 2026-10-21 02:54:18
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, CLIPLoader, VAELoader, easy showAnything, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, SaveImage, SaveImageAdvanced, UNETLoader, KSamplerSelect, ManualSigmas, SamplerCustom]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
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
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustom` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`SaveImage`、`SaveImageAdvanced`、`UNETLoader`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustom`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader、KSamplerSelect

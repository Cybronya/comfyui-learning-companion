---
key: 图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json
name: Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json
hash: ac236a10993a88c0
coverage: 0.882353
learned_at: 2026-10-21 02:54:18
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, CLIPLoader, VAELoader, easy showAnything, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, SaveImage, SaveImageAdvanced, KSamplerSelect, ManualSigmas, SamplerCustom, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`SaveImage`、`SaveImageAdvanced`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustom`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

---
key: 图片生成/文生图/Krea2 Multi-Image Reference Editing_2073788017583673345.json
name: Krea2 Multi-Image Reference Editing_2073788017583673345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Multi-Image Reference Editing_2073788017583673345.json
hash: 17d8a8fe4e8a7c46
coverage: 0.783784
learned_at: 2026-10-20 00:01:17
nodes: [RandomNoise, PrimitiveStringMultiline, UNETLoader, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, EmptyLatentImage, Reroute, VAELoader, LoadImage, LoadImage, CLIPLoader, PrimitiveStringMultiline, ResolutionSelector, RandomNoise, UNETLoader, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecode, EmptyLatentImage, Reroute, VAELoader, PreviewImage, CLIPLoader, Krea2EditRebalance, ResolutionSelector, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, Krea2EditRebalance, LoadImage, PreviewImage, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Krea2 Multi-Image Reference Editing_2073788017583673345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Multi-Image Reference Editing_2073788017583673345.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `RandomNoise`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `Reroute`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `RandomNoise`
- `UNETLoader` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Reroute`
- `VAELoader`
- `PreviewImage`
- `CLIPLoader`
- `Krea2EditRebalance`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Krea2EditRebalance`
- `LoadImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（29/37）

**有卡**：`RandomNoise`、`UNETLoader`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`VAELoader`、`LoadImage`、`CLIPLoader`、`ResolutionSelector`、`VAEDecode`、`Krea2EditRebalance`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

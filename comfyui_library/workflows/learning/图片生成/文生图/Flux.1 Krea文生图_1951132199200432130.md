---
key: 图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json
name: Flux.1 Krea文生图_1951132199200432130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json
hash: bb8696c901bd76d5
coverage: 1
learned_at: 2026-10-07 22:59:00
nodes: [UNETLoader, DualCLIPLoader, FluxGuidance, BasicScheduler, BasicGuider, RandomNoise, KSamplerSelect, VAELoader, SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, SaveImage, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1951132199200432130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `FluxGuidance`
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`FluxGuidance`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`、`EmptyLatentImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

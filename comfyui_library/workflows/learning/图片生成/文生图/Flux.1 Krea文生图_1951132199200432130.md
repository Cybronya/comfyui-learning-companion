---
key: 图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json
name: Flux.1 Krea文生图_1951132199200432130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json
hash: bb8696c901bd76d5
coverage: 1
learned_at: 2026-10-10 20:58:36
nodes: [UNETLoader, DualCLIPLoader, FluxGuidance, BasicScheduler, BasicGuider, RandomNoise, KSamplerSelect, VAELoader, SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, SaveImage, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json`

## 结构

**节点**（13 个）：
- `UNETLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect`
- `VAELoader`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `CLIPTextEncode`
- `SaveImage`
- `EmptyLatentImage`

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `width` = `1024`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`FluxGuidance`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`、`EmptyLatentImage`

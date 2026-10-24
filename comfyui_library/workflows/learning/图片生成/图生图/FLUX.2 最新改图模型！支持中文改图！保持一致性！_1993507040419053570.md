---
key: 图片生成/图生图/FLUX.2 最新改图模型！支持中文改图！保持一致性！_1993507040419053570.json
name: FLUX.2 最新改图模型！支持中文改图！保持一致性！_1993507040419053570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 最新改图模型！支持中文改图！保持一致性！_1993507040419053570.json
hash: 0e95a342ad8dbb18
coverage: 0.84
learned_at: 2026-10-23 10:54:08
nodes: [Flux2Scheduler, BasicGuider, VAEEncode, FluxGuidance, KSamplerSelect, ReferenceLatent, PrimitiveNode, PrimitiveNode, VAELoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, ImageScaleToTotalPixels, Note, UNETLoader, RandomNoise, SaveImage, CLIPLoader, MarkdownNote, LoadImage, LoadImage, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 最新改图模型！支持中文改图！保持一致性！_1993507040419053570.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 最新改图模型！支持中文改图！保持一致性！_1993507040419053570.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAEEncode` ★核心
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `UNETLoader` ★核心
- `RandomNoise`
- `SaveImage`
- `CLIPLoader`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **84%**（21/25）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAEEncode`、`FluxGuidance`、`KSamplerSelect`、`ReferenceLatent`、`VAELoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageScaleToTotalPixels`、`UNETLoader`、`RandomNoise`、`SaveImage`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect

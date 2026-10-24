---
key: 图片生成/图生图/【遇见AI】FLUX模型Mistoline版线条Controlnet_2041086725912530946.json
name: 【遇见AI】FLUX模型Mistoline版线条Controlnet_2041086725912530946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型Mistoline版线条Controlnet_2041086725912530946.json
hash: 3303e845919d96bc
coverage: 0.823529
learned_at: 2026-10-23 11:51:59
nodes: [Note, ApplyTheMistoFluxControlNet, AnyLineArtPreprocessor_aux, PreviewImage, CLIPTextEncodeFlux, ModelSamplingFlux, ConditioningZeroOut, KSamplerTheMisto, SaveImage, Note, LoadImage, LoadImage, UnetLoaderGGUF, DualCLIPLoader, VAELoader, LoadImage, LoadTheMistoFluxControlNet]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】FLUX模型Mistoline版线条Controlnet_2041086725912530946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型Mistoline版线条Controlnet_2041086725912530946.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Output → Other

**节点**（17 个）：
- `Note`
- `ApplyTheMistoFluxControlNet`
- `AnyLineArtPreprocessor_aux`
- `PreviewImage`
- `CLIPTextEncodeFlux` ★核心
- `ModelSamplingFlux`
- `ConditioningZeroOut`
- `KSamplerTheMisto` ★核心
- `SaveImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadTheMistoFluxControlNet`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ApplyTheMistoFluxControlNet`、`AnyLineArtPreprocessor_aux`、`CLIPTextEncodeFlux`、`ModelSamplingFlux`、`ConditioningZeroOut`、`KSamplerTheMisto`、`SaveImage`、`LoadImage`、`UnetLoaderGGUF`、`DualCLIPLoader`、`VAELoader`、`LoadTheMistoFluxControlNet`

**用到的条目**：VAELoader、ConditioningZeroOut、LoadImage、ApplyTheMistoFluxControlNet、LoadTheMistoFluxControlNet、KSamplerTheMisto、CLIPTextEncodeFlux、DualCLIPLoader

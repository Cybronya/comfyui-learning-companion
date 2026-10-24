---
key: 图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json
name: 【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json
hash: 343a7fd6a33cc91e
coverage: 0.8
learned_at: 2026-10-23 11:52:01
nodes: [ModelSamplingFlux, PrimitiveNode, ApplyFluxControlNet, CLIPTextEncodeFlux, EmptyLatentImage, VAEDecode, PrimitiveNode, CannyEdgePreprocessor, PreviewImage, ConditioningZeroOut, SaveImage, XlabsSampler, Note, LoadImage, LoadImage, LoadImage, UnetLoaderGGUF, DualCLIPLoader, LoadFluxControlNet, VAELoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 768}
---

# 图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（20 个）：
- `ModelSamplingFlux`
- `PrimitiveNode`
- `ApplyFluxControlNet`
- `CLIPTextEncodeFlux` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PrimitiveNode`
- `CannyEdgePreprocessor`
- `PreviewImage`
- `ConditioningZeroOut`
- `SaveImage`
- `XlabsSampler` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `LoadFluxControlNet`
- `VAELoader`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`ModelSamplingFlux`、`ApplyFluxControlNet`、`CLIPTextEncodeFlux`、`EmptyLatentImage`、`VAEDecode`、`CannyEdgePreprocessor`、`ConditioningZeroOut`、`SaveImage`、`XlabsSampler`、`LoadImage`、`UnetLoaderGGUF`、`DualCLIPLoader`、`LoadFluxControlNet`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、ApplyFluxControlNet、CannyEdgePreprocessor、LoadFluxControlNet

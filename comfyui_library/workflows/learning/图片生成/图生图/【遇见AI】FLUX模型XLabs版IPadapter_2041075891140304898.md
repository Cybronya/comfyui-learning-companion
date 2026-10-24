---
key: 图片生成/图生图/【遇见AI】FLUX模型XLabs版IPadapter_2041075891140304898.json
name: 【遇见AI】FLUX模型XLabs版IPadapter_2041075891140304898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型XLabs版IPadapter_2041075891140304898.json
hash: 18f58068612c8c2b
coverage: 0.833333
learned_at: 2026-10-23 11:52:01
nodes: [ModelSamplingFlux, ConditioningZeroOut, VAEDecode, SaveImage, EmptyLatentImage, PrimitiveNode, PrimitiveNode, XlabsSampler, Note, LoadImage, LoadImage, UnetLoaderGGUF, DualCLIPLoader, VAELoader, LoadFluxIPAdapter, LoadImage, CLIPTextEncodeFlux, ApplyFluxIPAdapter]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/【遇见AI】FLUX模型XLabs版IPadapter_2041075891140304898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型XLabs版IPadapter_2041075891140304898.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（18 个）：
- `ModelSamplingFlux`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `XlabsSampler` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadFluxIPAdapter`
- `LoadImage`
- `CLIPTextEncodeFlux` ★核心
- `ApplyFluxIPAdapter`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`ModelSamplingFlux`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`XlabsSampler`、`LoadImage`、`UnetLoaderGGUF`、`DualCLIPLoader`、`VAELoader`、`LoadFluxIPAdapter`、`CLIPTextEncodeFlux`、`ApplyFluxIPAdapter`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、XlabsSampler、CLIPTextEncodeFlux、DualCLIPLoader

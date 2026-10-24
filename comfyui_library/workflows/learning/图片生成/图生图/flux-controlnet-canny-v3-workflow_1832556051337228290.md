---
key: 图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json
name: flux-controlnet-canny-v3-workflow_1832556051337228290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json
hash: 0cae02697a0e7a98
coverage: 0.888889
learned_at: 2026-10-23 11:35:34
nodes: [CLIPTextEncodeFlux, LoadFluxControlNet, VAELoader, DualCLIPLoader, UNETLoader, VAEDecode, CannyEdgePreprocessor, SaveImage, PreviewImage, SaveImage, CLIPTextEncodeFlux, EmptyLatentImage, GetImageSize+, ApplyFluxControlNet, XlabsSampler, LoadImage, easy imageScaleDownToSize, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPTextEncodeFlux` ★核心
- `LoadFluxControlNet`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CannyEdgePreprocessor`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `CLIPTextEncodeFlux` ★核心
- `EmptyLatentImage` ★核心
- `GetImageSize+`
- `ApplyFluxControlNet`
- `XlabsSampler` ★核心
- `LoadImage`
- `easy imageScaleDownToSize`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPTextEncodeFlux`、`LoadFluxControlNet`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`VAEDecode`、`CannyEdgePreprocessor`、`SaveImage`、`EmptyLatentImage`、`GetImageSize+`、`ApplyFluxControlNet`、`XlabsSampler`、`LoadImage`、`easy imageScaleDownToSize`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、ApplyFluxControlNet、CannyEdgePreprocessor、LoadFluxControlNet

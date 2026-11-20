---
key: 平台全量/FLUX STYLE TRANSFER (better version)_1869661957786603522.json
name: FLUX STYLE TRANSFER (better version)_1869661957786603522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX STYLE TRANSFER (better version)_1869661957786603522.json
hash: cc23bf6af377558a
coverage: 0.793103
learned_at: 2026-11-14 00:24:40
nodes: [EmptyLatentImage, PreviewImage, LoadFluxControlNet, PreviewImage, PreviewImage, PreviewImage, CannyEdgePreprocessor, HEDPreprocessor, LoadFluxControlNet, LoadImage, DepthAnythingPreprocessor, CLIPTextEncodeFlux, ApplyFluxControlNet, LoadImage, ApplyFluxIPAdapter, LoadFluxIPAdapter, ImageScale, Fast Groups Bypasser (rgthree), ApplyFluxControlNet, ApplyFluxControlNet, XlabsSampler, CLIPTextEncodeFlux, UNETLoader, DualCLIPLoader, LoadFluxControlNet, VAELoader, VAEDecode, SaveImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/FLUX STYLE TRANSFER (better version)_1869661957786603522.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX STYLE TRANSFER (better version)_1869661957786603522.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `LoadFluxControlNet`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `CannyEdgePreprocessor`
- `HEDPreprocessor`
- `LoadFluxControlNet`
- `LoadImage`
- `DepthAnythingPreprocessor`
- `CLIPTextEncodeFlux` ★核心
- `ApplyFluxControlNet`
- `LoadImage`
- `ApplyFluxIPAdapter`
- `LoadFluxIPAdapter`
- `ImageScale`
- `Fast Groups Bypasser (rgthree)`
- `ApplyFluxControlNet`
- `ApplyFluxControlNet`
- `XlabsSampler` ★核心
- `CLIPTextEncodeFlux` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadFluxControlNet`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`EmptyLatentImage`、`LoadFluxControlNet`、`CannyEdgePreprocessor`、`HEDPreprocessor`、`LoadImage`、`DepthAnythingPreprocessor`、`CLIPTextEncodeFlux`、`ApplyFluxControlNet`、`ApplyFluxIPAdapter`、`LoadFluxIPAdapter`、`ImageScale`、`XlabsSampler`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、ApplyFluxControlNet、CannyEdgePreprocessor、DepthAnythingPreprocessor

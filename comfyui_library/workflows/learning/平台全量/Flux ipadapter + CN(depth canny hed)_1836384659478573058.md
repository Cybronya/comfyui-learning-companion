---
key: 平台全量/Flux ipadapter + CN(depth canny hed)_1836384659478573058.json
name: Flux ipadapter + CN(depth canny hed)_1836384659478573058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux ipadapter + CN(depth canny hed)_1836384659478573058.json
hash: e3d82b074c1b124e
coverage: 0.793103
learned_at: 2026-11-14 00:28:08
nodes: [EmptyLatentImage, PreviewImage, PreviewImage, PreviewImage, HEDPreprocessor, DepthAnythingPreprocessor, CLIPTextEncodeFlux, ImageScale, UNETLoader, DualCLIPLoader, VAELoader, LoadFluxIPAdapter, PreviewImage, CannyEdgePreprocessor, ApplyFluxControlNet, ApplyFluxControlNet, LoadFluxControlNet, LoadFluxControlNet, LoadFluxControlNet, ApplyFluxControlNet, ApplyFluxIPAdapter, XlabsSampler, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), VAEDecode, SaveImage, Note, CLIPTextEncodeFlux]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Flux ipadapter + CN(depth canny hed)_1836384659478573058.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux ipadapter + CN(depth canny hed)_1836384659478573058.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `HEDPreprocessor`
- `DepthAnythingPreprocessor`
- `CLIPTextEncodeFlux` ★核心
- `ImageScale`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadFluxIPAdapter`
- `PreviewImage`
- `CannyEdgePreprocessor`
- `ApplyFluxControlNet`
- `ApplyFluxControlNet`
- `LoadFluxControlNet`
- `LoadFluxControlNet`
- `LoadFluxControlNet`
- `ApplyFluxControlNet`
- `ApplyFluxIPAdapter`
- `XlabsSampler` ★核心
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `CLIPTextEncodeFlux` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`EmptyLatentImage`、`HEDPreprocessor`、`DepthAnythingPreprocessor`、`CLIPTextEncodeFlux`、`ImageScale`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoadFluxIPAdapter`、`CannyEdgePreprocessor`、`ApplyFluxControlNet`、`LoadFluxControlNet`、`ApplyFluxIPAdapter`、`XlabsSampler`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、ApplyFluxControlNet、CannyEdgePreprocessor、DepthAnythingPreprocessor

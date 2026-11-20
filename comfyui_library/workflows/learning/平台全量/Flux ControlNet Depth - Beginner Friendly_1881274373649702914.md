---
key: 平台全量/Flux ControlNet Depth - Beginner Friendly_1881274373649702914.json
name: Flux ControlNet Depth - Beginner Friendly_1881274373649702914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux ControlNet Depth - Beginner Friendly_1881274373649702914.json
hash: 9ea0c7d7295ed23f
coverage: 0.736842
learned_at: 2026-11-14 00:27:33
nodes: [XlabsSampler, EmptyLatentImage, LoadImage, CLIPTextEncodeFlux, SaveImage, PreviewImage, Note, Note, Image Comparer (rgthree), VAELoader, UnetLoaderGGUF, DualCLIPLoader, AIO_Preprocessor, LoadFluxControlNet, VAEDecode, ImageResizeKJ, CLIPTextEncodeFlux, Note, ApplyFluxControlNet]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Flux ControlNet Depth - Beginner Friendly_1881274373649702914.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux ControlNet Depth - Beginner Friendly_1881274373649702914.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `XlabsSampler` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `CLIPTextEncodeFlux` ★核心
- `SaveImage`
- `PreviewImage`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `AIO_Preprocessor`
- `LoadFluxControlNet`
- `VAEDecode` ★核心
- `ImageResizeKJ`
- `CLIPTextEncodeFlux` ★核心
- `Note`
- `ApplyFluxControlNet`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`XlabsSampler`、`EmptyLatentImage`、`LoadImage`、`CLIPTextEncodeFlux`、`SaveImage`、`VAELoader`、`UnetLoaderGGUF`、`DualCLIPLoader`、`AIO_Preprocessor`、`LoadFluxControlNet`、`VAEDecode`、`ImageResizeKJ`、`ApplyFluxControlNet`

**用到的条目**：VAEDecode、VAELoader、EmptyLatentImage、LoadImage、ApplyFluxControlNet、LoadFluxControlNet、XlabsSampler、CLIPTextEncodeFlux

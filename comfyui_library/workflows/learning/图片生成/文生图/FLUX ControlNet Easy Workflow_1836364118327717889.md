---
key: FLUX ControlNet Easy Workflow_1836364118327717889.json
name: FLUX ControlNet Easy Workflow_1836364118327717889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX ControlNet Easy Workflow_1836364118327717889.json
hash: a1266c6095cd349c
coverage: 0.9375
learned_at: 2026-10-10 20:58:31
nodes: [PreviewImage, VAELoader, CLIPTextEncode, VAEDecode, CLIPTextEncodeFlux, AIO_Preprocessor, LoadFluxControlNet, SaveImage, CLIPTextEncodeFlux, LoadImage, XlabsSampler, DualCLIPLoaderGGUF, EmptyLatentImage, UNETLoader, UnetLoaderGGUF, ApplyFluxControlNet]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 768, "width": 512}
---

# FLUX ControlNet Easy Workflow_1836364118327717889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX ControlNet Easy Workflow_1836364118327717889.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（16 个）：
- `PreviewImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `AIO_Preprocessor`
- `LoadFluxControlNet`
- `SaveImage`
- `CLIPTextEncodeFlux` ★核心
- `LoadImage`
- `XlabsSampler` ★核心
- `DualCLIPLoaderGGUF`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `ApplyFluxControlNet`

## 关键参数

- `width` = `512`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`CLIPTextEncodeFlux`、`AIO_Preprocessor`、`LoadFluxControlNet`、`SaveImage`、`LoadImage`、`XlabsSampler`、`DualCLIPLoaderGGUF`、`EmptyLatentImage`、`UNETLoader`、`UnetLoaderGGUF`、`ApplyFluxControlNet`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ApplyFluxControlNet、LoadFluxControlNet

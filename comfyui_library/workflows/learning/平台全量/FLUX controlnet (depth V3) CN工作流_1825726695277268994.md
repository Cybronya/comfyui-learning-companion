---
key: 平台全量/FLUX controlnet (depth V3) CN工作流_1825726695277268994.json
name: FLUX controlnet (depth V3) CN工作流_1825726695277268994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX controlnet (depth V3) CN工作流_1825726695277268994.json
hash: 7c1c0356b46dc9b4
coverage: 0.888889
learned_at: 2026-11-14 00:24:41
nodes: [LoadImage, ApplyFluxControlNet, LoadFluxControlNet, VAELoader, SaveImage, VAEDecode, PreviewImage, XlabsSampler, AIO_Preprocessor, SaveImage, PreviewImage, DualCLIPLoader, CLIPTextEncodeFlux, EmptyLatentImage, ModelSamplingFlux, ImageResize+, UNETLoader, CLIPTextEncodeFlux]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 平台全量/FLUX controlnet (depth V3) CN工作流_1825726695277268994.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX controlnet (depth V3) CN工作流_1825726695277268994.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `LoadImage`
- `ApplyFluxControlNet`
- `LoadFluxControlNet`
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `XlabsSampler` ★核心
- `AIO_Preprocessor`
- `SaveImage`
- `PreviewImage`
- `DualCLIPLoader`
- `CLIPTextEncodeFlux` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingFlux`
- `ImageResize+`
- `UNETLoader` ★核心
- `CLIPTextEncodeFlux` ★核心

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`LoadImage`、`ApplyFluxControlNet`、`LoadFluxControlNet`、`VAELoader`、`SaveImage`、`VAEDecode`、`XlabsSampler`、`AIO_Preprocessor`、`DualCLIPLoader`、`CLIPTextEncodeFlux`、`EmptyLatentImage`、`ModelSamplingFlux`、`ImageResize+`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、ApplyFluxControlNet、LoadFluxControlNet、XlabsSampler

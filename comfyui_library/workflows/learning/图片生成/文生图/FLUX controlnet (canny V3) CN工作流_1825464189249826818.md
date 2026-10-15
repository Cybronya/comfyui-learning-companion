---
key: 图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json
name: FLUX controlnet (canny V3) CN工作流_1825464189249826818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json
hash: 321962907ef08c28
coverage: 0.833333
learned_at: 2026-10-10 20:58:31
nodes: [PreviewImage, AIO_Preprocessor, ApplyFluxControlNet, PreviewImage, LoadFluxControlNet, SaveImage, VAEDecode, VAELoader, ImageResize+, LoadImage, DualCLIPLoader, ModelSamplingFlux, UNETLoader, XlabsSampler, CLIPTextEncodeFlux, CLIPTextEncodeFlux, VAEEncode, EmptyLatentImage]
patterns: []
missing: [ImageResize+]
parameters: {"batch_size": 1, "height": 512, "width": 512}
discoveries: [次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json`

## 结构

**节点**（18 个）：
- `PreviewImage`
- `AIO_Preprocessor`
- `ApplyFluxControlNet`
- `PreviewImage`
- `LoadFluxControlNet`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `ImageResize+`
- `LoadImage`
- `DualCLIPLoader`
- `ModelSamplingFlux`
- `UNETLoader`
- `XlabsSampler`
- `CLIPTextEncodeFlux`
- `CLIPTextEncodeFlux`
- `VAEEncode`
- `EmptyLatentImage`

## 关键参数

- `batch_size` = `1`
- `height` = `512`
- `width` = `512`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`PreviewImage`、`AIO_Preprocessor`、`ApplyFluxControlNet`、`LoadFluxControlNet`、`SaveImage`、`VAEDecode`、`VAELoader`、`ImageResize+`、`LoadImage`、`DualCLIPLoader`、`ModelSamplingFlux`、`UNETLoader`、`XlabsSampler`、`CLIPTextEncodeFlux`

**缺卡**（1）：`ImageResize+`

## 学习发现

- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明

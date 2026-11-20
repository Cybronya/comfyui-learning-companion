---
key: 平台全量/Flux 室内设计 _ Flux Redux Roomdesigner_1864869212488683521.json
name: Flux 室内设计 _ Flux Redux Roomdesigner_1864869212488683521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux 室内设计 _ Flux Redux Roomdesigner_1864869212488683521.json
hash: 79e4fb3086301bf7
coverage: 0.862069
learned_at: 2026-11-14 00:28:16
nodes: [Florence2Run, LoadImage, LoadImage, DownloadAndLoadFlorence2Model, Florence2Run, LoadImage, CLIPVisionEncode, Text List, Text List to Text, Florence2Run, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, StyleModelApply, StyleModelApply, StyleModelApply, FluxSamplerParams+, VAELoader, SaveImage, VAEDecode, PreviewImage, UnetLoaderGGUF, DualCLIPLoaderGGUF, StyleModelLoader, CLIPVisionLoader, Note, Note, Note, SDXLEmptyLatentSizePicker+]
patterns: []
missing: []
parameters: {"batch_size": 0, "height": 1, "width": "1024x1024 (1.0)"}
---

# 平台全量/Flux 室内设计 _ Flux Redux Roomdesigner_1864869212488683521.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux 室内设计 _ Flux Redux Roomdesigner_1864869212488683521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `Florence2Run`
- `LoadImage`
- `LoadImage`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `LoadImage`
- `CLIPVisionEncode`
- `Text List`
- `Text List to Text`
- `Florence2Run`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `StyleModelApply`
- `StyleModelApply`
- `StyleModelApply`
- `FluxSamplerParams+` ★核心
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoaderGGUF`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `Note`
- `Note`
- `Note`
- `SDXLEmptyLatentSizePicker+` ★核心

## 关键参数

- `width` = `1024x1024 (1.0)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`Florence2Run`、`LoadImage`、`DownloadAndLoadFlorence2Model`、`CLIPVisionEncode`、`Text List`、`Text List to Text`、`CLIPTextEncode`、`StyleModelApply`、`FluxSamplerParams+`、`VAELoader`、`SaveImage`、`VAEDecode`、`UnetLoaderGGUF`、`DualCLIPLoaderGGUF`、`StyleModelLoader`、`CLIPVisionLoader`、`SDXLEmptyLatentSizePicker+`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxSamplerParams+、CLIPVisionEncode、SDXLEmptyLatentSizePicker+、StyleModelApply

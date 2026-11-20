---
key: 平台全量/多图融合室内设计 Flux Redux RoomDesigner_1860229849133748226.json
name: 多图融合室内设计 Flux Redux RoomDesigner_1860229849133748226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/多图融合室内设计 Flux Redux RoomDesigner_1860229849133748226.json
hash: c3d3555d1e653df7
coverage: 1
learned_at: 2026-11-14 01:57:40
nodes: [Florence2Run, Florence2Run, DownloadAndLoadFlorence2Model, Florence2Run, Text List, Text List to Text, CLIPVisionEncode, StyleModelApply, StyleModelApply, CLIPVisionEncode, CLIPVisionLoader, StyleModelLoader, CLIPTextEncode, FluxSamplerParams+, StyleModelApply, VAEDecode, SaveImage, CLIPVisionEncode, UnetLoaderGGUF, DualCLIPLoaderGGUF, VAELoader, LoadImage, LoadImage, LoadImage, SDXLEmptyLatentSizePicker+]
patterns: []
missing: []
parameters: {"batch_size": 0, "height": 1, "width": "1280x768 (1.67)"}
---

# 平台全量/多图融合室内设计 Flux Redux RoomDesigner_1860229849133748226.json

> 来源文件 `comfyui_library/workflows/平台全量/多图融合室内设计 Flux Redux RoomDesigner_1860229849133748226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `Florence2Run`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `Text List`
- `Text List to Text`
- `CLIPVisionEncode`
- `StyleModelApply`
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CLIPTextEncode` ★核心
- `FluxSamplerParams+` ★核心
- `StyleModelApply`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPVisionEncode`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SDXLEmptyLatentSizePicker+` ★核心

## 关键参数

- `width` = `1280x768 (1.67)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`Florence2Run`、`DownloadAndLoadFlorence2Model`、`Text List`、`Text List to Text`、`CLIPVisionEncode`、`StyleModelApply`、`CLIPVisionLoader`、`StyleModelLoader`、`CLIPTextEncode`、`FluxSamplerParams+`、`VAEDecode`、`SaveImage`、`UnetLoaderGGUF`、`DualCLIPLoaderGGUF`、`VAELoader`、`LoadImage`、`SDXLEmptyLatentSizePicker+`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxSamplerParams+、CLIPVisionEncode、SDXLEmptyLatentSizePicker+、StyleModelApply

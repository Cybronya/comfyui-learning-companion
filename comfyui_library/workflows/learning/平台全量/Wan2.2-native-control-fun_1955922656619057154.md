---
key: 平台全量/Wan2.2-native-control-fun_1955922656619057154.json
name: Wan2.2-native-control-fun_1955922656619057154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-native-control-fun_1955922656619057154.json
hash: 41b53a1f82f7412f
coverage: 0.888889
learned_at: 2026-11-14 01:06:08
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CreateVideo, VAEDecode, CLIPLoader, VAELoader, SaveVideo, GetVideoComponents, Canny, LoadVideo, ModelSamplingSD3, Wan22FunControlToVideo, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, LoadImage, PreviewImage, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, CLIPTextEncode, Note, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, MarkdownNote, CLIPTextEncode, VHS_LoadVideo, GetImageSizeAndCount, Wan22FunControlToVideo, PreviewImage, ImageResizeKJv2, ImageResizeKJv2, UNETLoader, UNETLoader, LoadImage, VHS_VideoCombine, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/Wan2.2-native-control-fun_1955922656619057154.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-native-control-fun_1955922656619057154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveVideo`
- `GetVideoComponents`
- `Canny`
- `LoadVideo`
- `ModelSamplingSD3`
- `Wan22FunControlToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `PreviewImage`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `Note`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `Wan22FunControlToVideo`
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`GetVideoComponents`、`Canny`、`LoadVideo`、`Wan22FunControlToVideo`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、Canny

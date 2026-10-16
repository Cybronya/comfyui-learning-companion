---
key: 视频生成/文生视频/wan2.2动作迁移美女跳舞（fun-control）V1.0官方版_1958382181972393985.json
name: wan2.2动作迁移美女跳舞（fun-control）V1.0官方版_1958382181972393985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1958382181972393985.json
hash: 7c26881f524cb677
coverage: 0.862069
learned_at: 2026-10-15 22:43:42
nodes: [CreateVideo, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, SaveVideo, PreviewImage, Canny, VAELoader, CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, LoadImage, Wan22FunControlToVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, Note, CreateVideo, VAEDecode, KSamplerAdvanced, CLIPTextEncode, Text Concatenate, VHS_LoadVideoFFmpeg, ImageResizeKJv2, MarkdownNote, CreateVideo, ImageResizeKJv2, PreviewImage, Note, PrimitiveInt, PrimitiveInt, AIO_Preprocessor, SaveVideo, SaveVideo, RH_Captioner, VHS_LoadVideo, Text Multiline, UNETLoader, UNETLoader, CLIPLoader, ImageBlend, ImageConcatMulti, Zoe-DepthMapPreprocessor, DWPreprocessor, Canny, PrimitiveInt, Wan22FunControlToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2动作迁移美女跳舞（fun-control）V1.0官方版_1958382181972393985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958382181972393985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `CreateVideo`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveVideo`
- `PreviewImage`
- `Canny`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Wan22FunControlToVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `Note`
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `VHS_LoadVideoFFmpeg`
- `ImageResizeKJv2`
- `MarkdownNote`
- `CreateVideo`
- `ImageResizeKJv2`
- `PreviewImage`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `AIO_Preprocessor`
- `SaveVideo`
- `SaveVideo`
- `RH_Captioner`
- `VHS_LoadVideo`
- `Text Multiline`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ImageBlend`
- `ImageConcatMulti`
- `Zoe-DepthMapPreprocessor`
- `DWPreprocessor`
- `Canny`
- `PrimitiveInt`
- `Wan22FunControlToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（50/58）

**有卡**：`CreateVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveVideo`、`Canny`、`CLIPTextEncode`、`ModelSamplingSD3`、`LoadImage`、`Wan22FunControlToVideo`、`KSamplerAdvanced`、`Text Concatenate`、`VHS_LoadVideoFFmpeg`、`ImageResizeKJv2`、`AIO_Preprocessor`、`RH_Captioner`、`VHS_LoadVideo`、`Text Multiline`、`ImageBlend`、`ImageConcatMulti`、`Zoe-DepthMapPreprocessor`、`DWPreprocessor`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Canny

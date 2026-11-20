---
key: 平台全量/万相wan2.2视频图像驱动 B站：乔治-周士诚_1957370684315987969.json
name: 万相wan2.2视频图像驱动 B站：乔治-周士诚_1957370684315987969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/万相wan2.2视频图像驱动 B站：乔治-周士诚_1957370684315987969.json
hash: ca303df0215fa299
coverage: 0.965517
learned_at: 2026-11-14 01:32:24
nodes: [VAEDecode, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, Wan22FunControlToVideo, ImageScale, ImageScale, DepthAnythingV2Preprocessor, DWPreprocessor, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, VHS_LoadVideo, TextInput_, TextInput_, VHS_VideoCombine, QZ_ResolutionPreset, easy int, TextInput_, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/万相wan2.2视频图像驱动 B站：乔治-周士诚_1957370684315987969.json

> 来源文件 `comfyui_library/workflows/平台全量/万相wan2.2视频图像驱动 B站：乔治-周士诚_1957370684315987969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Wan22FunControlToVideo`
- `ImageScale`
- `ImageScale`
- `DepthAnythingV2Preprocessor`
- `DWPreprocessor`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `TextInput_`
- `TextInput_`
- `VHS_VideoCombine`
- `QZ_ResolutionPreset`
- `easy int`
- `TextInput_`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`VAEDecode`、`WanVideoNAG`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`Wan22FunControlToVideo`、`ImageScale`、`DepthAnythingV2Preprocessor`、`DWPreprocessor`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`VHS_VideoCombine`、`VHS_LoadVideo`、`TextInput_`、`QZ_ResolutionPreset`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、DepthAnythingV2Preprocessor

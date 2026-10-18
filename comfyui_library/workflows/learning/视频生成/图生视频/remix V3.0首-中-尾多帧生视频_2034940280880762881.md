---
key: 视频生成/图生视频/remix V3.0首-中-尾多帧生视频_2034940280880762881.json
name: remix V3.0首-中-尾多帧生视频_2034940280880762881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/remix V3.0首-中-尾多帧生视频_2034940280880762881.json
hash: 76044de78a49e9ba
coverage: 0.921053
learned_at: 2026-10-15 22:35:47
nodes: [CLIPTextEncode, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, Seed (rgthree), INTConstant, INTConstant, KSamplerAdvanced, CLIPTextEncode, LatentFromBatch, VHS_VideoCombine, llama_cpp_parameters, ImageResizeKJv2, ImageStitch, PreviewImage, INTConstant, INTConstant, INTConstant, easy showAnything, WanFirstMiddleLastFrameToVideo, PrimitiveStringMultiline, ImageStitch, CLIPVisionEncode, CLIPVisionEncode, llama_cpp_model_loader, UNETLoader, UNETLoader, LoadImage, LoadImage, ImageResizeKJv2, CLIPVisionLoader, CLIPVisionEncode, LoadImage, ImageResizeKJv2, CLIPLoader, VAELoader, KSamplerAdvanced, llama_cpp_instruct_adv]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/remix V3.0首-中-尾多帧生视频_2034940280880762881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034940280880762881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `INTConstant`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LatentFromBatch`
- `VHS_VideoCombine`
- `llama_cpp_parameters`
- `ImageResizeKJv2`
- `ImageStitch`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `easy showAnything`
- `WanFirstMiddleLastFrameToVideo`
- `PrimitiveStringMultiline`
- `ImageStitch`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `llama_cpp_instruct_adv`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`Seed (rgthree)`、`INTConstant`、`KSamplerAdvanced`、`LatentFromBatch`、`VHS_VideoCombine`、`llama_cpp_parameters`、`ImageResizeKJv2`、`ImageStitch`、`WanFirstMiddleLastFrameToVideo`、`CLIPVisionEncode`、`llama_cpp_model_loader`、`UNETLoader`、`LoadImage`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

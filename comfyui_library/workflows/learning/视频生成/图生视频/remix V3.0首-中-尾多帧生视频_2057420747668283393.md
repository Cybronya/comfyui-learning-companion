---
key: 视频生成/图生视频/remix V3.0首-中-尾多帧生视频_2057420747668283393.json
name: remix V3.0首-中-尾多帧生视频_2057420747668283393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2057420747668283393.json
hash: 584a68a42cd0fa2a
coverage: 0.921053
learned_at: 2026-10-15 22:38:12
nodes: [CLIPTextEncode, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, Seed (rgthree), INTConstant, INTConstant, KSamplerAdvanced, VHS_VideoCombine, llama_cpp_parameters, ImageStitch, PreviewImage, INTConstant, INTConstant, INTConstant, WanFirstMiddleLastFrameToVideo, ImageStitch, llama_cpp_model_loader, UNETLoader, UNETLoader, CLIPVisionLoader, ImageResizeKJv2, CLIPLoader, VAELoader, KSamplerAdvanced, LoadImage, ImageResizeKJv2, PrimitiveStringMultiline, LatentFromBatch, CLIPVisionEncode, LoadImage, ImageResizeKJv2, LoadImage, CLIPVisionEncode, CLIPVisionEncode, llama_cpp_instruct_adv, CLIPTextEncode, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/remix V3.0首-中-尾多帧生视频_2057420747668283393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057420747668283393.json`

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
- `VHS_VideoCombine`
- `llama_cpp_parameters`
- `ImageStitch`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanFirstMiddleLastFrameToVideo`
- `ImageStitch`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `LatentFromBatch`
- `CLIPVisionEncode`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `easy showAnything`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingSD3`、`Seed (rgthree)`、`INTConstant`、`KSamplerAdvanced`、`VHS_VideoCombine`、`llama_cpp_parameters`、`ImageStitch`、`WanFirstMiddleLastFrameToVideo`、`llama_cpp_model_loader`、`UNETLoader`、`CLIPVisionLoader`、`ImageResizeKJv2`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LatentFromBatch`、`CLIPVisionEncode`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

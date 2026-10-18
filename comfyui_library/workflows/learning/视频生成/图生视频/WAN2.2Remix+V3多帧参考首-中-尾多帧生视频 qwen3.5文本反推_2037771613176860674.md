---
key: 视频生成/图生视频/WAN2.2Remix+V3多帧参考首-中-尾多帧生视频 qwen3.5文本反推_2037771613176860674.json
name: WAN2.2Remix+V3多帧参考首-中-尾多帧生视频 qwen3.5文本反推_2037771613176860674.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2Remix+V3多帧参考首-中-尾多帧生视频 qwen3.5文本反推_2037771613176860674.json
hash: 71c0c459a9c11f88
coverage: 0.954545
learned_at: 2026-10-15 22:35:58
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, ImageResizeKJv2, CLIPVisionEncode, VAELoader, Seed (rgthree), CLIPVisionLoader, ImageResizeKJv2, CLIPLoader, PrimitiveStringMultiline, INTConstant, INTConstant, SaveVideo, VAEDecode, ImageResizeKJv2, llama_cpp_parameters, ImageBatchMulti, LoadImage, VRAM_Debug, UNETLoader, UNETLoader, VRAM_Debug, VRAM_Debug, VRAM_Debug, llama_cpp_model_loader, VRAM_Debug, ShowText|pysssss, KSamplerAdvanced, ColorMatch, CreateVideo, VRAM_Debug, INTConstant, WanFirstMiddleLastFrameToVideo, INTConstant, INTConstant, KSamplerAdvanced, LoadImage, LoadImage, VRAM_Debug, llama_cpp_instruct_adv]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2Remix+V3多帧参考首-中-尾多帧生视频 qwen3.5文本反推_2037771613176860674.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037771613176860674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `VAELoader`
- `Seed (rgthree)`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `INTConstant`
- `INTConstant`
- `SaveVideo`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `llama_cpp_parameters`
- `ImageBatchMulti`
- `LoadImage`
- `VRAM_Debug`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VRAM_Debug`
- `VRAM_Debug`
- `VRAM_Debug`
- `llama_cpp_model_loader`
- `VRAM_Debug`
- `ShowText|pysssss`
- `KSamplerAdvanced` ★核心
- `ColorMatch`
- `CreateVideo`
- `VRAM_Debug`
- `INTConstant`
- `WanFirstMiddleLastFrameToVideo`
- `INTConstant`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `VRAM_Debug`
- `llama_cpp_instruct_adv`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`CLIPVisionEncode`、`ImageResizeKJv2`、`VAELoader`、`Seed (rgthree)`、`CLIPVisionLoader`、`CLIPLoader`、`INTConstant`、`SaveVideo`、`VAEDecode`、`llama_cpp_parameters`、`ImageBatchMulti`、`LoadImage`、`VRAM_Debug`、`UNETLoader`、`llama_cpp_model_loader`、`KSamplerAdvanced`、`ColorMatch`、`CreateVideo`、`WanFirstMiddleLastFrameToVideo`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)

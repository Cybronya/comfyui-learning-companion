---
key: 图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json
name: Flux.1文生图工作流（高清+去除AI感）_1954823552040091649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json
hash: 9276f0a6a7c4b35a
coverage: 0.789474
learned_at: 2026-10-15 22:26:26
nodes: [Lora Loader Stack (rgthree), CheckpointLoaderSimple, CLIPTextEncodeFlux, CFGZeroStar, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, EmptyLatentImage, SamplerCustomAdvanced, KSamplerAdvanced, Note, Note, Note, StringConstantMultiline, PreviewImage, CLIPTextEncode, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 31, "checkpoint": "flux1-dev-fp8.safetensors", "denoise": "normal", "height": 1920, "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1080}
---

# 图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `Lora Loader Stack (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncodeFlux` ★核心
- `CFGZeroStar`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `Note`
- `Note`
- `StringConstantMultiline`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `31`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`Lora Loader Stack (rgthree)`、`CheckpointLoaderSimple`、`CLIPTextEncodeFlux`、`CFGZeroStar`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`KSamplerAdvanced`、`StringConstantMultiline`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、KSamplerAdvanced、KSamplerSelect、SamplerCustomAdvanced、CFGZeroStar

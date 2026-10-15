---
key: 图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json
name: Flux.1文生图工作流（高清+去除AI感）_1954823552040091649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json
hash: 9276f0a6a7c4b35a
coverage: 0.736842
learned_at: 2026-10-10 20:58:36
nodes: [Lora Loader Stack (rgthree), CheckpointLoaderSimple, CLIPTextEncodeFlux, CFGZeroStar, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, EmptyLatentImage, SamplerCustomAdvanced, KSamplerAdvanced, Note, Note, Note, StringConstantMultiline, PreviewImage, CLIPTextEncode, VAEDecode, SaveImage]
patterns: []
missing: [Lora Loader Stack (rgthree)]
parameters: {"batch_size": 1, "cfg": 31, "checkpoint": "flux1-dev-fp8.safetensors", "denoise": "normal", "height": 1920, "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1080}
discoveries: [次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json`

## 结构

**节点**（19 个）：
- `Lora Loader Stack (rgthree)`
- `CheckpointLoaderSimple`
- `CLIPTextEncodeFlux`
- `CFGZeroStar`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect`
- `BasicScheduler`
- `EmptyLatentImage`
- `SamplerCustomAdvanced`
- `KSamplerAdvanced`
- `Note`
- `Note`
- `Note`
- `StringConstantMultiline`
- `PreviewImage`
- `CLIPTextEncode`
- `VAEDecode`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `31`
- `checkpoint` = `flux1-dev-fp8.safetensors`
- `denoise` = `normal`
- `height` = `1920`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `seed` = `enable`
- `steps` = `randomize`
- `width` = `1080`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`Lora Loader Stack (rgthree)`、`CheckpointLoaderSimple`、`CLIPTextEncodeFlux`、`CFGZeroStar`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`KSamplerAdvanced`、`Note`

**缺卡**（1）：`Lora Loader Stack (rgthree)`

## 学习发现

- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明

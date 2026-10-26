---
key: 图片生成/图生图/Flux.1-controlnet工作流_2113996622580506626.json
name: Flux.1-controlnet工作流_2113996622580506626
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-controlnet工作流_2113996622580506626.json
hash: 361c4cf7369a513f
coverage: 0.954545
learned_at: 2026-10-26 22:01:42
nodes: [ControlNetLoader, SetUnionControlNetType, AIO_Preprocessor, LoadImage, ControlNetLoader, SetUnionControlNetType, AIO_Preprocessor, LoadImage, ControlNetApplyAdvanced, ControlNetApplyAdvanced, FluxGuidance, KSampler, EmptyLatentImage, VAEDecode, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, UNETLoader, DualCLIPLoader, VAELoader, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 0.020000000000000004, "height": 168, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 584917678958068, "steps": 25, "width": 352}
---

# 图片生成/图生图/Flux.1-controlnet工作流_2113996622580506626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-controlnet工作流_2113996622580506626.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（22 个）：
- `ControlNetLoader`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `LoadImage`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `LoadImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `FluxGuidance`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `584917678958068`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.020000000000000004`
- `width` = `352`
- `height` = `168`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`ControlNetLoader`、`SetUnionControlNetType`、`AIO_Preprocessor`、`LoadImage`、`ControlNetApplyAdvanced`、`FluxGuidance`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

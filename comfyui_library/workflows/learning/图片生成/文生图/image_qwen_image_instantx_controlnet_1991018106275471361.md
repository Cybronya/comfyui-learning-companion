---
key: 图片生成/文生图/image_qwen_image_instantx_controlnet_1991018106275471361.json
name: image_qwen_image_instantx_controlnet_1991018106275471361
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image_qwen_image_instantx_controlnet_1991018106275471361.json
hash: 7358410156590cfa
coverage: 0.8
learned_at: 2026-10-19 20:34:27
nodes: [CLIPTextEncode, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, VAEDecode, Note, Note, MarkdownNote, MarkdownNote, Canny, ControlNetApplyAdvanced, VAEEncode, PreviewImage, LoraLoaderModelOnly, KSampler, SaveImage, MarkdownNote, CLIPTextEncode, MarkdownNote, LotusConditioning, KSamplerSelect, BasicGuider, DisableNoise, VAEDecode, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ImageInvert, VAELoader, UNETLoader, SetFirstSigma, BasicScheduler, LoadImage, VAELoader, ControlNetLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 670264600281320, "steps": 20}
---

# 图片生成/文生图/image_qwen_image_instantx_controlnet_1991018106275471361.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image_qwen_image_instantx_controlnet_1991018106275471361.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `Note`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `Canny`
- `ControlNetApplyAdvanced` ★核心
- `VAEEncode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LotusConditioning`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `DisableNoise`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ImageInvert`
- `VAELoader`
- `UNETLoader` ★核心
- `SetFirstSigma`
- `BasicScheduler`
- `LoadImage`
- `VAELoader`
- `ControlNetLoader`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `670264600281320`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`Canny`、`ControlNetApplyAdvanced`、`VAEEncode`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`LotusConditioning`、`KSamplerSelect`、`BasicGuider`、`DisableNoise`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`ImageInvert`、`VAELoader`、`SetFirstSigma`、`BasicScheduler`、`LoadImage`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

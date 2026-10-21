---
key: 图片生成/图生图/Krea2  3.8反推_2092915740558053377.json
name: Krea2  3.8反推_2092915740558053377
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Krea2  3.8反推_2092915740558053377.json
hash: 21cbab2b7475e30c
coverage: 0.956522
learned_at: 2026-10-21 00:40:50
nodes: [CLIPLoader, SeedVR2LoadDiTModel, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, INTConstant, llama_cpp_parameters, ImageResizeKJv2, llama_cpp_model_loader, KSampler, ConditioningZeroOut, VAEDecode, VAELoader, EmptyLatentImage, PreviewAny, Text, llama_cpp_instruct_adv, UNETLoader, ModelSamplingAuraFlow, CLIPTextEncode, SaveImage, SeedVR2VideoUpscaler, SaveImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2440, "sampler_name": "er_sde", "scheduler": "simple", "seed": 651766989273796, "steps": 10, "width": 1560}
---

# 图片生成/图生图/Krea2  3.8反推_2092915740558053377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Krea2  3.8反推_2092915740558053377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `llama_cpp_parameters`
- `ImageResizeKJv2`
- `llama_cpp_model_loader`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `Text`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `651766989273796`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1560`
- `height` = `2440`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`CLIPLoader`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`INTConstant`、`llama_cpp_parameters`、`ImageResizeKJv2`、`llama_cpp_model_loader`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`Text`、`llama_cpp_instruct_adv`、`UNETLoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`SaveImage`、`SeedVR2VideoUpscaler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

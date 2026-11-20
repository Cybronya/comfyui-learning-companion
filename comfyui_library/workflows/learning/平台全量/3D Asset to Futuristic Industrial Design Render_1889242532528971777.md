---
key: 平台全量/3D Asset to Futuristic Industrial Design Render_1889242532528971777.json
name: 3D Asset to Futuristic Industrial Design Render_1889242532528971777
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/3D Asset to Futuristic Industrial Design Render_1889242532528971777.json
hash: 642dad628eb604c1
coverage: 0.888889
learned_at: 2026-11-14 00:11:54
nodes: [LoadImage, Image Comparer (rgthree), SaveImage, ControlNetApplyAdvanced, IPAdapterUnifiedLoader, DF_Get_image_size, CLIPTextEncode, CLIPTextEncode, VAEDecode, EmptyLatentImage, IPAdapterAdvanced, KSampler, CheckpointLoaderSimple, AnyLinePreprocessor, LoraLoaderModelOnly, PreviewImage, ControlNetLoader, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "dreamshaperXL_lightningDPMSDE.safetensors", "controlnet_strength": 0.8, "denoise": 1, "height": 512, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 0, "steps": 25, "width": 512}
---

# 平台全量/3D Asset to Futuristic Industrial Design Render_1889242532528971777.json

> 来源文件 `comfyui_library/workflows/平台全量/3D Asset to Futuristic Industrial Design Render_1889242532528971777.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ControlNetApplyAdvanced` ★核心
- `IPAdapterUnifiedLoader`
- `DF_Get_image_size`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `IPAdapterAdvanced`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `AnyLinePreprocessor`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `ControlNetLoader`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `0.8`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `dreamshaperXL_lightningDPMSDE.safetensors`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`LoadImage`、`SaveImage`、`ControlNetApplyAdvanced`、`IPAdapterUnifiedLoader`、`DF_Get_image_size`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`IPAdapterAdvanced`、`KSampler`、`CheckpointLoaderSimple`、`AnyLinePreprocessor`、`LoraLoaderModelOnly`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced

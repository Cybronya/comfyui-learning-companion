---
key: 图片生成/文生图/Z-Image Base +ControlNet_2022640984902864898.json
name: Z-Image Base +ControlNet_2022640984902864898
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image Base +ControlNet_2022640984902864898.json
hash: 776e194380c065a3
coverage: 1
learned_at: 2026-10-19 22:29:57
nodes: [UNETLoader, CLIPLoader, CLIPTextEncode, ZImageFunControlnet, VAELoader, ModelSamplingAuraFlow, ModelPatchLoader, EmptyLatentImage, VAEDecode, KSampler, SaveImage, LoadImage, AIO_Preprocessor, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 602445123575679, "steps": 30, "width": 720}
---

# 图片生成/文生图/Z-Image Base +ControlNet_2022640984902864898.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image Base +ControlNet_2022640984902864898.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ZImageFunControlnet`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `ModelPatchLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `AIO_Preprocessor`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `602445123575679`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`ZImageFunControlnet`、`VAELoader`、`ModelSamplingAuraFlow`、`ModelPatchLoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

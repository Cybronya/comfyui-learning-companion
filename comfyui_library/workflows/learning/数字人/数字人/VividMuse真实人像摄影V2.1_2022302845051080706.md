---
key: 数字人/数字人/VividMuse真实人像摄影V2.1_2022302845051080706.json
name: VividMuse真实人像摄影V2.1_2022302845051080706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/VividMuse真实人像摄影V2.1_2022302845051080706.json
hash: 7d1778772d00109c
coverage: 0.964286
learned_at: 2026-10-26 01:57:36
nodes: [SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Tile_Batch, ImageScaleBy, TTP_Tile_image_size, SaveImage, UNETLoader, GetImageSize+, GetImageSize+, ImageResize+, TTP_Image_Assy, ImageResize+, ImageScaleBy, CLIPLoader, VAELoader, VAEDecode, ConditioningZeroOut, CLIPTextEncode, SaveImage, ModelSamplingAuraFlow, SeedVR2LoadDiTModel, LoraLoaderModelOnly, easy promptList, easy promptList, EmptyLatentImage, DF_Text_Box, KSamplerAdvanced, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 2048, "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed", "width": 1536}
---

# 数字人/数字人/VividMuse真实人像摄影V2.1_2022302845051080706.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/VividMuse真实人像摄影V2.1_2022302845051080706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `SaveImage`
- `UNETLoader` ★核心
- `GetImageSize+`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Image_Assy`
- `ImageResize+`
- `ImageScaleBy`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ModelSamplingAuraFlow`
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `easy promptList`
- `easy promptList`
- `EmptyLatentImage` ★核心
- `DF_Text_Box`
- `KSamplerAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`TTP_Tile_image_size`、`SaveImage`、`UNETLoader`、`GetImageSize+`、`ImageResize+`、`TTP_Image_Assy`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`easy promptList`、`EmptyLatentImage`、`DF_Text_Box`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

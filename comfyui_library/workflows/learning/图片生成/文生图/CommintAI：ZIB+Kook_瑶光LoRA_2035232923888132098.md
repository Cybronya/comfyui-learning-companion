---
key: 图片生成/文生图/CommintAI：ZIB+Kook_瑶光LoRA_2035232923888132098.json
name: CommintAI：ZIB+Kook_瑶光LoRA_2035232923888132098
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/CommintAI：ZIB+Kook_瑶光LoRA_2035232923888132098.json
hash: 436f5adf5e0304cc
coverage: 0.804348
learned_at: 2026-10-21 02:51:29
nodes: [TTP_Image_Tile_Batch, SeedVR2LoadDiTModel, VAELoader, CLIPLoader, SeedVR2LoadVAEModel, CLIPTextEncode, EmptyLatentImage, FastFilmGrain, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, llama_cpp_model_loader, llama_cpp_parameters, GetImageSize+, ImageResize+, KSampler, Note, TTP_Image_Assy, SeedVR2VideoUpscaler, ImageScaleBy, TTP_Tile_image_size, ImageResize+, Reroute, GetImageSize+, SaveImage, Qwen3_VQA, Reroute, RunningHub Deepcleaner, ImageCASharpening+, VAEDecode, LoadImage, LoraLoaderModelOnly, LayerColor: BrightnessContrastV2, Note, ImageScaleBy, LoadImage, Note, easy showAnything, Reroute, SaveImage, LoadImage, SaveImage, ShowText|pysssss, llama_cpp_instruct_adv, ShowText|pysssss, MuyeSizeSelector]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 4649665467376, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/CommintAI：ZIB+Kook_瑶光LoRA_2035232923888132098.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/CommintAI：ZIB+Kook_瑶光LoRA_2035232923888132098.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadDiTModel`
- `VAELoader`
- `CLIPLoader`
- `SeedVR2LoadVAEModel`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `FastFilmGrain`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `GetImageSize+`
- `ImageResize+`
- `KSampler` ★核心
- `Note`
- `TTP_Image_Assy`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `ImageResize+`
- `Reroute`
- `GetImageSize+`
- `SaveImage`
- `Qwen3_VQA`
- `Reroute`
- `RunningHub Deepcleaner`
- `ImageCASharpening+`
- `VAEDecode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LayerColor: BrightnessContrastV2`
- `Note`
- `ImageScaleBy`
- `LoadImage`
- `Note`
- `easy showAnything`
- `Reroute`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `MuyeSizeSelector`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `4649665467376`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **80%**（37/46）

**有卡**：`TTP_Image_Tile_Batch`、`SeedVR2LoadDiTModel`、`VAELoader`、`CLIPLoader`、`SeedVR2LoadVAEModel`、`CLIPTextEncode`、`EmptyLatentImage`、`FastFilmGrain`、`LoraLoaderModelOnly`、`UNETLoader`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`GetImageSize+`、`ImageResize+`、`KSampler`、`TTP_Image_Assy`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`TTP_Tile_image_size`、`SaveImage`、`Qwen3_VQA`、`RunningHub Deepcleaner`、`ImageCASharpening+`、`VAEDecode`、`LoadImage`、`LayerColor: BrightnessContrastV2`、`llama_cpp_instruct_adv`、`MuyeSizeSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

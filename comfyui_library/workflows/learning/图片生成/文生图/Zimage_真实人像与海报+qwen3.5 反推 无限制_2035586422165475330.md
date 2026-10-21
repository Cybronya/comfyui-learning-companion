---
key: 图片生成/文生图/Zimage_真实人像与海报+qwen3.5 反推 无限制_2035586422165475330.json
name: Zimage_真实人像与海报+qwen3.5 反推 无限制_2035586422165475330
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage_真实人像与海报+qwen3.5 反推 无限制_2035586422165475330.json
hash: aadfacf26de5376f
coverage: 0.871795
learned_at: 2026-10-21 02:56:35
nodes: [LayerColor: BrightnessContrastV2, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, GetImageSize+, TTP_Tile_image_size, TTP_Image_Assy, ImageCASharpening+, ImageResize+, ImageResize+, ImageScaleBy, GetImageSize+, TTP_Image_Tile_Batch, ImageScaleBy, SaveImage, RunningHub Deepcleaner, FastFilmGrain, SeedVR2VideoUpscaler, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, KSampler, VAEDecode, CR Text, llama_cpp_parameters, llama_cpp_model_loader, Fast Groups Bypasser (rgthree), easy showAnything, llama_cpp_instruct_adv, CLIPTextEncode, SaveImage, CR Text, EmptyLatentImage, ImpactSwitch, Note, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 386606153260639, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Zimage_真实人像与海报+qwen3.5 反推 无限制_2035586422165475330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage_真实人像与海报+qwen3.5 反推 无限制_2035586422165475330.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LayerColor: BrightnessContrastV2`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `GetImageSize+`
- `TTP_Tile_image_size`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageResize+`
- `ImageScaleBy`
- `GetImageSize+`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `SaveImage`
- `RunningHub Deepcleaner`
- `FastFilmGrain`
- `SeedVR2VideoUpscaler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CR Text`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CR Text`
- `EmptyLatentImage` ★核心
- `ImpactSwitch`
- `Note`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `386606153260639`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`LayerColor: BrightnessContrastV2`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`GetImageSize+`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`ImageCASharpening+`、`ImageResize+`、`ImageScaleBy`、`TTP_Image_Tile_Batch`、`SaveImage`、`RunningHub Deepcleaner`、`FastFilmGrain`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`CR Text`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`EmptyLatentImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

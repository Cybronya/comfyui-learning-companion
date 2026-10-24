---
key: 图片生成/图生图/【最强全能洗图】Qwen3.5反推+Zimage混战_2035967073402232834.json
name: 【最强全能洗图】Qwen3.5反推+Zimage混战_2035967073402232834
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【最强全能洗图】Qwen3.5反推+Zimage混战_2035967073402232834.json
hash: aa8e615f89602097
coverage: 0.884058
learned_at: 2026-10-23 11:50:19
nodes: [CLIPTextEncode, CLIPLoaderGGUF, KSamplerAdvanced, UNETLoader, CLIPTextEncode, ModelSamplingAuraFlow, LoraLoaderModelOnly, KSampler, ModelSamplingAuraFlow, ModelSamplingAuraFlow, KSamplerAdvanced, Int, UNETLoader, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, Int, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, VAELoader, VAELoader, VAELoader, VAEDecode, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAEDecode, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, SaveImage, SaveImage, SeedVR2LoadVAEModel, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, SimpleComparison+, TTP_Image_Tile_Batch, SeedVR2VideoUpscaler, easy imageListToImageBatch, TTP_Image_Assy, easy imageBatchToImageList, SaveImage, LoadImage, Image Comparer (rgthree), LayerUtility: If , PreviewImage, SaveImage, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, llama_cpp_parameters, PreviewAny, FastFilmGrain, Note, Note, Note, llama_cpp_instruct_adv, llama_cpp_model_loader, Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, CLIPLoader, UNETLoader, LayerColor: BrightnessContrastV2, LoadImage, EmptyLatentImage, CR Text, CLIPLoaderGGUF]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 496230901315613, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【最强全能洗图】Qwen3.5反推+Zimage混战_2035967073402232834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【最强全能洗图】Qwen3.5反推+Zimage混战_2035967073402232834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoaderGGUF`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `Int`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `SaveImage`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `SimpleComparison+`
- `TTP_Image_Tile_Batch`
- `SeedVR2VideoUpscaler`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `easy imageBatchToImageList`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LayerUtility: If `
- `PreviewImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `llama_cpp_parameters`
- `PreviewAny`
- `FastFilmGrain`
- `Note`
- `Note`
- `Note`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LayerColor: BrightnessContrastV2`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `CR Text`
- `CLIPLoaderGGUF`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `496230901315613`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（61/69）

**有卡**：`CLIPTextEncode`、`CLIPLoaderGGUF`、`KSamplerAdvanced`、`UNETLoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`KSampler`、`Int`、`ConditioningZeroOut`、`VAELoader`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`SeedVR2LoadVAEModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`SimpleComparison+`、`TTP_Image_Tile_Batch`、`SeedVR2VideoUpscaler`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`easy imageBatchToImageList`、`LoadImage`、`LayerUtility: If `、`easy cleanGpuUsed`、`llama_cpp_parameters`、`FastFilmGrain`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`SeedVR2LoadDiTModel`、`CLIPLoader`、`LayerColor: BrightnessContrastV2`、`EmptyLatentImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

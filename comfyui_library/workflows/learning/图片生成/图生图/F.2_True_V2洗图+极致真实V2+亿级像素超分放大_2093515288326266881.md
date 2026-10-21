---
key: 图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093515288326266881.json
name: F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093515288326266881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093515288326266881.json
hash: 3303cfa0586d5a35
coverage: 0.825
learned_at: 2026-10-21 00:39:00
nodes: [EmptyFlux2LatentImage, CFGGuider, GetImageSize, SamplerCustomAdvanced, PrimitiveInt, KSamplerAdvanced, VAEDecode, ModelSamplingAuraFlow, PrimitiveInt, VAEEncode, ReferenceLatent, ConditioningZeroOut, VAEDecode, PreviewImage, ImageScaleToTotalPixels, easy getNode, Flux2Scheduler, ImageScaleBy, easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, CLIPTextEncode, easy setNode, easy setNode, easy getNode, easy getNode, easy imageSize, PreviewImage, ImageScaleBy, TTP_Tile_image_size, llama_cpp_parameters, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, llama_cpp_parameters, LayerUtility: PurgeVRAM, easy showAnything, SeedVR2LoadDiTModel, UNETLoader, UNETLoader, UNETLoader, CLIPLoader, VAELoader, VAELoader, EmptyLatentImage, CLIPLoader, easy showAnything, llama_cpp_instruct_adv, ImageResize+, PreviewImage, easy imageSize, KSamplerAdvanced, CR Text, llama_cpp_model_loader, llama_cpp_model_loader, llama_cpp_instruct_adv, LoadImage, MarkdownNote, Any Switch (rgthree), Fast Groups Bypasser (rgthree), SaveImage, ImageColorMatch+, Image Comparer (rgthree), CLIPTextEncode, LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ImageResize+, easy cleanGpuUsed, easy cleanGpuUsed, TTP_Image_Assy, Image Comparer (rgthree), PreviewImage, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, easy getNode, easy setNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 40, "denoise": "sgm_uniform", "height": 1536, "sampler_name": 4, "scheduler": "res_multistep", "seed": "enable", "steps": "randomize", "width": 864}
---

# 图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093515288326266881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2_True_V2洗图+极致真实V2+亿级像素超分放大_2093515288326266881.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `GetImageSize`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `easy getNode`
- `Flux2Scheduler`
- `ImageScaleBy`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `CLIPTextEncode` ★核心
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy imageSize`
- `PreviewImage`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `llama_cpp_parameters`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `llama_cpp_parameters`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `SeedVR2LoadDiTModel`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `ImageResize+`
- `PreviewImage`
- `easy imageSize`
- `KSamplerAdvanced` ★核心
- `CR Text`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `MarkdownNote`
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `ImageColorMatch+`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ImageResize+`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy setNode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `4`
- `scheduler` = `res_multistep`
- `denoise` = `sgm_uniform`
- `width` = `864`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（66/80）

**有卡**：`EmptyFlux2LatentImage`、`CFGGuider`、`GetImageSize`、`SamplerCustomAdvanced`、`KSamplerAdvanced`、`VAEDecode`、`ModelSamplingAuraFlow`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`easy getNode`、`Flux2Scheduler`、`ImageScaleBy`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`CLIPTextEncode`、`easy setNode`、`TTP_Tile_image_size`、`llama_cpp_parameters`、`SeedVR2LoadDiTModel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`llama_cpp_instruct_adv`、`ImageResize+`、`CR Text`、`llama_cpp_model_loader`、`LoadImage`、`SaveImage`、`ImageColorMatch+`、`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`easy cleanGpuUsed`、`TTP_Image_Assy`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

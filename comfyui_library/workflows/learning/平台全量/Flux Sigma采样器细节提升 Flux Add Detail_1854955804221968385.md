---
key: 平台全量/Flux Sigma采样器细节提升 Flux Add Detail_1854955804221968385.json
name: Flux Sigma采样器细节提升 Flux Add Detail_1854955804221968385
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Sigma采样器细节提升 Flux Add Detail_1854955804221968385.json
hash: 43a5116bcf1fb6f7
coverage: 0.818182
learned_at: 2026-11-14 00:28:05
nodes: [Seed_, RandomNoise, FluxGuidance, Reroute, BasicGuider, Reroute, VAEEncode, VAEDecodeTiled, TTP_Image_Tile_Batch, easy imageBatchToImageList, easy imageListToImageBatch, ImageScaleToTotalPixels, TTP_Tile_image_size, CLIPTextEncode, Reroute, LayerFilter: FilmV2, DepthAnythingV2Preprocessor, Reroute, UpscaleModelLoader, ImageUpscaleWithModel, KSamplerSelect, BasicScheduler, KSamplerSelect, EmptyLatentImage, VAELoader, PreviewImage, SamplerCustomAdvanced, TTP_Image_Assy, PreviewImage, VAEDecode, BasicScheduler, AdvancedLyingSigmaSampler, PreviewImage, CLIPTextEncode, UNETLoader, DualCLIPLoader, CLIPTextEncode, RH_Prompter, PreviewImage, CR Simple Image Compare, SaveImage, VAEDecode, SamplerCustom, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 883339040761268, "steps": 30, "width": 768}
---

# 平台全量/Flux Sigma采样器细节提升 Flux Add Detail_1854955804221968385.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Sigma采样器细节提升 Flux Add Detail_1854955804221968385.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `Seed_`
- `RandomNoise`
- `FluxGuidance`
- `Reroute`
- `BasicGuider`
- `Reroute`
- `VAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `CLIPTextEncode` ★核心
- `Reroute`
- `LayerFilter: FilmV2`
- `DepthAnythingV2Preprocessor`
- `Reroute`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `TTP_Image_Assy`
- `PreviewImage`
- `VAEDecode` ★核心
- `BasicScheduler`
- `AdvancedLyingSigmaSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `RH_Prompter`
- `PreviewImage`
- `CR Simple Image Compare`
- `SaveImage`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `883339040761268`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`Seed_`、`RandomNoise`、`FluxGuidance`、`BasicGuider`、`VAEEncode`、`VAEDecodeTiled`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`CLIPTextEncode`、`LayerFilter: FilmV2`、`DepthAnythingV2Preprocessor`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`KSamplerSelect`、`BasicScheduler`、`EmptyLatentImage`、`VAELoader`、`SamplerCustomAdvanced`、`TTP_Image_Assy`、`VAEDecode`、`AdvancedLyingSigmaSampler`、`UNETLoader`、`DualCLIPLoader`、`RH_Prompter`、`CR Simple Image Compare`、`SaveImage`、`SamplerCustom`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、DepthAnythingV2Preprocessor、AdvancedLyingSigmaSampler

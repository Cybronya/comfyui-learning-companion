---
key: 平台全量/Flux细节提升：Flux Add Detail & Realistic Skin_1868916738820816897.json
name: Flux细节提升：Flux Add Detail & Realistic Skin_1868916738820816897
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux细节提升：Flux Add Detail & Realistic Skin_1868916738820816897.json
hash: 083e26a84900d81b
coverage: 0.813953
learned_at: 2026-11-14 00:30:39
nodes: [Seed_, RandomNoise, FluxGuidance, Reroute, BasicGuider, Reroute, VAEEncode, VAEDecodeTiled, TTP_Image_Tile_Batch, easy imageBatchToImageList, easy imageListToImageBatch, ImageScaleToTotalPixels, TTP_Tile_image_size, CLIPTextEncode, Reroute, DepthAnythingV2Preprocessor, Reroute, UpscaleModelLoader, ImageUpscaleWithModel, KSamplerSelect, BasicScheduler, SamplerCustom, EmptyLatentImage, PreviewImage, PreviewImage, TTP_Image_Assy, PreviewImage, VAEDecode, VAEDecode, AdvancedLyingSigmaSampler, PreviewImage, KSampler, CLIPTextEncode, UNETLoader, DualCLIPLoader, BasicScheduler, KSamplerSelect, VAELoader, CR Simple Image Compare, SaveImage, SamplerCustomAdvanced, CLIPTextEncode, LayerFilter: FilmV2]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 359799774960949, "steps": 30, "width": 768}
---

# 平台全量/Flux细节提升：Flux Add Detail & Realistic Skin_1868916738820816897.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux细节提升：Flux Add Detail & Realistic Skin_1868916738820816897.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
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
- `DepthAnythingV2Preprocessor`
- `Reroute`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustom` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `PreviewImage`
- `TTP_Image_Assy`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `AdvancedLyingSigmaSampler` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CR Simple Image Compare`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LayerFilter: FilmV2`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `359799774960949`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`Seed_`、`RandomNoise`、`FluxGuidance`、`BasicGuider`、`VAEEncode`、`VAEDecodeTiled`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`CLIPTextEncode`、`DepthAnythingV2Preprocessor`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustom`、`EmptyLatentImage`、`TTP_Image_Assy`、`VAEDecode`、`AdvancedLyingSigmaSampler`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CR Simple Image Compare`、`SaveImage`、`SamplerCustomAdvanced`、`LayerFilter: FilmV2`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、DepthAnythingV2Preprocessor、AdvancedLyingSigmaSampler

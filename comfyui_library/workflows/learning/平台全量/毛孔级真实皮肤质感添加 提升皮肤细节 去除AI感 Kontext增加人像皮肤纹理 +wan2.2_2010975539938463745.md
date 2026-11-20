---
key: 平台全量/毛孔级真实皮肤质感添加 提升皮肤细节 去除AI感 Kontext增加人像皮肤纹理 +wan2.2_2010975539938463745.json
name: 毛孔级真实皮肤质感添加 提升皮肤细节 去除AI感 Kontext增加人像皮肤纹理 +wan2.2_2010975539938463745
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/毛孔级真实皮肤质感添加 提升皮肤细节 去除AI感 Kontext增加人像皮肤纹理 +wan2.2_2010975539938463745.json
hash: 6059677ec97557ad
coverage: 0.926829
learned_at: 2026-11-14 02:19:03
nodes: [VAEDecode, Image Comparer (rgthree), ConditioningZeroOut, CLIPTextEncode, VAELoader, KSampler, FluxKontextImageScale, CLIPLoader, KSampler, Float, MarkdownNote, VAEEncode, VAELoader, Image Comparer (rgthree), SaveImage, LoadImage, ImpactInt, VAEDecode, VAEEncode, ReferenceLatent, FluxGuidance, CLIPTextEncode, CLIPTextEncode, easy imageBatchToImageList, ImageListToImageBatch, TTP_Image_Tile_Batch, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, TTP_Image_Assy, ModelSamplingSD3, DualCLIPLoader, UpscaleModelLoader, UNETLoader, UNETLoader, SaveImage, LoraLoaderModelOnly, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "heun", "scheduler": "beta", "seed": 209429335161538, "steps": 10}
---

# 平台全量/毛孔级真实皮肤质感添加 提升皮肤细节 去除AI感 Kontext增加人像皮肤纹理 +wan2.2_2010975539938463745.json

> 来源文件 `comfyui_library/workflows/平台全量/毛孔级真实皮肤质感添加 提升皮肤细节 去除AI感 Kontext增加人像皮肤纹理 +wan2.2_2010975539938463745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `CLIPLoader`
- `KSampler` ★核心
- `Float`
- `MarkdownNote`
- `VAEEncode` ★核心
- `VAELoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `ImpactInt`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy imageBatchToImageList`
- `ImageListToImageBatch`
- `TTP_Image_Tile_Batch`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `TTP_Image_Assy`
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `209429335161538`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.1`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`KSampler`、`FluxKontextImageScale`、`CLIPLoader`、`Float`、`VAEEncode`、`SaveImage`、`LoadImage`、`ImpactInt`、`ReferenceLatent`、`FluxGuidance`、`easy imageBatchToImageList`、`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`TTP_Image_Assy`、`ModelSamplingSD3`、`DualCLIPLoader`、`UpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

---
key: 图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2068868548872728577.json
name: image2.0 后处理 去模糊放大，去ai感，合理细节_2068868548872728577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2068868548872728577.json
hash: 2398136aca9dc017
coverage: 0.865854
learned_at: 2026-10-23 11:37:44
nodes: [MathExpression|pysssss, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageBatchToImageList, ImageFromBatch, GetImageSize+, easy imageListToImageBatch, ImpactCompare, SeedVR2VideoUpscaler, MathExpression|pysssss, If ANY execute A else B, ImageResizeKJv2, GetImageSizeAndCount, ImageListToImageBatch, TTP_Image_Tile_Batch, MathExpression|pysssss, GetImageSizeAndCount, TTP_Tile_image_size, MathExpression|pysssss, ImpactImageBatchToImageList, ImageColorMatch+, Image Comparer (rgthree), GetImageSizeAndCount, ImageResizeKJv2, Upscale by Factor with Model (WLSH), RH_Captioner, ImageResize+, UNETLoader, TTP_Image_Assy, VAELoader, ImageResizeKJv2, Note, Note, CLIPLoader, ModelSamplingAuraFlow, VAEEncode, Image Comparer (rgthree), VAEDecode, KSamplerAdvanced, ImageResizeKJv2, ImageListToImageBatch, TTP_Image_Tile_Batch, MathExpression|pysssss, GetImageSizeAndCount, TTP_Tile_image_size, MathExpression|pysssss, ImageColorMatch+, GetImageSizeAndCount, ImageResizeKJv2, Upscale Model Loader, Upscale by Factor with Model (WLSH), TTP_Image_Assy, VAELoader, Note, VAEEncode, Switch any [Crystools], VAEDecode, ImageResizeKJv2, ImageResize+, ShowText|pysssss, ImageResize+, ImageResize+, TTP_Image_Assy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, CFGNorm, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, Switch any [Crystools], KSamplerAdvanced, Note, Note, Image Comparer (rgthree), Note, Note, Int, LoadImage, SaveImage, SaveImage, SaveImage, Upscale Model Loader]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "res_multistep", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2068868548872728577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2068868548872728577.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `MathExpression|pysssss`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `ImageFromBatch`
- `GetImageSize+`
- `easy imageListToImageBatch`
- `ImpactCompare`
- `SeedVR2VideoUpscaler`
- `MathExpression|pysssss`
- `If ANY execute A else B`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `ImageListToImageBatch`
- `TTP_Image_Tile_Batch`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `TTP_Tile_image_size`
- `MathExpression|pysssss`
- `ImpactImageBatchToImageList`
- `ImageColorMatch+`
- `Image Comparer (rgthree)`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `Upscale by Factor with Model (WLSH)`
- `RH_Captioner`
- `ImageResize+`
- `UNETLoader` ★核心
- `TTP_Image_Assy`
- `VAELoader`
- `ImageResizeKJv2`
- `Note`
- `Note`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `ImageListToImageBatch`
- `TTP_Image_Tile_Batch`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `TTP_Tile_image_size`
- `MathExpression|pysssss`
- `ImageColorMatch+`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `Upscale Model Loader`
- `Upscale by Factor with Model (WLSH)`
- `TTP_Image_Assy`
- `VAELoader`
- `Note`
- `VAEEncode` ★核心
- `Switch any [Crystools]`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `ImageResize+`
- `ShowText|pysssss`
- `ImageResize+`
- `ImageResize+`
- `TTP_Image_Assy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `CFGNorm`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactImageBatchToImageList`
- `Switch any [Crystools]`
- `KSamplerAdvanced` ★核心
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `Int`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Upscale Model Loader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `res_multistep`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **87%**（71/82）

**有卡**：`MathExpression|pysssss`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`ImageFromBatch`、`GetImageSize+`、`easy imageListToImageBatch`、`ImpactCompare`、`SeedVR2VideoUpscaler`、`If ANY execute A else B`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`ImageListToImageBatch`、`ImpactImageBatchToImageList`、`ImageColorMatch+`、`Upscale by Factor with Model (WLSH)`、`RH_Captioner`、`ImageResize+`、`UNETLoader`、`TTP_Image_Assy`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAEEncode`、`VAEDecode`、`KSamplerAdvanced`、`Upscale Model Loader`、`Switch any [Crystools]`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`CFGNorm`、`CLIPTextEncode`、`Int`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGNorm、KSamplerAdvanced

---
key: 平台全量/image2.0 去噪点+放大_2100263940218515458.json
name: image2.0 去噪点+放大_2100263940218515458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/image2.0 去噪点+放大_2100263940218515458.json
hash: 737741b715f54e96
coverage: 0.820513
learned_at: 2026-11-14 01:12:38
nodes: [ImageListToImageBatch, TTP_Image_Tile_Batch, MathExpression|pysssss, GetImageSizeAndCount, TTP_Tile_image_size, MathExpression|pysssss, ImpactImageBatchToImageList, ImageColorMatch+, Image Comparer (rgthree), GetImageSizeAndCount, ImageResizeKJv2, Upscale by Factor with Model (WLSH), RH_Captioner, ImageResize+, UNETLoader, TTP_Image_Assy, VAELoader, ImageResizeKJv2, Note, Note, CLIPLoader, ModelSamplingAuraFlow, VAEEncode, VAEDecode, KSamplerAdvanced, ImageResizeKJv2, ImageResize+, ShowText|pysssss, CFGNorm, CLIPTextEncode, CLIPTextEncode, Switch any [Crystools], Note, Note, Note, Int, SaveImage, LoadImage, Upscale Model Loader]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "res_multistep", "seed": "enable", "steps": "randomize"}
---

# 平台全量/image2.0 去噪点+放大_2100263940218515458.json

> 来源文件 `comfyui_library/workflows/平台全量/image2.0 去噪点+放大_2100263940218515458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
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
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `ImageResize+`
- `ShowText|pysssss`
- `CFGNorm`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Switch any [Crystools]`
- `Note`
- `Note`
- `Note`
- `Int`
- `SaveImage`
- `LoadImage`
- `Upscale Model Loader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `res_multistep`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`MathExpression|pysssss`、`GetImageSizeAndCount`、`TTP_Tile_image_size`、`ImpactImageBatchToImageList`、`ImageColorMatch+`、`ImageResizeKJv2`、`Upscale by Factor with Model (WLSH)`、`RH_Captioner`、`ImageResize+`、`UNETLoader`、`TTP_Image_Assy`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAEEncode`、`VAEDecode`、`KSamplerAdvanced`、`CFGNorm`、`CLIPTextEncode`、`Switch any [Crystools]`、`Int`、`SaveImage`、`LoadImage`、`Upscale Model Loader`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、CFGNorm、KSamplerAdvanced

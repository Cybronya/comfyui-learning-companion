---
key: 图片生成/图生图/Wan2.2最强单帧写实洗图工作流【可TTP放大】_1951485907062960130.json
name: Wan2.2最强单帧写实洗图工作流【可TTP放大】_1951485907062960130
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2最强单帧写实洗图工作流【可TTP放大】_1951485907062960130.json
hash: feef3a4a2d245885
coverage: 0.9
learned_at: 2026-10-23 11:28:23
nodes: [CLIPTextEncode, VAEEncode, CLIPTextEncode, ModelSamplingSD3, CLIPLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, CR Text Concatenate, RH_Captioner, LayerUtility: ImageReel, SaveImage, UNETLoader, UnetLoaderGGUF, LayerUtility: ImageScaleByAspectRatio V2, DF_Integer, PrimitiveFloat, MaxNode, PrimitiveFloat, PrimitiveFloat, MinNode, DualCLIPLoader, UNETLoader, UpscaleModelLoader, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAELoader, CLIPTextEncode, CLIPTextEncode, ImpactImageBatchToImageList, VAEEncode, KSampler, CR Simple Image Compare, SaveImage, TTP_Image_Assy, VAEDecodeTiled, ImageListToImageBatch, ImageUpscaleWithModel, SaveImage, VAEDecode, LoadImage, PrimitiveStringMultiline, CR Simple Image Compare, LayerUtility: ImageReelComposit, SaveImage, KSampler, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 954994834171506, "steps": 12}
---

# 图片生成/图生图/Wan2.2最强单帧写实洗图工作流【可TTP放大】_1951485907062960130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2最强单帧写实洗图工作流【可TTP放大】_1951485907062960130.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CR Text Concatenate`
- `RH_Captioner`
- `LayerUtility: ImageReel`
- `SaveImage`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DF_Integer`
- `PrimitiveFloat`
- `MaxNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `MinNode`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactImageBatchToImageList`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `CR Simple Image Compare`
- `SaveImage`
- `TTP_Image_Assy`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `CR Simple Image Compare`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `954994834171506`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **90%**（45/50）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`ModelSamplingSD3`、`CLIPLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CR Text Concatenate`、`RH_Captioner`、`LayerUtility: ImageReel`、`SaveImage`、`UNETLoader`、`UnetLoaderGGUF`、`LayerUtility: ImageScaleByAspectRatio V2`、`DF_Integer`、`MaxNode`、`MinNode`、`DualCLIPLoader`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImpactImageBatchToImageList`、`KSampler`、`CR Simple Image Compare`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`VAEDecode`、`LoadImage`、`LayerUtility: ImageReelComposit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

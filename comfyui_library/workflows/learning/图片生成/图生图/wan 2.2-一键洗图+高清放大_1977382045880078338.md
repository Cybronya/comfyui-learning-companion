---
key: 图片生成/图生图/wan 2.2-一键洗图+高清放大_1977382045880078338.json
name: wan 2.2-一键洗图+高清放大_1977382045880078338
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan 2.2-一键洗图+高清放大_1977382045880078338.json
hash: 8699bda8ef9a7e02
coverage: 0.671429
learned_at: 2026-10-23 11:45:48
nodes: [SetNode, SetNode, LayerUtility: PurgeVRAM, Image Comparer (rgthree), PathchSageAttentionKJ, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, ModelSamplingSD3, VAELoader, CLIPLoader, Anything Everywhere3, CLIPTextEncode, GetNode, CLIPTextEncode, SetNode, SetNode, GetNode, CR Seed, VAEDecode, ModelSamplingSD3, SetNode, GetNode, GetNode, GetNode, SetNode, PreviewImage, GetNode, GetNode, KSampler, ImpactInt, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, KSampler, VAEEncode, LoadImage, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageBatchToImageList, VAEEncode, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, Image Comparer (rgthree), easy imageListToImageBatch, UNETLoader, LoraLoaderModelOnly, UpscaleModelLoader, ImageUpscaleWithModel, Image Comparer (rgthree), ImageSmartSharpen+, KSampler, VAEDecodeTiled, ResizeLongestToNode, Anything Everywhere, DualCLIPLoader, VAELoader, GetNode, RH_LLMAPI_NODE, SaveImage, TTP_Image_Assy, Fast Groups Bypasser (rgthree), VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 328338393162286, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan 2.2-一键洗图+高清放大_1977382045880078338.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan 2.2-一键洗图+高清放大_1977382045880078338.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `Image Comparer (rgthree)`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `CR Seed`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `easy imageListToImageBatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Image Comparer (rgthree)`
- `ImageSmartSharpen+`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `ResizeLongestToNode`
- `Anything Everywhere`
- `DualCLIPLoader`
- `VAELoader`
- `GetNode`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `TTP_Image_Assy`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `328338393162286`
- `steps` = `4`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **67%**（47/70）

**有卡**：`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`CR Seed`、`VAEDecode`、`KSampler`、`ImpactInt`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEEncode`、`LoadImage`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageSmartSharpen+`、`VAEDecodeTiled`、`ResizeLongestToNode`、`DualCLIPLoader`、`RH_LLMAPI_NODE`、`SaveImage`、`TTP_Image_Assy`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

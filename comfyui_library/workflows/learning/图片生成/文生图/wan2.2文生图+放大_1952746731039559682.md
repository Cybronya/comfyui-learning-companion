---
key: wan2.2文生图+放大_1952746731039559682.json
name: wan2.2文生图+放大_1952746731039559682
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图+放大_1952746731039559682.json
hash: 1f712ee68ac9aacf
coverage: 0.705882
learned_at: 2026-10-10 20:59:27
nodes: [easy imageInsetCrop, Constant Number, CLIPTextEncode, ImageListToImageBatch, CLIPTextEncode, ShowText|pysssss, VAEEncode, LayerUtility: PurgeVRAM, VAEDecode, PathchSageAttentionKJ, CLIPLoader, VAELoader, ShowText|pysssss, ModelSamplingSD3, TTP_Image_Tile_Batch, ImageScaleBy, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, InjectLatentNoise+, TTP_Tile_image_size, KSamplerAdvanced, KSamplerAdvanced, EmptyHunyuanLatentVideo, PreviewImage, Note, DeepTranslatorTextNode, LoraLoaderModelOnly, LoraLoaderModelOnly, Qwen2.5VL, LoadImage, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, LayerUtility: Florence2Image2Prompt, LayerMask: LoadFlorence2Model, LoraLoaderModelOnly, LoraLoaderModelOnly, UpscaleModelLoader, PreviewImage, TTP_Image_Assy, SaveImage]
patterns: [image_to_image]
missing: [Constant Number, LayerMask: LoadFlorence2Model, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Qwen2.5VL, easy imageBatchToImageList, easy imageInsetCrop, InjectLatentNoise+, LayerUtility: Florence2Image2Prompt]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "bong_tangent", "seed": 752200592380295, "steps": 10}
discoveries: [次要节点 `Constant Number` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `Qwen2.5VL` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageInsetCrop` 知识库中没有该节点类型的任何知识, 次要节点 `InjectLatentNoise+` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `LayerUtility: Florence2Image2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# wan2.2文生图+放大_1952746731039559682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图+放大_1952746731039559682.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `easy imageInsetCrop`
- `Constant Number`
- `CLIPTextEncode` ★核心
- `ImageListToImageBatch`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `ShowText|pysssss`
- `ModelSamplingSD3`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `easy imageBatchToImageList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `InjectLatentNoise+`
- `TTP_Tile_image_size`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `PreviewImage`
- `Note`
- `DeepTranslatorTextNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Qwen2.5VL`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LayerUtility: Florence2Image2Prompt`
- `LayerMask: LoadFlorence2Model`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `PreviewImage`
- `TTP_Image_Assy`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `752200592380295`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `bong_tangent`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **71%**（36/51）

**有卡**：`CLIPTextEncode`、`ImageListToImageBatch`、`VAEEncode`、`VAEDecode`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`TTP_Tile_image_size`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`DeepTranslatorTextNode`、`LoadImage`、`UNETLoader`、`KSampler`、`UpscaleModelLoader`、`TTP_Image_Assy`、`SaveImage`

**缺卡**（10）：`Constant Number`、`LayerMask: LoadFlorence2Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`Qwen2.5VL`、`easy imageBatchToImageList`、`easy imageInsetCrop`、`InjectLatentNoise+`、`LayerUtility: Florence2Image2Prompt`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `Constant Number` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `Qwen2.5VL` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageInsetCrop` 知识库中没有该节点类型的任何知识
- 次要节点 `InjectLatentNoise+` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `LayerUtility: Florence2Image2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

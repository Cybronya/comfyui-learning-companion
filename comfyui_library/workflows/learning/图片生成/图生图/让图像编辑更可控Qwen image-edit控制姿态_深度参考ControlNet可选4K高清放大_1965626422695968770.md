---
key: 图片生成/图生图/让图像编辑更可控Qwen image-edit控制姿态_深度参考ControlNet可选4K高清放大_1965626422695968770.json
name: 让图像编辑更可控Qwen image-edit控制姿态_深度参考ControlNet可选4K高清放大_1965626422695968770
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/让图像编辑更可控Qwen image-edit控制姿态_深度参考ControlNet可选4K高清放大_1965626422695968770.json
hash: 03ce0cc66e9d1511
coverage: 0.815385
learned_at: 2026-10-23 13:27:36
nodes: [LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, CR Text, LoadImage, CLIPLoader, VAELoader, TextEncodeQwenImageEdit, SaveImage, ConditioningZeroOut, ImageListToBatch+, CLIPTextEncode, ReferenceLatent, FluxGuidance, DF_Integer, Note, LayerUtility: Seed, ImpactImageBatchToImageList, TeaCache, VAEEncode, VAEDecode, KSampler, TTP_Image_Tile_Batch, TTP_Tile_image_size, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, Reroute, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: ColorAdapter, Image Comparer (rgthree), Image Comparer (rgthree), Anything Everywhere3, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, AIO_Preprocessor, FluxKontextImageScale, TTP_Image_Assy, FluxKontextImageScale, easy cleanGpuUsed, easy clearCacheAll, SetUnionControlNetType, ControlNetLoader, easy imageSize, LoadImage, SaveImage, DF_Integer, DualCLIPLoader, CLIPTextEncode, CFGNorm, ControlNetApplyAdvanced, EmptyLatentImage, Note, KSampler, LayerUtility: PurgeVRAM V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, CR Text, LoadImage, CLIPLoader, VAELoader, TextEncodeQwenImageEdit, SaveImage, ConditioningZeroOut, ImageListToBatch+, CLIPTextEncode, ReferenceLatent, FluxGuidance, DF_Integer, Note, LayerUtility: Seed, ImpactImageBatchToImageList, TeaCache, VAEEncode, VAEDecode, KSampler, TTP_Image_Tile_Batch, TTP_Tile_image_size, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, MarkdownNote, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), Image Comparer (rgthree), Anything Everywhere3, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, FluxKontextImageScale, TTP_Image_Assy, FluxKontextImageScale, easy cleanGpuUsed, easy clearCacheAll, SetUnionControlNetType, ControlNetLoader, easy imageSize, LoadImage, DualCLIPLoader, CLIPTextEncode, CFGNorm, ControlNetApplyAdvanced, EmptyLatentImage, Note, KSampler, LayerUtility: PurgeVRAM V2, AIO_Preprocessor, PreviewImage, VAEDecode, VAEDecode, LayerColor: ColorAdapter, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), MarkdownNote, Fast Groups Bypasser (rgthree), RHHiddenNodes, DF_Integer, RHHiddenNodes, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1.5000000000000002, "denoise": 1, "height": 1376, "sampler_name": "euler", "scheduler": "simple", "seed": 1060199130247674, "steps": 6, "width": 824}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/让图像编辑更可控Qwen image-edit控制姿态_深度参考ControlNet可选4K高清放大_1965626422695968770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/让图像编辑更可控Qwen image-edit控制姿态_深度参考ControlNet可选4K高清放大_1965626422695968770.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（130 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `CR Text`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEdit`
- `SaveImage`
- `ConditioningZeroOut`
- `ImageListToBatch+`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `DF_Integer`
- `Note`
- `LayerUtility: Seed`
- `ImpactImageBatchToImageList`
- `TeaCache`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: ColorAdapter`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `AIO_Preprocessor`
- `FluxKontextImageScale`
- `TTP_Image_Assy`
- `FluxKontextImageScale`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `easy imageSize`
- `LoadImage`
- `SaveImage`
- `DF_Integer`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `ControlNetApplyAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `CR Text`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEdit`
- `SaveImage`
- `ConditioningZeroOut`
- `ImageListToBatch+`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `DF_Integer`
- `Note`
- `LayerUtility: Seed`
- `ImpactImageBatchToImageList`
- `TeaCache`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `MarkdownNote`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `FluxKontextImageScale`
- `TTP_Image_Assy`
- `FluxKontextImageScale`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `easy imageSize`
- `LoadImage`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `ControlNetApplyAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerColor: ColorAdapter`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `RHHiddenNodes`
- `DF_Integer`
- `RHHiddenNodes`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `1060199130247674`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.5000000000000002`
- `width` = `824`
- `height` = `1376`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（106/130）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`LoadImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEdit`、`SaveImage`、`ConditioningZeroOut`、`ImageListToBatch+`、`CLIPTextEncode`、`ReferenceLatent`、`FluxGuidance`、`DF_Integer`、`LayerUtility: Seed`、`ImpactImageBatchToImageList`、`TeaCache`、`VAEEncode`、`VAEDecode`、`KSampler`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerColor: ColorAdapter`、`ModelSamplingAuraFlow`、`AIO_Preprocessor`、`FluxKontextImageScale`、`TTP_Image_Assy`、`easy cleanGpuUsed`、`easy clearCacheAll`、`SetUnionControlNetType`、`ControlNetLoader`、`easy imageSize`、`DualCLIPLoader`、`CFGNorm`、`ControlNetApplyAdvanced`、`EmptyLatentImage`、`LayerUtility: PurgeVRAM V2`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

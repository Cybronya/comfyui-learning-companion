---
key: 图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json
name: Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json
hash: 5944ad5a7c89b6f1
coverage: 0.586957
learned_at: 2026-10-06 21:41:11
nodes: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SetNode, UNETLoader, QwenImage21Cache, CLIPLoader, CLIPLoader, CLIPLoader, VAELoader, PreviewImage, SaveImage, Anything Everywhere3, SetNode, LoadImage, LoadImage, CR Prompt Text, ResolutionSelector, BatchImagesNode, GetNode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, PreviewAny, EmptyLatentImage, ComfySwitchNode, VAEDecode, LoraLoaderModelOnly, KSampler, SetNode, Fast Groups Bypasser (rgthree), easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, Image Comparer (rgthree), TTP_Image_Assy, Image Comparer (rgthree), GetNode, TTP_Tile_image_size, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [BatchImagesNode, Fast Groups Bypasser (rgthree), ImageScaleBy, ImageScaleBy, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, TTP_Image_Assy, TTP_Image_Tile_Batch, CR Prompt Text, ImageResize+, ImageResize+, PreviewAny, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Tile_image_size, TextGenerateLTX2Prompt, easy imageSize, easy imageSize, easy imageSize, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `TTP_Image_Assy` 知识库中没有该节点类型的任何知识, 次要节点 `TTP_Image_Tile_Batch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `TTP_Tile_image_size` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物换姿势｜服装模特姿势复刻，摆拍角度随心控_2107360567005634561.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SetNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `SaveImage`
- `Anything Everywhere3`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `ResolutionSelector`
- `BatchImagesNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `ImageResize+`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `ImageResize+`
- `PreviewImage`
- `easy imageSize`
- `easy imageSize`
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `GetNode`
- `TTP_Tile_image_size`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **59%**（54/92）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`

**缺卡**（22）：`BatchImagesNode`、`Fast Groups Bypasser (rgthree)`、`ImageScaleBy`、`ImageScaleBy`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`CR Prompt Text`、`ImageResize+`、`ImageResize+`、`PreviewAny`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TTP_Tile_image_size`、`TextGenerateLTX2Prompt`、`easy imageSize`、`easy imageSize`、`easy imageSize`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `TTP_Image_Assy` 知识库中没有该节点类型的任何知识
- 次要节点 `TTP_Image_Tile_Batch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `TTP_Tile_image_size` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

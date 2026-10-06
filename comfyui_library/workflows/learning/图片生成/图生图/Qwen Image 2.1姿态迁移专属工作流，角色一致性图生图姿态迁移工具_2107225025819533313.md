---
key: 图片生成/图生图/Qwen Image 2.1姿态迁移专属工作流，角色一致性图生图姿态迁移工具_2107225025819533313.json
name: Qwen Image 2.1姿态迁移专属工作流，角色一致性图生图姿态迁移工具_2107225025819533313
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1姿态迁移专属工作流，角色一致性图生图姿态迁移工具_2107225025819533313.json
hash: 2287ac92f88435c1
coverage: 0.581633
learned_at: 2026-10-07 02:41:24
nodes: [SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PixaromaGroupSwitch, ResolutionSelector, EmptyLatentImage, GetNode, GetNode, KSampler, CR Prompt Text, ShowText|pysssss, VRAM_Debug, TextEncodeQwenImage21, GetNode, PreviewImage, SetNode, easy showAnything, easy showAnything, CM_NumberToInt, GetImageSize, LayerUtility: ImageScaleRestore, easy imageSize, easy imageSize, LayerUtility: ImageScaleByAspectRatio V2, ImageCASharpening+, ttN concat, SetNode, GetNode, SetNode, GetNode, GetNode, ttN concat, PixaromaGroupSwitch, VAEDecode, SaveImage, PixaromaGroupSwitch, GetNode, GetNode, QwenPERewriteT8, LoadImage, DWPreprocessor, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, ImageRGBA2RGB, ImageResize+, LayerUtility: NumberCalculatorV2, TTP_Tile_image_size, ImageScaleBy, GetImageSize, CM_NumberBinaryOperation, LayerUtility: NumberCalculatorV2, easy imageSize, ImageCASharpening+, ImageResize+, TTP_Image_Assy, CR Prompt Text, PathchSageAttentionKJ, QwenImage21Cache, ModelAttentionBackend, TTP_Image_Tile_Batch, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LoadImage, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CM_NumberBinaryOperation, CM_NumberToInt, ImageCASharpening+, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore, LayerUtility: NumberCalculatorV2, LayerUtility: NumberCalculatorV2, ttN concat, ttN concat, CR Prompt Text, CR Prompt Text, CR Prompt Text, ImageResize+, ImageResize+, easy imageSize, easy imageSize, easy imageSize]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CM_NumberBinaryOperation` 知识库中没有该节点类型的任何知识, 次要节点 `CM_NumberToInt` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleRestore` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1姿态迁移专属工作流，角色一致性图生图姿态迁移工具_2107225025819533313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1姿态迁移专属工作流，角色一致性图生图姿态迁移工具_2107225025819533313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PixaromaGroupSwitch`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `CR Prompt Text`
- `ShowText|pysssss`
- `VRAM_Debug`
- `TextEncodeQwenImage21`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `CM_NumberToInt`
- `GetImageSize`
- `LayerUtility: ImageScaleRestore`
- `easy imageSize`
- `easy imageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCASharpening+`
- `ttN concat`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ttN concat`
- `PixaromaGroupSwitch`
- `VAEDecode` ★核心
- `SaveImage`
- `PixaromaGroupSwitch`
- `GetNode`
- `GetNode`
- `QwenPERewriteT8`
- `LoadImage`
- `DWPreprocessor`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ImageRGBA2RGB`
- `ImageResize+`
- `LayerUtility: NumberCalculatorV2`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `GetImageSize`
- `CM_NumberBinaryOperation`
- `LayerUtility: NumberCalculatorV2`
- `easy imageSize`
- `ImageCASharpening+`
- `ImageResize+`
- `TTP_Image_Assy`
- `CR Prompt Text`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `TTP_Image_Tile_Batch`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **58%**（57/98）

**有卡**：`PixaromaGroupSwitch`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`VRAM_Debug`、`TextEncodeQwenImage21`、`GetImageSize`、`VAEDecode`、`SaveImage`、`QwenPERewriteT8`、`LoadImage`、`DWPreprocessor`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ImageRGBA2RGB`、`TTP_Tile_image_size`、`ImageScaleBy`、`TTP_Image_Assy`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`ModelAttentionBackend`、`TTP_Image_Tile_Batch`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（20）：`CM_NumberBinaryOperation`、`CM_NumberToInt`、`ImageCASharpening+`、`ImageCASharpening+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleRestore`、`LayerUtility: NumberCalculatorV2`、`LayerUtility: NumberCalculatorV2`、`ttN concat`、`ttN concat`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`ImageResize+`、`ImageResize+`、`easy imageSize`、`easy imageSize`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CM_NumberBinaryOperation` 知识库中没有该节点类型的任何知识
- 次要节点 `CM_NumberToInt` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleRestore` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

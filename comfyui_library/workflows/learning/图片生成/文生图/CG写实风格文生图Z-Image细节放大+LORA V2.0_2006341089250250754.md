---
key: 图片生成/文生图/CG写实风格文生图Z-Image细节放大+LORA V2.0_2006341089250250754.json
name: CG写实风格文生图Z-Image细节放大+LORA V2.0_2006341089250250754
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/CG写实风格文生图Z-Image细节放大+LORA V2.0_2006341089250250754.json
hash: 611a32ed65ff08d9
coverage: 0.790698
learned_at: 2026-10-19 22:00:27
nodes: [CLIPLoader, VAELoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, KSampler, GetImageSize+, SeedVR2LoadDiTModel, ImageResize+, GetImageSize+, TTP_Image_Tile_Batch, ImageScaleBy, TTP_Tile_image_size, TTP_Image_Assy, VAEDecode, DuckHideNode, Note, DuckHideNode, PreviewImage, Int, Int, PrimitiveBoolean, PrimitiveBoolean, easy ifElse, SaveImage, Image Compare (mtb), PreviewImage, Note, ZML_SaveImage, SaveImage, RH_LLMAPI_NODE, ZML_AnyTypeSwitchFiveBoolean, UNETLoader, ConditioningZeroOut, CLIPTextEncode, PreviewAny, EmptyLatentImage, LoraLoaderModelOnly, Note, Note, JjkText, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 965990729365971, "steps": 9, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/CG写实风格文生图Z-Image细节放大+LORA V2.0_2006341089250250754.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/CG写实风格文生图Z-Image细节放大+LORA V2.0_2006341089250250754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `KSampler` ★核心
- `GetImageSize+`
- `SeedVR2LoadDiTModel`
- `ImageResize+`
- `GetImageSize+`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `TTP_Image_Assy`
- `VAEDecode` ★核心
- `DuckHideNode`
- `Note`
- `DuckHideNode`
- `PreviewImage`
- `Int`
- `Int`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `easy ifElse`
- `SaveImage`
- `Image Compare (mtb)`
- `PreviewImage`
- `Note`
- `ZML_SaveImage`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `ZML_AnyTypeSwitchFiveBoolean`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `JjkText`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `965990729365971`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（34/43）

**有卡**：`CLIPLoader`、`VAELoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`ImageResize+`、`KSampler`、`GetImageSize+`、`SeedVR2LoadDiTModel`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`VAEDecode`、`DuckHideNode`、`Int`、`PrimitiveBoolean`、`SaveImage`、`Image Compare (mtb)`、`ZML_SaveImage`、`RH_LLMAPI_NODE`、`ZML_AnyTypeSwitchFiveBoolean`、`UNETLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`EmptyLatentImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

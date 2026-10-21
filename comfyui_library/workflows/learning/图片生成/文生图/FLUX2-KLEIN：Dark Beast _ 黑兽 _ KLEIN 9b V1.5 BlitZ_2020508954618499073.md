---
key: 图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1.5 BlitZ_2020508954618499073.json
name: FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1.5 BlitZ_2020508954618499073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1.5 BlitZ_2020508954618499073.json
hash: 6dc9be71e5d43778
coverage: 0.928571
learned_at: 2026-10-19 22:29:38
nodes: [VAELoader, ProcessString, Text Concatenate, JDCN_StringToList, CR Text, CR Prompt Text, easy showAnything, RH_LLMAPI_Pro_Node, CR Prompt Text, CR Text Replace, UNETLoader, KSampler, ImageResize+, ImageResize+, GetImageSize+, PreviewImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, VAEDecode, LayerUtility: PurgeVRAM, easy cleanGpuUsed, TTP_Tile_image_size, Note, TTP_Image_Tile_Batch, ImageScaleBy, SeedVR2VideoUpscaler, GetImageSize+, TTP_Image_Assy, ImageCASharpening+, MuyeSizeSelector, SaveImage, CLIPLoader, LoadImage, CLIPTextEncode, LoadImage, CR Prompt Text, CR Prompt Text, CR Text Input Switch (4 way), LoadImage, CR Prompt Text, CR Prompt Text, LoadImage, CR Prompt Text, easy textSwitch, CLIPTextEncode, Note, LoadImage, CR Prompt Text, EmptyFlux2LatentImage, LoadImage, CR Prompt Text, SaveImage, CR Prompt Text, CR Text Input Switch (4 way), LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 710017032369910, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1.5 BlitZ_2020508954618499073.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX2-KLEIN：Dark Beast _ 黑兽 _ KLEIN 9b V1.5 BlitZ_2020508954618499073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `VAELoader`
- `ProcessString`
- `Text Concatenate`
- `JDCN_StringToList`
- `CR Text`
- `CR Prompt Text`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `CR Text Replace`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ImageResize+`
- `ImageResize+`
- `GetImageSize+`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `TTP_Tile_image_size`
- `Note`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `GetImageSize+`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `MuyeSizeSelector`
- `SaveImage`
- `CLIPLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Text Input Switch (4 way)`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`
- `easy textSwitch`
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
- `LoadImage`
- `CR Prompt Text`
- `SaveImage`
- `CR Prompt Text`
- `CR Text Input Switch (4 way)`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `710017032369910`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（52/56）

**有卡**：`VAELoader`、`ProcessString`、`Text Concatenate`、`JDCN_StringToList`、`CR Text`、`CR Prompt Text`、`RH_LLMAPI_Pro_Node`、`CR Text Replace`、`UNETLoader`、`KSampler`、`ImageResize+`、`GetImageSize+`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`TTP_Image_Assy`、`ImageCASharpening+`、`MuyeSizeSelector`、`SaveImage`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`、`CR Text Input Switch (4 way)`、`easy textSwitch`、`EmptyFlux2LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

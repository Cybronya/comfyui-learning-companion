---
key: 图片生成/图生图/全能图片Gimage2.0_全能图片_即梦、反推提示词、高清放大_2058909481295237121.json
name: 全能图片Gimage2.0_全能图片_即梦、反推提示词、高清放大_2058909481295237121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能图片Gimage2.0_全能图片_即梦、反推提示词、高清放大_2058909481295237121.json
hash: 1f554c2ccac11ef8
coverage: 0.590909
learned_at: 2026-10-23 12:16:07
nodes: [PreviewImage, PreviewImage, PreviewImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, CR Prompt Text, llama_cpp_model_loader, llama_cpp_instruct_adv, easy saveText, PreviewAny, LoadImage, PreviewImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Note, ImageResize+, SimpleMath+, easy cleanGpuUsed, ImpactMinMax, Get Image Size, ImageCASharpening+, ImageResize+, TTP_Image_Tile_Batch, TTP_Image_Assy, ImageCASharpening+, DF_Integer, SeedVR2, DF_Integer, Image Comparer (rgthree), Note, Note, SaveImage, LoadImage, Note, 忽略多组孤海, Note, Note, RH_BytedanceJimeng46ImageToImage, GetImageSize, PreviewImage, RH_Jimeng4_Image2Image, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, RH_Nano_Banana2_Gemini31Flash, RH_RhartImageG2ImageToImage, SaveImage, PrimitiveNode, PrimitiveNode, Note, PrimitiveNode, PrimitiveNode, PrimitiveNode, RH_RhartImageG2OfficialImageToImage]
patterns: []
missing: []
---

# 图片生成/图生图/全能图片Gimage2.0_全能图片_即梦、反推提示词、高清放大_2058909481295237121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全能图片Gimage2.0_全能图片_即梦、反推提示词、高清放大_2058909481295237121.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（66 个）：
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `CR Prompt Text`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `PreviewAny`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `ImageResize+`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `ImpactMinMax`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `DF_Integer`
- `SeedVR2`
- `DF_Integer`
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `SaveImage`
- `LoadImage`
- `Note`
- `忽略多组孤海`
- `Note`
- `Note`
- `RH_BytedanceJimeng46ImageToImage`
- `GetImageSize`
- `PreviewImage`
- `RH_Jimeng4_Image2Image`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `RH_Nano_Banana2_Gemini31Flash`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `RH_RhartImageG2OfficialImageToImage`

## 知识

覆盖率 **59%**（39/66）

**有卡**：`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy saveText`、`ImageResize+`、`SimpleMath+`、`easy cleanGpuUsed`、`ImpactMinMax`、`Get Image Size`、`ImageCASharpening+`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`DF_Integer`、`SeedVR2`、`SaveImage`、`忽略多组孤海`、`RH_BytedanceJimeng46ImageToImage`、`GetImageSize`、`RH_Jimeng4_Image2Image`、`RH_Nano_Banana2_Gemini31Flash`、`RH_RhartImageG2ImageToImage`、`RH_RhartImageG2OfficialImageToImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、SeedVR2、CR Prompt Text、GetImageSize、GetImageSize、Get Image Size、ImageResize+

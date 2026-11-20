---
key: 平台全量/firered-image-edit-1.1-电商内衣模特图生成：方案三_2042462258244100098.json
name: firered-image-edit-1.1-电商内衣模特图生成：方案三_2042462258244100098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/firered-image-edit-1.1-电商内衣模特图生成：方案三_2042462258244100098.json
hash: 209e5c94e8f7ee91
coverage: 0.821138
learned_at: 2026-11-14 01:10:25
nodes: [CLIPLoader, ReferenceLatent, VAEEncode, VAELoader, easy cleanGpuUsed, PreviewImage, KSamplerSelect, VAEEncode, ConditioningZeroOut, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, AILab_QwenVL, UNETLoader, KSamplerSelect, ModelSamplingAuraFlow, ImageScaleToTotalPixelsX, VAEEncode, SamplerCustom, KSamplerSelect, VAEDecode, Image Comparer (rgthree), CLIPTextEncode, BasicScheduler, DetailDaemonSamplerNode, Reroute, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixelsX, PreviewImage, DetailDaemonSamplerNode, BasicScheduler, LoadImage, ImageScaleToTotalPixelsX, easy cleanGpuUsed, ShowText|pysssss, DetailDaemonSamplerNode, SamplerCustom, VAEEncode, LatentColorMatchSimple, VAEDecode, SplitSigmas, CLIPTextEncode, AIO_Preprocessor, easy imageSizeBySide, KSamplerSelect, ZImageFunControlnet, PreviewImage, BasicScheduler, SamplerCustom, ModelPatchLoader, VAEDecode, easy cleanGpuUsed, VAELoader_Any, CLIPLoader_Any, ModelSamplingAuraFlow, easy cleanGpuUsed, PreviewImage, ImageScaleToTotalPixelsX, Seed (rgthree), PrimitiveNode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Seed (rgthree), UNETLoader, DetailDaemonSamplerNode, AILab_QwenVL, PrimitiveNode, PrimitiveNode, PreviewImage, PreviewImage, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, Fast Groups Bypasser (rgthree), SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, BasicScheduler, SamplerCustom, ProcessString, ProcessString, TextEncodeQwenImageEditPlus, JDCN_StringToList, easy cleanGpuUsed, LoraLoaderModelOnly, UNETLoader, CFGNorm, CLIPLoader, VAELoader, VAEDecode, LoadImage, LoadImage, VAEDecode, easy cleanGpuUsed, ImageScaleToTotalPixelsX, TextEncodeQwenImageEditPlus, Note, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveNode, SamplerCustom, Note, PrimitiveNode, CR Text, PreviewImage, VAEEncode, CR Text, easy promptReplace, easy cleanGpuUsed, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, ImageColorMatch+, PrimitiveNode, Seed (rgthree), LoadImage, AILab_QwenVL, SaveImage, ShowText|pysssss, Seed (rgthree), CR Text, SaveImage]
patterns: []
missing: []
---

# 平台全量/firered-image-edit-1.1-电商内衣模特图生成：方案三_2042462258244100098.json

> 来源文件 `comfyui_library/workflows/平台全量/firered-image-edit-1.1-电商内衣模特图生成：方案三_2042462258244100098.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（123 个）：
- `CLIPLoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `PreviewImage`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `AILab_QwenVL`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixelsX`
- `VAEEncode` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `DetailDaemonSamplerNode` ★核心
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixelsX`
- `PreviewImage`
- `DetailDaemonSamplerNode` ★核心
- `BasicScheduler`
- `LoadImage`
- `ImageScaleToTotalPixelsX`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `DetailDaemonSamplerNode` ★核心
- `SamplerCustom` ★核心
- `VAEEncode` ★核心
- `LatentColorMatchSimple`
- `VAEDecode` ★核心
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `easy imageSizeBySide`
- `KSamplerSelect` ★核心
- `ZImageFunControlnet`
- `PreviewImage`
- `BasicScheduler`
- `SamplerCustom` ★核心
- `ModelPatchLoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAELoader_Any`
- `CLIPLoader_Any`
- `ModelSamplingAuraFlow`
- `easy cleanGpuUsed`
- `PreviewImage`
- `ImageScaleToTotalPixelsX`
- `Seed (rgthree)`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `DetailDaemonSamplerNode` ★核心
- `AILab_QwenVL`
- `PrimitiveNode`
- `PrimitiveNode`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `BasicScheduler`
- `SamplerCustom` ★核心
- `ProcessString`
- `ProcessString`
- `TextEncodeQwenImageEditPlus`
- `JDCN_StringToList`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CFGNorm`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixelsX`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `ImageScaleToTotalPixelsX`
- `ImageScaleToTotalPixelsX`
- `ImageScaleToTotalPixelsX`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveNode`
- `SamplerCustom` ★核心
- `Note`
- `PrimitiveNode`
- `CR Text`
- `PreviewImage`
- `VAEEncode` ★核心
- `CR Text`
- `easy promptReplace`
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixelsX`
- `ImageScaleToTotalPixelsX`
- `ImageColorMatch+`
- `PrimitiveNode`
- `Seed (rgthree)`
- `LoadImage`
- `AILab_QwenVL`
- `SaveImage`
- `ShowText|pysssss`
- `Seed (rgthree)`
- `CR Text`
- `SaveImage`

## 知识

覆盖率 **82%**（101/123）

**有卡**：`CLIPLoader`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`easy cleanGpuUsed`、`KSamplerSelect`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`AILab_QwenVL`、`UNETLoader`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixelsX`、`SamplerCustom`、`VAEDecode`、`CLIPTextEncode`、`BasicScheduler`、`DetailDaemonSamplerNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LatentColorMatchSimple`、`SplitSigmas`、`AIO_Preprocessor`、`easy imageSizeBySide`、`ZImageFunControlnet`、`ModelPatchLoader`、`VAELoader_Any`、`CLIPLoader_Any`、`Seed (rgthree)`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ProcessString`、`JDCN_StringToList`、`LoraLoaderModelOnly`、`CFGNorm`、`CR Text`、`easy promptReplace`、`ImageColorMatch+`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader

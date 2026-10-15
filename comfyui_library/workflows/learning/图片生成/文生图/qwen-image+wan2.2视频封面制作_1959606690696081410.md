---
key: 图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json
name: qwen-image+wan2.2视频封面制作_1959606690696081410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json
hash: 449fc78dbd17d946
coverage: 0.590909
learned_at: 2026-10-10 20:59:24
nodes: [CLIPTextEncode, JjkText, JjkText, JjkText, QwenVLDetection, BBoxesToSAM2, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, VAELoader, JjkText, CLIPTextEncode, LayerUtility: PurgeVRAM, VAEDecode, JjkText, easy showAnything, SeedVR2BlockSwap, SeedVR2, LayerUtility: PurgeVRAM, VAEDecode, JjkText, VAELoader, CLIPLoader, JjkText, UNETLoader, EmptySD3LatentImage, ImpactSwitch, LimitNumber, EmptySD3LatentImage, Note, EmptySD3LatentImage, JjkText, TextCombinerTwo, TextCombinerSix, TextCombinerTwo, TextCombinerTwo, TextCombinerSix, LayerUtility: PurgeVRAM, JjkText, JjkText, TextCombinerTwo, TextCombinerTwo, JjkText, TextCombinerSix, JjkText, InpaintModelConditioning, LayerMask: MaskPreview, LayerUtility: PurgeVRAM, ModelSamplingAuraFlow, easy showAnything, easy showAnything, CLIPTextEncode, KSampler, KSampler, PrimitiveInt, easy seed, CLIPTextEncode, LayerMask: MaskPreview, JjkText, JjkText, PreviewImage, GetMaskSizeAndCount, MathExpression|pysssss, LayerMask: SAM2Ultra, LayerMask: MaskPreview, MathExpression|pysssss, MathExpression|pysssss, MaskBoundingBox+, LayerMask: MaskGrow, VAEDecode, RH_Captioner, KSampler, RH_LLMAPI_NODE, DownloadAndLoadQwenModel, TextCombinerSix, RH_LLMAPI_NODE, JjkText, CLIPTextEncode, LoadImage, SaveImage, SaveImage, SaveImage, SaveImage, CreateShapeMask]
patterns: []
missing: [LayerMask: MaskGrow, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, MaskBoundingBox+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, LayerMask: MaskPreview, LayerMask: MaskPreview, LayerMask: MaskPreview, easy seed]
parameters: {"cfg": 3.5, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "normal", "seed": 756467682942260, "steps": 20}
discoveries: [次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SAM2Ultra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `MaskBoundingBox+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json`

## 结构

**节点**（88 个）：
- `CLIPTextEncode`
- `JjkText`
- `JjkText`
- `JjkText`
- `QwenVLDetection`
- `BBoxesToSAM2`
- `CLIPLoader`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `ModelSamplingSD3`
- `VAELoader`
- `JjkText`
- `CLIPTextEncode`
- `LayerUtility: PurgeVRAM`
- `VAEDecode`
- `JjkText`
- `easy showAnything`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `VAEDecode`
- `JjkText`
- `VAELoader`
- `CLIPLoader`
- `JjkText`
- `UNETLoader`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `LimitNumber`
- `EmptySD3LatentImage`
- `Note`
- `EmptySD3LatentImage`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerSix`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `TextCombinerSix`
- `LayerUtility: PurgeVRAM`
- `JjkText`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `TextCombinerSix`
- `JjkText`
- `InpaintModelConditioning`
- `LayerMask: MaskPreview`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingAuraFlow`
- `easy showAnything`
- `easy showAnything`
- `CLIPTextEncode`
- `KSampler`
- `KSampler`
- `PrimitiveInt`
- `easy seed`
- `CLIPTextEncode`
- `LayerMask: MaskPreview`
- `JjkText`
- `JjkText`
- `PreviewImage`
- `GetMaskSizeAndCount`
- `MathExpression|pysssss`
- `LayerMask: SAM2Ultra`
- `LayerMask: MaskPreview`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MaskBoundingBox+`
- `LayerMask: MaskGrow`
- `VAEDecode`
- `RH_Captioner`
- `KSampler`
- `RH_LLMAPI_NODE`
- `DownloadAndLoadQwenModel`
- `TextCombinerSix`
- `RH_LLMAPI_NODE`
- `JjkText`
- `CLIPTextEncode`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CreateShapeMask`

## 关键参数

- `cfg` = `3.5`
- `denoise` = `0.30000000000000004`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `756467682942260`
- `steps` = `20`

## 知识

覆盖率 **59%**（52/88）

**有卡**：`CLIPTextEncode`、`JjkText`、`QwenVLDetection`、`BBoxesToSAM2`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`easy showAnything`、`SeedVR2BlockSwap`、`SeedVR2`、`EmptySD3LatentImage`、`ImpactSwitch`、`LimitNumber`、`Note`、`TextCombinerTwo`、`TextCombinerSix`、`InpaintModelConditioning`、`LayerMask: MaskPreview`

**缺卡**（14）：`LayerMask: MaskGrow`、`LayerMask: SAM2Ultra`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`MaskBoundingBox+`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`LayerMask: MaskPreview`、`LayerMask: MaskPreview`、`LayerMask: MaskPreview`、`easy seed`

## 学习发现

- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SAM2Ultra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `MaskBoundingBox+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `LayerMask: MaskPreview` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

---
key: 图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json
name: qwen-image+wan2.2视频封面制作_1959606690696081410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json
hash: 449fc78dbd17d946
coverage: 0.75
learned_at: 2026-10-15 22:27:54
nodes: [CLIPTextEncode, JjkText, JjkText, JjkText, QwenVLDetection, BBoxesToSAM2, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, ModelSamplingSD3, VAELoader, JjkText, CLIPTextEncode, LayerUtility: PurgeVRAM, VAEDecode, JjkText, easy showAnything, SeedVR2BlockSwap, SeedVR2, LayerUtility: PurgeVRAM, VAEDecode, JjkText, VAELoader, CLIPLoader, JjkText, UNETLoader, EmptySD3LatentImage, ImpactSwitch, LimitNumber, EmptySD3LatentImage, Note, EmptySD3LatentImage, JjkText, TextCombinerTwo, TextCombinerSix, TextCombinerTwo, TextCombinerTwo, TextCombinerSix, LayerUtility: PurgeVRAM, JjkText, JjkText, TextCombinerTwo, TextCombinerTwo, JjkText, TextCombinerSix, JjkText, InpaintModelConditioning, LayerMask: MaskPreview, LayerUtility: PurgeVRAM, ModelSamplingAuraFlow, easy showAnything, easy showAnything, CLIPTextEncode, KSampler, KSampler, PrimitiveInt, easy seed, CLIPTextEncode, LayerMask: MaskPreview, JjkText, JjkText, PreviewImage, GetMaskSizeAndCount, MathExpression|pysssss, LayerMask: SAM2Ultra, LayerMask: MaskPreview, MathExpression|pysssss, MathExpression|pysssss, MaskBoundingBox+, LayerMask: MaskGrow, VAEDecode, RH_Captioner, KSampler, RH_LLMAPI_NODE, DownloadAndLoadQwenModel, TextCombinerSix, RH_LLMAPI_NODE, JjkText, CLIPTextEncode, LoadImage, SaveImage, SaveImage, SaveImage, SaveImage, CreateShapeMask]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "normal", "seed": 756467682942260, "steps": 20}
---

# 图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image+wan2.2视频封面制作_1959606690696081410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `CLIPTextEncode` ★核心
- `JjkText`
- `JjkText`
- `JjkText`
- `QwenVLDetection`
- `BBoxesToSAM2`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `JjkText`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `JjkText`
- `easy showAnything`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `JjkText`
- `VAELoader`
- `CLIPLoader`
- `JjkText`
- `UNETLoader` ★核心
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
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `PrimitiveInt`
- `easy seed`
- `CLIPTextEncode` ★核心
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
- `VAEDecode` ★核心
- `RH_Captioner`
- `KSampler` ★核心
- `RH_LLMAPI_NODE`
- `DownloadAndLoadQwenModel`
- `TextCombinerSix`
- `RH_LLMAPI_NODE`
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CreateShapeMask`

## 关键参数

- `seed` = `756467682942260`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **75%**（66/88）

**有卡**：`CLIPTextEncode`、`QwenVLDetection`、`BBoxesToSAM2`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`SeedVR2BlockSwap`、`SeedVR2`、`EmptySD3LatentImage`、`LimitNumber`、`TextCombinerTwo`、`TextCombinerSix`、`InpaintModelConditioning`、`LayerMask: MaskPreview`、`ModelSamplingAuraFlow`、`KSampler`、`easy seed`、`GetMaskSizeAndCount`、`MathExpression|pysssss`、`LayerMask: SAM2Ultra`、`MaskBoundingBox+`、`LayerMask: MaskGrow`、`RH_Captioner`、`RH_LLMAPI_NODE`、`DownloadAndLoadQwenModel`、`LoadImage`、`SaveImage`、`CreateShapeMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

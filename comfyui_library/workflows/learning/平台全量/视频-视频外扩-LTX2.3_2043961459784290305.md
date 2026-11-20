---
key: 平台全量/视频-视频外扩-LTX2.3_2043961459784290305.json
name: 视频-视频外扩-LTX2.3_2043961459784290305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频外扩-LTX2.3_2043961459784290305.json
hash: 9803247b6f93279d
coverage: 0.752688
learned_at: 2026-11-14 02:34:31
nodes: [LTXVConcatAVLatent, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, CFGGuider, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuide, LTX2SamplingPreviewOverride, KSamplerSelect, ManualSigmas, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXAVTextEncoderLoader, LTXVConditioning, SamplerCustomAdvanced, LTXVEmptyLatentAudio, CheckpointLoaderSimple, LTXVAudioVAELoader, easy showAnything, easy imageSize, GetNode, GetNode, PreviewImage, ImageFromBatch, GetImageSizeAndCount, SetNode, SetNode, GetNode, GetImageSizeAndCount, SetNode, MemoryCleaner, VHS_VideoCombine, Reroute, ShowText|pysssss, SetNode, PreviewImage, easy showAnything, JWFloatToString, StringFunction|pysssss, ImageFromBatch+, Qwen3_VQA, GetNode, easy showAnything, RH_LLMAPI_NODE, easy positive, easy positive, easy positive, SetNode, StringFunction|pysssss, easy saveText, GetImageSizeAndCount, GetNode, VAEDecodeTiled, ImageConcanate, GetImageSizeAndCount, CM_FloatToInt, GetNode, easy seed, easy positive, easy anythingIndexSwitch, GetNode, LTXVPreprocess, PrimitiveBoolean, EmptyImage, RandomNoise, GetNode, Reroute, GetImageSizeAndCount, GetImageSizeAndCount, PrimitiveFloat, MathExpression|pysssss, ImageFromBatch, ImpactFloat, VHS_VideoInfoLoaded, GetImageSizeAndCount, GetImageSize, easy int, GetImageSizeAndCount, ImagePadKJ, SetNode, VHS_VideoCombine, GetImageSizeAndCount, ImageResizeKJv2, GetImageSizeAndCount, easy int, easy int, easy int, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 平台全量/视频-视频外扩-LTX2.3_2043961459784290305.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频外扩-LTX2.3_2043961459784290305.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuide`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `easy showAnything`
- `easy imageSize`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `Reroute`
- `ShowText|pysssss`
- `SetNode`
- `PreviewImage`
- `easy showAnything`
- `JWFloatToString`
- `StringFunction|pysssss`
- `ImageFromBatch+`
- `Qwen3_VQA`
- `GetNode`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `easy positive`
- `easy positive`
- `easy positive`
- `SetNode`
- `StringFunction|pysssss`
- `easy saveText`
- `GetImageSizeAndCount`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ImageConcanate`
- `GetImageSizeAndCount`
- `CM_FloatToInt`
- `GetNode`
- `easy seed`
- `easy positive`
- `easy anythingIndexSwitch`
- `GetNode`
- `LTXVPreprocess`
- `PrimitiveBoolean`
- `EmptyImage`
- `RandomNoise`
- `GetNode`
- `Reroute`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `ImpactFloat`
- `VHS_VideoInfoLoaded`
- `GetImageSizeAndCount`
- `GetImageSize`
- `easy int`
- `GetImageSizeAndCount`
- `ImagePadKJ`
- `SetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `easy int`
- `easy int`
- `easy int`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **75%**（70/93）

**有卡**：`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuide`、`LTX2SamplingPreviewOverride`、`KSamplerSelect`、`ManualSigmas`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`easy imageSize`、`ImageFromBatch`、`GetImageSizeAndCount`、`MemoryCleaner`、`VHS_VideoCombine`、`JWFloatToString`、`StringFunction|pysssss`、`ImageFromBatch+`、`Qwen3_VQA`、`RH_LLMAPI_NODE`、`easy positive`、`easy saveText`、`VAEDecodeTiled`、`ImageConcanate`、`CM_FloatToInt`、`easy seed`、`easy anythingIndexSwitch`、`LTXVPreprocess`、`PrimitiveBoolean`、`EmptyImage`、`RandomNoise`、`MathExpression|pysssss`、`ImpactFloat`、`VHS_VideoInfoLoaded`、`GetImageSize`、`easy int`、`ImagePadKJ`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、easy seed、KSamplerSelect、SamplerCustomAdvanced

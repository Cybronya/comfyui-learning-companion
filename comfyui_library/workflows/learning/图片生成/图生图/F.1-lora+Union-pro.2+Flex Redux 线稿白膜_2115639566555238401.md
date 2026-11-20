---
key: 图片生成/图生图/F.1-lora+Union-pro.2+Flex Redux 线稿白膜_2115639566555238401.json
name: F.1-lora+Union-pro.2+Flex Redux 线稿白膜_2115639566555238401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1-lora+Union-pro.2+Flex Redux 线稿白膜_2115639566555238401.json
hash: ee25946f1dafc059
coverage: 0.815217
learned_at: 2026-10-30 17:49:30
nodes: [BasicGuider, FluxGuidance, ConditioningZeroOut, EmptyLatentImage, RandomNoise, easy cleanGpuUsed, SamplerCustomAdvanced, KSamplerSelect, VAEDecode, BasicScheduler, Image Levels Adjustment, ImageSharpen, ModelSamplingFlux, ImageResize+, SetUnionControlNetType, SetUnionControlNetType, AIO_Preprocessor, DepthAnythingV2Preprocessor, ImageResize+, ControlNetLoader, AIO_Preprocessor, ImageResize+, PreviewImage, ImageResize+, FloatComparison, MathExpression|pysssss, Text Concatenate, Switch any [Crystools], MathExpression|pysssss, FloatComparison, DF_Float, Switch any [Crystools], DF_Float, ZML_AnyTypeSwitch, DF_Float, RunningHub SeedXPro Translator, String Literal, Fast Groups Bypasser (rgthree), DF_Float, Fast Groups Bypasser (rgthree), DF_Float, Fast Groups Bypasser (rgthree), DF_Float, Fast Groups Bypasser (rgthree), DF_Float, Fast Groups Bypasser (rgthree), DF_Float, Fast Groups Bypasser (rgthree), DF_Float, Fast Groups Bypasser (rgthree), DF_Float, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, CLIPTextEncode, PreviewImage, PreviewImage, ImageResize+, DF_Integer, easy showAnything, CLIPVisionLoader, StyleModelLoader, CLIPVisionEncode, StyleModelApply, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStar, VAELoader, DualCLIPLoader, DF_Float, DF_Float, DF_Float, easy showAnything, String Literal, 3c4e3e3a-1576-4637-abe2-148d45be46f6, ControlNetApplySD3, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
parameters: {"batch_size": 2, "controlnet_strength": 0.3500000000000001, "height": 512, "width": 512}
---

# 图片生成/图生图/F.1-lora+Union-pro.2+Flex Redux 线稿白膜_2115639566555238401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1-lora+Union-pro.2+Flex Redux 线稿白膜_2115639566555238401.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `BasicGuider`
- `FluxGuidance`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `RandomNoise`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `Image Levels Adjustment`
- `ImageSharpen`
- `ModelSamplingFlux`
- `ImageResize+`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `DepthAnythingV2Preprocessor`
- `ImageResize+`
- `ControlNetLoader`
- `AIO_Preprocessor`
- `ImageResize+`
- `PreviewImage`
- `ImageResize+`
- `FloatComparison`
- `MathExpression|pysssss`
- `Text Concatenate`
- `Switch any [Crystools]`
- `MathExpression|pysssss`
- `FloatComparison`
- `DF_Float`
- `Switch any [Crystools]`
- `DF_Float`
- `ZML_AnyTypeSwitch`
- `DF_Float`
- `RunningHub SeedXPro Translator`
- `String Literal`
- `Fast Groups Bypasser (rgthree)`
- `DF_Float`
- `Fast Groups Bypasser (rgthree)`
- `DF_Float`
- `Fast Groups Bypasser (rgthree)`
- `DF_Float`
- `Fast Groups Bypasser (rgthree)`
- `DF_Float`
- `Fast Groups Bypasser (rgthree)`
- `DF_Float`
- `Fast Groups Bypasser (rgthree)`
- `DF_Float`
- `Fast Groups Bypasser (rgthree)`
- `DF_Float`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `ImageResize+`
- `DF_Integer`
- `easy showAnything`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
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
- `CFGZeroStar`
- `VAELoader`
- `DualCLIPLoader`
- `DF_Float`
- `DF_Float`
- `DF_Float`
- `easy showAnything`
- `String Literal`
- `3c4e3e3a-1576-4637-abe2-148d45be46f6`
- `ControlNetApplySD3` ★核心
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `2`
- `controlnet_strength` = `0.3500000000000001`

## 知识

覆盖率 **82%**（75/92）

**有卡**：`BasicGuider`、`FluxGuidance`、`ConditioningZeroOut`、`EmptyLatentImage`、`RandomNoise`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecode`、`BasicScheduler`、`Image Levels Adjustment`、`ImageSharpen`、`ModelSamplingFlux`、`ImageResize+`、`SetUnionControlNetType`、`AIO_Preprocessor`、`DepthAnythingV2Preprocessor`、`ControlNetLoader`、`FloatComparison`、`MathExpression|pysssss`、`Text Concatenate`、`Switch any [Crystools]`、`DF_Float`、`ZML_AnyTypeSwitch`、`RunningHub SeedXPro Translator`、`String Literal`、`LoadImage`、`SaveImage`、`CLIPTextEncode`、`DF_Integer`、`CLIPVisionLoader`、`StyleModelLoader`、`CLIPVisionEncode`、`StyleModelApply`、`UNETLoader`、`LoraLoaderModelOnly`、`CFGZeroStar`、`VAELoader`、`DualCLIPLoader`、`3c4e3e3a-1576-4637-abe2-148d45be46f6`、`ControlNetApplySD3`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

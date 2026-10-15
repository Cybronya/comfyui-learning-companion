---
key: 视频生成/文生视频/AI换装丨Flux2-Klein＋Wan2.2丨换装试穿·转身视频_2099769122765758466.json
name: AI换装丨Flux2-Klein＋Wan2.2丨换装试穿·转身视频_2099769122765758466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI换装丨Flux2-Klein＋Wan2.2丨换装试穿·转身视频_2099769122765758466.json
hash: 2c2a6f3669c4d7b9
coverage: 0.883117
learned_at: 2026-10-15 22:43:59
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPTextEncode, CLIPTextEncode, SimpleMath+, VHS_VideoCombine, INTConstant, UNETLoader, UNETLoader, LoraLoaderModelOnly, DownloadAndLoadGIMMVFIModel, VAELoader, GetImageSize, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, RandomNoise, LoraLoaderModelOnly, UNETLoader, easy ifElse, easy ifElse, easy ifElse, ZML_AnyTypeSwitchFive, ZML_AnyTypeSwitchFive, Logic Comparison AND, ImpactNeg, ImpactNeg, Logic Comparison AND, Text Multiline, Text Multiline, SaveImage, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, CFGGuider, AnyBooleanSwitch, AnyBooleanSwitch, WanImageToVideo, GIMMVFI_interpolate, CLIPLoader, CLIPLoader, PainterVRAM, ImageConcatMulti, ImpactControlBridge, ImageConcatMulti, VHS_VideoCombine, workflow>load image03, PainterVRAM, PreviewAny, ImpactControlBridge, VAEEncode, ReferenceLatent, ReferenceLatent, Int, Int, Int, Int, ImageScaleToTotalPixels, PrimitiveBoolean, PrimitiveBoolean, PrimitiveBoolean, PrimitiveBoolean, Fast Groups Bypasser (rgthree), 1hew_StringJoinMulti, Note, Note, Note, workflow>load image02, workflow>load image01]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/AI换装丨Flux2-Klein＋Wan2.2丨换装试穿·转身视频_2099769122765758466.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI换装丨Flux2-Klein＋Wan2.2丨换装试穿·转身视频_2099769122765758466.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `VHS_VideoCombine`
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `VAELoader`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `ZML_AnyTypeSwitchFive`
- `ZML_AnyTypeSwitchFive`
- `Logic Comparison AND`
- `ImpactNeg`
- `ImpactNeg`
- `Logic Comparison AND`
- `Text Multiline`
- `Text Multiline`
- `SaveImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CFGGuider`
- `AnyBooleanSwitch`
- `AnyBooleanSwitch`
- `WanImageToVideo`
- `GIMMVFI_interpolate`
- `CLIPLoader`
- `CLIPLoader`
- `PainterVRAM`
- `ImageConcatMulti`
- `ImpactControlBridge`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `workflow>load image03`
- `PainterVRAM`
- `PreviewAny`
- `ImpactControlBridge`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImageScaleToTotalPixels`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `1hew_StringJoinMulti`
- `Note`
- `Note`
- `Note`
- `workflow>load image02`
- `workflow>load image01`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（68/77）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`CLIPTextEncode`、`SimpleMath+`、`VHS_VideoCombine`、`INTConstant`、`UNETLoader`、`LoraLoaderModelOnly`、`DownloadAndLoadGIMMVFIModel`、`VAELoader`、`GetImageSize`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`RandomNoise`、`ZML_AnyTypeSwitchFive`、`Logic Comparison AND`、`ImpactNeg`、`Text Multiline`、`SaveImage`、`CFGGuider`、`AnyBooleanSwitch`、`WanImageToVideo`、`GIMMVFI_interpolate`、`CLIPLoader`、`PainterVRAM`、`ImageConcatMulti`、`ImpactControlBridge`、`workflow>load image03`、`VAEEncode`、`ReferenceLatent`、`Int`、`ImageScaleToTotalPixels`、`PrimitiveBoolean`、`1hew_StringJoinMulti`、`workflow>load image02`、`workflow>load image01`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerAdvanced

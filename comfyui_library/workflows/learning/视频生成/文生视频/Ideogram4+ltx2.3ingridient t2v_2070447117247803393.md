---
key: 视频生成/文生视频/Ideogram4+ltx2.3ingridient t2v_2070447117247803393.json
name: Ideogram4+ltx2.3ingridient t2v_2070447117247803393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ideogram4+ltx2.3ingridient t2v_2070447117247803393.json
hash: 5bbd00c6170f5c23
coverage: 0.91
learned_at: 2026-10-15 22:44:28
nodes: [ConditioningZeroOut, EmptyFlux2LatentImage, RandomNoise, PrimitiveInt, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyNumberConvert, JsonExtractString, ComfyNumberConvert, StringReplace, JsonExtractString, CustomCombo, DualModelGuider, KSamplerSelect, Ideogram4OptimizationsKJ, Ideogram4OptimizationsKJ, GetVideoComponents, ResizeImageMaskNode, PrimitiveFloat, RepeatImageBatch, RandomNoise, GetImageSize, KSamplerSelect, CFGGuider, ManualSigmas, LTXVAudioVAEDecode, SamplerCustomAdvanced, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVEmptyLatentAudio, LTXFloatToInt, easy cleanGpuUsed, LTXVTiledVAEDecode, LTXVConditioning, LTXVConcatAVLatent, KSamplerSelect, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, LTXVAudioVAEDecode, VAEDecode, LTXVConcatAVLatent, easy cleanGpuUsed, easy cleanGpuUsed, PrimitiveInt, CFGGuider, BasicScheduler, PrimitiveBoolean, easy cleanGpuUsed, LTXVCropGuides, LTXVCropGuides, LTXVLatentUpsampler, LTXAddVideoICLoRAGuide, easy cleanGpuUsed, Label (rgthree), CLIPTextEncode, CLIPTextEncode, Fast Groups Bypasser (rgthree), ComfyNumberConvert, JsonExtractString, SamplerCustomAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LTXAddVideoICLoRAGuide, UNETLoader, CFGOverride, UNETLoader, VAELoader, LatentUpscaleModelLoader, easy cleanGpuUsed, CreateVideo, VAELoaderKJ, VAELoaderKJ, DualCLIPLoaderGGUF, LTXICLoRALoaderModelOnly, JsonExtractString, VAEDecode, CreateVideo, Fast Groups Bypasser (rgthree), CLIPTextEncode, ShowText|pysssss, Ideogram4PromptBuilderKJ, CLIPLoader, RH_LLMAPI_NODE, ImageScaleBy, StringReplace, StringReplace, JWStringMultiline, Ideogram4Scheduler, PreviewImage, VHS_VideoCombine, SaveVideo, TextInput_, Label (rgthree), PreviewAny, UnetLoaderGGUF]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/文生视频/Ideogram4+ltx2.3ingridient t2v_2070447117247803393.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ideogram4+ltx2.3ingridient t2v_2070447117247803393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `JsonExtractString`
- `ComfyNumberConvert`
- `StringReplace`
- `JsonExtractString`
- `CustomCombo`
- `DualModelGuider`
- `KSamplerSelect` ★核心
- `Ideogram4OptimizationsKJ`
- `Ideogram4OptimizationsKJ`
- `GetVideoComponents`
- `ResizeImageMaskNode`
- `PrimitiveFloat`
- `RepeatImageBatch`
- `RandomNoise`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVEmptyLatentAudio` ★核心
- `LTXFloatToInt`
- `easy cleanGpuUsed`
- `LTXVTiledVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PrimitiveInt`
- `CFGGuider`
- `BasicScheduler`
- `PrimitiveBoolean`
- `easy cleanGpuUsed`
- `LTXVCropGuides`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXAddVideoICLoRAGuide`
- `easy cleanGpuUsed`
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ComfyNumberConvert`
- `JsonExtractString`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXAddVideoICLoRAGuide`
- `UNETLoader` ★核心
- `CFGOverride`
- `UNETLoader` ★核心
- `VAELoader`
- `LatentUpscaleModelLoader`
- `easy cleanGpuUsed`
- `CreateVideo`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoaderGGUF`
- `LTXICLoRALoaderModelOnly` ★核心
- `JsonExtractString`
- `VAEDecode` ★核心
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `Ideogram4PromptBuilderKJ`
- `CLIPLoader`
- `RH_LLMAPI_NODE`
- `ImageScaleBy`
- `StringReplace`
- `StringReplace`
- `JWStringMultiline`
- `Ideogram4Scheduler`
- `PreviewImage`
- `VHS_VideoCombine`
- `SaveVideo`
- `TextInput_`
- `Label (rgthree)`
- `PreviewAny`
- `UnetLoaderGGUF` ★核心

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（91/100）

**有卡**：`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`RandomNoise`、`ComfyMathExpression`、`ComfyNumberConvert`、`JsonExtractString`、`StringReplace`、`CustomCombo`、`DualModelGuider`、`KSamplerSelect`、`Ideogram4OptimizationsKJ`、`GetVideoComponents`、`ResizeImageMaskNode`、`RepeatImageBatch`、`GetImageSize`、`CFGGuider`、`ManualSigmas`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`LTXFloatToInt`、`easy cleanGpuUsed`、`LTXVTiledVAEDecode`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecode`、`BasicScheduler`、`PrimitiveBoolean`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXAddVideoICLoRAGuide`、`Label (rgthree)`、`CLIPTextEncode`、`UNETLoader`、`CFGOverride`、`VAELoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`VAELoaderKJ`、`DualCLIPLoaderGGUF`、`LTXICLoRALoaderModelOnly`、`Ideogram4PromptBuilderKJ`、`CLIPLoader`、`RH_LLMAPI_NODE`、`ImageScaleBy`、`JWStringMultiline`、`Ideogram4Scheduler`、`VHS_VideoCombine`、`SaveVideo`、`TextInput_`、`UnetLoaderGGUF`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect

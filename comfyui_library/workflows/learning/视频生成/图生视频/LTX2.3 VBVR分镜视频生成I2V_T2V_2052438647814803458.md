---
key: 视频生成/图生视频/LTX2.3 VBVR分镜视频生成I2V_T2V_2052438647814803458.json
name: LTX2.3 VBVR分镜视频生成I2V_T2V_2052438647814803458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 VBVR分镜视频生成I2V_T2V_2052438647814803458.json
hash: 77182ef7aef7170b
coverage: 0.526316
learned_at: 2026-10-15 22:37:29
nodes: [GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SimpleCalculatorKJ, GetNode, GetNode, SetNode, SetNode, ResizeImageMaskNode, SetNode, SetNode, GetImageSize, ResizeImagesByLongerEdge, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, KSamplerSelect, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, MarkdownNote, SimpleCalculatorKJ, GetNode, MarkdownNote, RandomNoise, SetNode, MarkdownNote, MarkdownNote, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, SetNode, GetNode, RandomNoise, GetNode, SetNode, SetNode, EmptyLTXVLatentVideo, SetNode, MarkdownNote, MarkdownNote, SamplerCustomAdvanced, LTXVPreprocess, LTXVChunkFeedForward, UNETLoader, DualCLIPLoader, ManualSigmas, ManualSigmas, KSamplerSelect, LTXVScheduler, GetNode, CFGGuider, ManualSigmas, LoraLoaderModelOnly, ImageResizeKJv2, LatentUpscaleModelLoader, DualCLIPLoaderGGUF, SetNode, DualCLIPLoader, VAELoaderKJ, VAELoader, VAELoader, LTXVSeparateAVLatent, GetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, LTX2_NAG, INTConstant, INTConstant, PrimitiveBoolean, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, DualCLIPLoaderGGUF, SeedGenerator, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, UnetLoaderGGUF, INTConstant, CFGGuider, LTXVConcatAVLatent, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVLatentUpsampler, VHS_VideoCombine, easy convertAnything, LoadImage, VAEDecodeTiled, VHS_GetImageCount, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, MathExpression|pysssss, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, LazySwitchKJ, PreviewAny, AILab_QwenVL, TTP_text_mix, TextGenerateLTX2Prompt, PrimitiveStringMultiline, VHS_VideoCombine, PreviewAny, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX2.3 VBVR分镜视频生成I2V_T2V_2052438647814803458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052438647814803458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（133 个）：
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `MarkdownNote`
- `SimpleCalculatorKJ`
- `GetNode`
- `MarkdownNote`
- `RandomNoise`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ManualSigmas`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `GetNode`
- `CFGGuider`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `LatentUpscaleModelLoader`
- `DualCLIPLoaderGGUF`
- `SetNode`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `VAELoader`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTX2_NAG`
- `INTConstant`
- `INTConstant`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoaderGGUF`
- `SeedGenerator`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `UnetLoaderGGUF` ★核心
- `INTConstant`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `VHS_VideoCombine`
- `easy convertAnything`
- `LoadImage`
- `VAEDecodeTiled` ★核心
- `VHS_GetImageCount`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LazySwitchKJ`
- `PreviewAny`
- `AILab_QwenVL`
- `TTP_text_mix`
- `TextGenerateLTX2Prompt`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `PreviewAny`
- `PrimitiveBoolean`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（70/133）

**有卡**：`SimpleCalculatorKJ`、`ResizeImageMaskNode`、`GetImageSize`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVChunkFeedForward`、`UNETLoader`、`DualCLIPLoader`、`ManualSigmas`、`LTXVScheduler`、`CFGGuider`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`DualCLIPLoaderGGUF`、`VAELoaderKJ`、`VAELoader`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`INTConstant`、`PrimitiveBoolean`、`LTXVConditioning`、`CLIPTextEncode`、`SeedGenerator`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`UnetLoaderGGUF`、`LTXVLatentUpsampler`、`VHS_VideoCombine`、`easy convertAnything`、`LoadImage`、`VHS_GetImageCount`、`GetImageRangeFromBatch`、`MathExpression|pysssss`、`LazySwitchKJ`、`AILab_QwenVL`、`TTP_text_mix`、`TextGenerateLTX2Prompt`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

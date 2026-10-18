---
key: 视频生成/图生视频/🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json
name: 🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json
hash: 710268c0814258ea
coverage: 0.887097
learned_at: 2026-10-15 22:36:59
nodes: [RandomNoise, LTXVCropGuides, ManualSigmas, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetLatentNoiseMask, LTXVLatentUpsampler, Reroute, CLIPTextEncode, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConditioning, VAELoaderKJ, VAELoaderKJ, KSamplerSelect, PrimitiveBoolean, RandomNoise, LTXVPreprocess, SamplerCustomAdvanced, CFGGuider, ResizeImagesByLongerEdge, ResizeImageMaskNode, ComfyMathExpression, easy showAnything, EmptyLTXVLatentVideo, SolidMask, MelBandRoFormerSampler, LTXVAudioVAEEncode, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, CLIPTextEncode, LatentUpscaleModelLoader, DualCLIPLoader, MelBandRoFormerModelLoader, Text, LTXVAudioVAEDecode, easy downloadIndexTTSAndLoadModel, PreviewAudio, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, UNETLoader, LoraLoaderModelOnly, easy indexTTSGenerateSimple, LoadAudio, PreviewAudio, PrimitiveInt, GetAudioDurationFromAudio, math_calculate, easy showAnything, SimpleCalculatorKJ, TrimAudioDuration, CreateVideo, LayerUtility: PurgeVRAM V2]
patterns: []
missing: []
---

# 视频生成/图生视频/🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046500148146085890.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（62 个）：
- `RandomNoise`
- `LTXVCropGuides`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `SetLatentNoiseMask`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `PrimitiveBoolean`
- `RandomNoise`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `SolidMask`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `MelBandRoFormerModelLoader`
- `Text`
- `LTXVAudioVAEDecode` ★核心
- `easy downloadIndexTTSAndLoadModel`
- `PreviewAudio`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy indexTTSGenerateSimple`
- `LoadAudio`
- `PreviewAudio`
- `PrimitiveInt`
- `GetAudioDurationFromAudio`
- `math_calculate`
- `easy showAnything`
- `SimpleCalculatorKJ`
- `TrimAudioDuration`
- `CreateVideo`
- `LayerUtility: PurgeVRAM V2`

## 知识

覆盖率 **89%**（55/62）

**有卡**：`RandomNoise`、`LTXVCropGuides`、`ManualSigmas`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`VAELoaderKJ`、`KSamplerSelect`、`PrimitiveBoolean`、`LTXVPreprocess`、`SamplerCustomAdvanced`、`CFGGuider`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`SolidMask`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`Text`、`LTXVAudioVAEDecode`、`easy downloadIndexTTSAndLoadModel`、`PreviewAudio`、`VHS_VideoCombine`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`easy indexTTSGenerateSimple`、`LoadAudio`、`GetAudioDurationFromAudio`、`math_calculate`、`SimpleCalculatorKJ`、`TrimAudioDuration`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

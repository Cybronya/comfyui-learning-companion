---
key: 视频生成/文生视频/ltx2.3-文_图生视频-数字人-整合版_2031260976904933377.json
name: ltx2.3-文_图生视频-数字人-整合版_2031260976904933377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3-文_图生视频-数字人-整合版_2031260976904933377.json
hash: f4d21108deace15a
coverage: 0.921053
learned_at: 2026-10-15 22:47:22
nodes: [easy float, SolidMask, CLIPTextEncode, RandomNoise, DualCLIPLoader, easy int, easy int, easy int, RH_LLMAPI_NODE, VAELoaderKJ, VAELoaderKJ, JWInteger, JWInteger, ImpactSwitch, easy int, PreviewAny, VHS_VideoCombine, Note, TrimAudioDuration, easy compare, LTXVAudioVAELoader, LTXVAudioVAEEncode, CR Text, easy compare, LTXVConcatAVLatent, easy int, LazySwitch1way, easy compare, LazySwitch1way, easy int, CR Text, easy int, easy float, ImpactSwitch, MathExpression|pysssss, AudioCropProcessUTK, CM_FloatToInt, ImpactSwitch, MathExpression|pysssss, LazySwitch1way, EmptyLTXVLatentVideo, CR Text, ImpactSwitch, CR Text, CR Text Concatenate, easy int, SetLatentNoiseMask, LTXVConcatAVLatent, ImpactSwitch, LazySwitch1way, RH_LLMAPI_Pro_Node, Bjornulf_IfElse, easy int, easy compare, LoadAudio, LoadImage, easy int, LoadImage, CR Text, CLIPTextEncode, LTX2_NAG, LTXVConditioning, CR Text, CR Text, LatentUpscaleModelLoader, ManualSigmas, ManualSigmas, ManualSigmas, KSamplerSelect, KSamplerSelect, ManualSigmas, PrimitiveFloat, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LazySwitch1way, easy compare, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LazySwitch1way, LazySwitch1way, LTXVSeparateAVLatent, easy compare, LTXVAudioVAEDecode, easy compare, LazySwitch1way, easy int, easy int, easy int, LazySwitch1way, RTXVideoSuperResolution, VAEDecodeTiled, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTX2SamplingPreviewOverride, CFGGuider, LTX2SamplingPreviewOverride, RandomNoise, SamplerCustomAdvanced, ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2, easy int, easy compare, easy compare]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 20, "width": 93}
---

# 视频生成/文生视频/ltx2.3-文_图生视频-数字人-整合版_2031260976904933377.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3-文_图生视频-数字人-整合版_2031260976904933377.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（114 个）：
- `easy float`
- `SolidMask`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `DualCLIPLoader`
- `easy int`
- `easy int`
- `easy int`
- `RH_LLMAPI_NODE`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `JWInteger`
- `JWInteger`
- `ImpactSwitch`
- `easy int`
- `PreviewAny`
- `VHS_VideoCombine`
- `Note`
- `TrimAudioDuration`
- `easy compare`
- `LTXVAudioVAELoader`
- `LTXVAudioVAEEncode` ★核心
- `CR Text`
- `easy compare`
- `LTXVConcatAVLatent`
- `easy int`
- `LazySwitch1way`
- `easy compare`
- `LazySwitch1way`
- `easy int`
- `CR Text`
- `easy int`
- `easy float`
- `ImpactSwitch`
- `MathExpression|pysssss`
- `AudioCropProcessUTK`
- `CM_FloatToInt`
- `ImpactSwitch`
- `MathExpression|pysssss`
- `LazySwitch1way`
- `EmptyLTXVLatentVideo`
- `CR Text`
- `ImpactSwitch`
- `CR Text`
- `CR Text Concatenate`
- `easy int`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `ImpactSwitch`
- `LazySwitch1way`
- `RH_LLMAPI_Pro_Node`
- `Bjornulf_IfElse`
- `easy int`
- `easy compare`
- `LoadAudio`
- `LoadImage`
- `easy int`
- `LoadImage`
- `CR Text`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVConditioning`
- `CR Text`
- `CR Text`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `ManualSigmas`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LazySwitch1way`
- `easy compare`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LazySwitch1way`
- `LazySwitch1way`
- `LTXVSeparateAVLatent`
- `easy compare`
- `LTXVAudioVAEDecode` ★核心
- `easy compare`
- `LazySwitch1way`
- `easy int`
- `easy int`
- `easy int`
- `LazySwitch1way`
- `RTXVideoSuperResolution`
- `VAEDecodeTiled` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `LTX2SamplingPreviewOverride`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `easy compare`
- `easy compare`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `93`
- `height` = `20`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（105/114）

**有卡**：`easy float`、`SolidMask`、`CLIPTextEncode`、`RandomNoise`、`DualCLIPLoader`、`easy int`、`RH_LLMAPI_NODE`、`VAELoaderKJ`、`JWInteger`、`VHS_VideoCombine`、`TrimAudioDuration`、`easy compare`、`LTXVAudioVAELoader`、`LTXVAudioVAEEncode`、`CR Text`、`LTXVConcatAVLatent`、`LazySwitch1way`、`MathExpression|pysssss`、`AudioCropProcessUTK`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`CR Text Concatenate`、`SetLatentNoiseMask`、`RH_LLMAPI_Pro_Node`、`Bjornulf_IfElse`、`LoadAudio`、`LoadImage`、`LTX2_NAG`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`ManualSigmas`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`RTXVideoSuperResolution`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`CFGGuider`、`SamplerCustomAdvanced`、`LTX2SamplingPreviewOverride`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

---
key: 视频生成/图生视频/LTX2.3 数字人唱歌_对口型_2032276814873235457.json
name: LTX2.3 数字人唱歌_对口型_2032276814873235457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032276814873235457.json
hash: 877dbb8c5e2643da
coverage: 0.95
learned_at: 2026-10-15 22:35:35
nodes: [LoadImage, RandomNoise, SamplerCustomAdvanced, CLIPTextEncode, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVConcatAVLatent, RandomNoise, CLIPTextEncode, CFGGuider, ManualSigmas, KSamplerSelect, LTX2_NAG, LTXVImgToVideoConditionOnly, LTXVConditioning, LatentUpscaleModelLoader, ManualSigmas, intToFloat _O, DualCLIPLoader, LTXVConcatAVLatent, Reroute, Reroute, MelBandRoFormerSampler, CreateVideo, VAELoaderKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVImgToVideoInplace, LTXVPreprocess, MathExpression|pysssss, LTXVSpatioTemporalTiledVAEDecode, PrimitiveBoolean, Int, MathExpression|pysssss, MelBandRoFormerModelLoader, LTXVAudioVAEDecode, VAELoaderKJ, LTXVSeparateAVLatent, UNETLoader, Audio Duration (mtb), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, PrimitiveStringMultiline, SaveVideo, JWIntegerToString, JWIntegerToString, Int, Int, LoadAudio, AudioCrop, Int, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3 数字人唱歌_对口型_2032276814873235457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032276814873235457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTX2_NAG`
- `LTXVImgToVideoConditionOnly`
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `intToFloat _O`
- `DualCLIPLoader`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `MelBandRoFormerSampler` ★核心
- `CreateVideo`
- `VAELoaderKJ`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `MathExpression|pysssss`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `PrimitiveBoolean`
- `Int`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `LTXVAudioVAEDecode` ★核心
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `Audio Duration (mtb)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `JWIntegerToString`
- `JWIntegerToString`
- `Int`
- `Int`
- `LoadAudio`
- `AudioCrop`
- `Int`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `Int`

## 知识

覆盖率 **95%**（57/60）

**有卡**：`LoadImage`、`RandomNoise`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`KSamplerSelect`、`CFGGuider`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTX2_NAG`、`LTXVImgToVideoConditionOnly`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`intToFloat _O`、`DualCLIPLoader`、`MelBandRoFormerSampler`、`CreateVideo`、`VAELoaderKJ`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`MathExpression|pysssss`、`LTXVSpatioTemporalTiledVAEDecode`、`PrimitiveBoolean`、`Int`、`MelBandRoFormerModelLoader`、`LTXVAudioVAEDecode`、`UNETLoader`、`Audio Duration (mtb)`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveVideo`、`JWIntegerToString`、`LoadAudio`、`AudioCrop`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

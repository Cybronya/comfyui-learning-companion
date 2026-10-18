---
key: 视频生成/图生视频/LTX2.3稳定版数字人（最新版模型）_2044579812215361538.json
name: LTX2.3稳定版数字人（最新版模型）_2044579812215361538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3稳定版数字人（最新版模型）_2044579812215361538.json
hash: d40cf3504f913702
coverage: 0.788462
learned_at: 2026-10-15 22:36:39
nodes: [GetNode, SetNode, SetNode, KSamplerSelect, MelBandRoFormerModelLoader, LTXVSeparateAVLatent, LoraLoaderModelOnly, UNETLoader, LTXVSpatioTemporalTiledVAEDecode, MelBandRoFormerSampler, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVAudioVAEEncode, SetNode, SamplerCustomAdvanced, LTXVPreprocess, SaveAudio, LTXVAudioVAEDecode, CFGGuider, SimpleCalculatorKJ, SimpleCalculatorKJ, LTXVConditioning, RandomNoise, VAELoaderKJ, SolidMask, SetLatentNoiseMask, LTX2SamplingPreviewOverride, VAELoader, LTXVImgToVideoInplace, VAELoader, ManualSigmas, LTXVConcatAVLatent, TrimAudioDuration, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, INTConstant, PrimitiveFloat, ComfySwitchNode, Note, Note, CR Text, Note, Note, Note, LoadImage, DualCLIPLoader, LoadAudio, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX2.3稳定版数字人（最新版模型）_2044579812215361538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044579812215361538.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `MelBandRoFormerModelLoader`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `MelBandRoFormerSampler` ★核心
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `SaveAudio`
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `LTXVConditioning`
- `RandomNoise`
- `VAELoaderKJ`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTX2SamplingPreviewOverride`
- `VAELoader`
- `LTXVImgToVideoInplace`
- `VAELoader`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `TrimAudioDuration`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `PrimitiveFloat`
- `ComfySwitchNode`
- `Note`
- `Note`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `DualCLIPLoader`
- `LoadAudio`
- `VHS_VideoCombine`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`KSamplerSelect`、`MelBandRoFormerModelLoader`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`UNETLoader`、`LTXVSpatioTemporalTiledVAEDecode`、`MelBandRoFormerSampler`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEEncode`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`SaveAudio`、`LTXVAudioVAEDecode`、`CFGGuider`、`SimpleCalculatorKJ`、`LTXVConditioning`、`RandomNoise`、`VAELoaderKJ`、`SolidMask`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`VAELoader`、`LTXVImgToVideoInplace`、`ManualSigmas`、`LTXVConcatAVLatent`、`TrimAudioDuration`、`LTX2_NAG`、`CLIPTextEncode`、`INTConstant`、`CR Text`、`LoadImage`、`DualCLIPLoader`、`LoadAudio`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

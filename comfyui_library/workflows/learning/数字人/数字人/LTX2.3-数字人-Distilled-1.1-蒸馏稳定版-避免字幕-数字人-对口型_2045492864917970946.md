---
key: 数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json
name: LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json
hash: ff0b09340d0af4ca
coverage: 0.882353
learned_at: 2026-10-26 01:55:55
nodes: [LTXVEmptyLatentAudio, ManualSigmas, GetNode, Int, CR Text, LoadImage, DualCLIPLoader, VAELoader, MelBandRoFormerModelLoader, SimpleCalculatorKJ, LTX2_NAG, TrimAudioDuration, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVImgToVideoInplace, ComfySwitchNode, SolidMask, LTXVPreprocess, SetNode, LTXVConcatAVLatent, CLIPTextEncode, MelBandRoFormerSampler, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, KSamplerSelect, CustomAddLabel, LoadAudio, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, EmptyLTXVLatentVideo, SetNode, VAELoaderKJ, UNETLoader, SaveAudio, LTXVAudioVAEDecode, SetNode, SimpleCalculatorKJ, PrimitiveFloat, VHS_VideoCombine, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, VHS_VideoCombine, LTX2_NAG, LTXVConditioning, CFGGuider, RandomNoise, SamplerCustomAdvanced, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `GetNode`
- `Int`
- `CR Text`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `MelBandRoFormerModelLoader`
- `SimpleCalculatorKJ`
- `LTX2_NAG`
- `TrimAudioDuration`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVImgToVideoInplace`
- `ComfySwitchNode`
- `SolidMask`
- `LTXVPreprocess`
- `SetNode`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CustomAddLabel`
- `LoadAudio`
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `SaveAudio`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SimpleCalculatorKJ`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `LTX2_NAG`
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `INTConstant`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（45/51）

**有卡**：`LTXVEmptyLatentAudio`、`ManualSigmas`、`Int`、`CR Text`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`MelBandRoFormerModelLoader`、`SimpleCalculatorKJ`、`LTX2_NAG`、`TrimAudioDuration`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`SolidMask`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`MelBandRoFormerSampler`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVSpatioTemporalTiledVAEDecode`、`KSamplerSelect`、`CustomAddLabel`、`LoadAudio`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`UNETLoader`、`SaveAudio`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LTXVConditioning`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`INTConstant`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

---
key: 数字人/数字人/LTX2.3数字人_2046490310024372225.json
name: LTX2.3数字人_2046490310024372225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人_2046490310024372225.json
hash: 9a00f6a795290ba4
coverage: 0.87234
learned_at: 2026-10-26 01:56:03
nodes: [LTXVPreprocess, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LayerUtility: ImageScaleByAspectRatio V2, EmptyLTXVLatentVideo, VAELoaderKJ, SetNode, LTXVEmptyLatentAudio, CFGGuider, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, LTXVSeparateAVLatent, LTXVAudioVAEDecode, SaveAudio, SimpleCalculatorKJ, VAELoader, SetNode, VAELoader, LTXVImgToVideoInplace, SimpleCalculatorKJ, LTX2_NAG, SetNode, LTXVConcatAVLatent, LTX2SamplingPreviewOverride, GetNode, MelBandRoFormerSampler, MelBandRoFormerModelLoader, ComfySwitchNode, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, ManualSigmas, LTXVSpatioTemporalTiledVAEDecode, VHS_VideoCombine, TrimAudioDuration, PrimitiveFloat, VHS_VideoCombine, LoadImage, INTConstant, LoadAudio, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 数字人/数字人/LTX2.3数字人_2046490310024372225.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人_2046490310024372225.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `LTXVPreprocess`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLTXVLatentVideo`
- `VAELoaderKJ`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SaveAudio`
- `SimpleCalculatorKJ`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `LTXVImgToVideoInplace`
- `SimpleCalculatorKJ`
- `LTX2_NAG`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `ComfySwitchNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `ManualSigmas`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `VHS_VideoCombine`
- `TrimAudioDuration`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LoadImage`
- `INTConstant`
- `LoadAudio`
- `CR Text`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`LTXVPreprocess`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`CLIPTextEncode`、`LTXVConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`LTXVEmptyLatentAudio`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`SaveAudio`、`SimpleCalculatorKJ`、`VAELoader`、`LTXVImgToVideoInplace`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LTX2SamplingPreviewOverride`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`ManualSigmas`、`LTXVSpatioTemporalTiledVAEDecode`、`VHS_VideoCombine`、`TrimAudioDuration`、`LoadImage`、`INTConstant`、`LoadAudio`、`CR Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

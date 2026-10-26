---
key: 数字人/数字人/Wan2.2-S2V数字人-对口型唱歌_1976869794446299137.json
name: Wan2.2-S2V数字人-对口型唱歌_1976869794446299137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2-S2V数字人-对口型唱歌_1976869794446299137.json
hash: 537f6b849ac6f5be
coverage: 0.921053
learned_at: 2026-10-26 01:57:56
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, WanVideoVAELoader, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncodeCached, PreviewImage, ImageResize+, AudioEncoderLoader, WanVideoSampler, WanVideoDecode, ImageFromBatch+, NormalizeAudioLoudness, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, SoundFlow_GetLength, easy showAnything, AudioEncoderEncode, VHS_VideoCombine, AudioSeparation, LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, Reroute, CR Prompt Text, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, LoadImage, LoadAudio, Note _O]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2-S2V数字人-对口型唱歌_1976869794446299137.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2-S2V数字人-对口型唱歌_1976869794446299137.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `Note _O`
- `Note _O`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `ImageResize+`
- `AudioEncoderLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageFromBatch+`
- `NormalizeAudioLoudness`
- `easy compare`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `SDVN Any Show`
- `SDVN Any Show`
- `SoundFlow_GetLength`
- `easy showAnything`
- `AudioEncoderEncode`
- `VHS_VideoCombine`
- `AudioSeparation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Switch any [Crystools]`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `Reroute`
- `CR Prompt Text`
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `LoadImage`
- `LoadAudio`
- `Note _O`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`ImageResize+`、`AudioEncoderLoader`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`NormalizeAudioLoudness`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`SoundFlow_GetLength`、`AudioEncoderEncode`、`VHS_VideoCombine`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`CM_FloatToInt`、`CR Prompt Text`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached

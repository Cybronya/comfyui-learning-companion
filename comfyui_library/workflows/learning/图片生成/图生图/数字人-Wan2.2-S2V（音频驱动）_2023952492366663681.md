---
key: 图片生成/图生图/数字人-Wan2.2-S2V（音频驱动）_2023952492366663681.json
name: 数字人-Wan2.2-S2V（音频驱动）_2023952492366663681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/数字人-Wan2.2-S2V（音频驱动）_2023952492366663681.json
hash: fc7140aa5b7447e7
coverage: 0.921053
learned_at: 2026-10-23 13:03:26
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, Note _O, WanVideoVAELoader, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncodeCached, PreviewImage, ImageResize+, AudioEncoderLoader, NormalizeAudioLoudness, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, SoundFlow_GetLength, easy showAnything, AudioEncoderEncode, AudioSeparation, LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, Reroute, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, WanVideoSampler, CR Prompt Text, LoadImage, LoadAudio, WanVideoDecode, ImageFromBatch+, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/数字人-Wan2.2-S2V（音频驱动）_2023952492366663681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/数字人-Wan2.2-S2V（音频驱动）_2023952492366663681.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `Note _O`
- `Note _O`
- `Note _O`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `ImageResize+`
- `AudioEncoderLoader`
- `NormalizeAudioLoudness`
- `easy compare`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `SDVN Any Show`
- `SDVN Any Show`
- `SoundFlow_GetLength`
- `easy showAnything`
- `AudioEncoderEncode`
- `AudioSeparation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Switch any [Crystools]`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `Reroute`
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `WanVideoSampler` ★核心
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `WanVideoDecode`
- `ImageFromBatch+`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`ImageResize+`、`AudioEncoderLoader`、`NormalizeAudioLoudness`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`SoundFlow_GetLength`、`AudioEncoderEncode`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`CM_FloatToInt`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`WanVideoSampler`、`CR Prompt Text`、`LoadImage`、`LoadAudio`、`WanVideoDecode`、`ImageFromBatch+`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached

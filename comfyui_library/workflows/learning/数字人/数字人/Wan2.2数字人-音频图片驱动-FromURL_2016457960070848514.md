---
key: 数字人/数字人/Wan2.2数字人-音频图片驱动-FromURL_2016457960070848514.json
name: Wan2.2数字人-音频图片驱动-FromURL_2016457960070848514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2数字人-音频图片驱动-FromURL_2016457960070848514.json
hash: 29028164580350db
coverage: 0.9
learned_at: 2026-10-26 01:58:00
nodes: [WanVideoModelLoader, Note _O, AudioEncoderEncode, Note _O, WanVideoVAELoader, WanVideoTextEncodeCached, AudioEncoderLoader, Switch any [Crystools], SDVN Any Show, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, Reroute, easy showAnything, WanVideoAddS2VEmbeds, Note _O, MathExpression|pysssss, CM_FloatToInt, WanVideoEncode, WanVideoContextOptions, VHS_VideoCombine, MathExpression|pysssss, SDVN Any Show, WanVideoSetLoRAs, NormalizeAudioLoudness, SoundFlow_GetLength, easy showAnything, WanVideoLoraSelect, Reroute, SaveAudio, CR Prompt Text, WanVideoSampler, ImageFromBatch+, WanVideoDecode, WanVideoEmptyEmbeds, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, LoadImageFromUrl, LoadAudioFromUrl]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2数字人-音频图片驱动-FromURL_2016457960070848514.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2数字人-音频图片驱动-FromURL_2016457960070848514.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `WanVideoModelLoader`
- `Note _O`
- `AudioEncoderEncode`
- `Note _O`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `AudioEncoderLoader`
- `Switch any [Crystools]`
- `SDVN Any Show`
- `easy compare`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `SDVN Any Show`
- `Reroute`
- `easy showAnything`
- `WanVideoAddS2VEmbeds`
- `Note _O`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `WanVideoEncode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `SDVN Any Show`
- `WanVideoSetLoRAs`
- `NormalizeAudioLoudness`
- `SoundFlow_GetLength`
- `easy showAnything`
- `WanVideoLoraSelect`
- `Reroute`
- `SaveAudio`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `ImageFromBatch+`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `LoadImageFromUrl`
- `LoadAudioFromUrl`

## 知识

覆盖率 **90%**（36/40）

**有卡**：`WanVideoModelLoader`、`Note _O`、`AudioEncoderEncode`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`AudioEncoderLoader`、`Switch any [Crystools]`、`SDVN Any Show`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`WanVideoAddS2VEmbeds`、`CM_FloatToInt`、`WanVideoEncode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`NormalizeAudioLoudness`、`SoundFlow_GetLength`、`WanVideoLoraSelect`、`SaveAudio`、`CR Prompt Text`、`WanVideoSampler`、`ImageFromBatch+`、`WanVideoDecode`、`WanVideoEmptyEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`LoadImageFromUrl`、`LoadAudioFromUrl`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached、WanVideoEncode

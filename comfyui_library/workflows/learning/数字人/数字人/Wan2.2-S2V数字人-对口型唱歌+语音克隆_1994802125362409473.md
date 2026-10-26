---
key: 数字人/数字人/Wan2.2-S2V数字人-对口型唱歌+语音克隆_1994802125362409473.json
name: Wan2.2-S2V数字人-对口型唱歌+语音克隆_1994802125362409473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2-S2V数字人-对口型唱歌+语音克隆_1994802125362409473.json
hash: e740eefdf1c18cbe
coverage: 0.890909
learned_at: 2026-10-26 01:57:56
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, WanVideoVAELoader, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncodeCached, PreviewImage, ImageResize+, WanVideoSampler, WanVideoDecode, ImageFromBatch+, NormalizeAudioLoudness, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, SoundFlow_GetLength, easy showAnything, AudioEncoderEncode, VHS_VideoCombine, AudioSeparation, LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, CR Prompt Text, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, LoadImage, Note _O, CR Prompt Text, Note _O, SaveAudio, CR Prompt Text, Note, CR Prompt Text, LoadAudio, SaveAudio, SaveAudio, LoadAudio, Reroute, AudioEncoderLoader, IndexTTS2Run, IndexTTS2Run, IndexTTS2Run, SaveAudio, IndexTTS2Run, Fast Groups Bypasser (rgthree), ImpactSwitch, CR Prompt Text]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2-S2V数字人-对口型唱歌+语音克隆_1994802125362409473.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2-S2V数字人-对口型唱歌+语音克隆_1994802125362409473.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（55 个）：
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
- `CR Prompt Text`
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `LoadImage`
- `Note _O`
- `CR Prompt Text`
- `Note _O`
- `SaveAudio`
- `CR Prompt Text`
- `Note`
- `CR Prompt Text`
- `LoadAudio`
- `SaveAudio`
- `SaveAudio`
- `LoadAudio`
- `Reroute`
- `AudioEncoderLoader`
- `IndexTTS2Run`
- `IndexTTS2Run`
- `IndexTTS2Run`
- `SaveAudio`
- `IndexTTS2Run`
- `Fast Groups Bypasser (rgthree)`
- `ImpactSwitch`
- `CR Prompt Text`

## 知识

覆盖率 **89%**（49/55）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`ImageResize+`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`NormalizeAudioLoudness`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`SoundFlow_GetLength`、`AudioEncoderEncode`、`VHS_VideoCombine`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`CM_FloatToInt`、`CR Prompt Text`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`LoadImage`、`SaveAudio`、`LoadAudio`、`AudioEncoderLoader`、`IndexTTS2Run`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached

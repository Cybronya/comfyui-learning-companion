---
key: 视频生成/图生视频/Wan2.2-S2V数字人-对口型唱歌_1971380113747197954.json
name: Wan2.2-S2V数字人-对口型唱歌_1971380113747197954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-S2V数字人-对口型唱歌_1971380113747197954.json
hash: 2e60ea4e3d9bcad3
coverage: 0.921053
learned_at: 2026-10-15 22:31:56
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, Note _O, WanVideoVAELoader, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncodeCached, PreviewImage, ImageResize+, AudioEncoderLoader, WanVideoSampler, WanVideoDecode, ImageFromBatch+, NormalizeAudioLoudness, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, SoundFlow_GetLength, easy showAnything, AudioEncoderEncode, VHS_VideoCombine, AudioSeparation, LoadAudio, LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, Reroute, CR Prompt Text, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-S2V数字人-对口型唱歌_1971380113747197954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971380113747197954.json`

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
- `LoadAudio`
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

## 知识

覆盖率 **92%**（35/38）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`ImageResize+`、`AudioEncoderLoader`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`NormalizeAudioLoudness`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`SoundFlow_GetLength`、`AudioEncoderEncode`、`VHS_VideoCombine`、`AudioSeparation`、`LoadAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`CM_FloatToInt`、`CR Prompt Text`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached

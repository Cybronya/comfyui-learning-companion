---
key: 视频生成/图生视频/数字人-Wan2.2-S2V（音频驱动）_2020045393261764609.json
name: 数字人-Wan2.2-S2V（音频驱动）_2020045393261764609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字人-Wan2.2-S2V（音频驱动）_2020045393261764609.json
hash: 6b6da8f40e6a2428
coverage: 0.921053
learned_at: 2026-10-15 22:35:05
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, Note _O, WanVideoVAELoader, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncodeCached, PreviewImage, ImageResize+, AudioEncoderLoader, WanVideoDecode, ImageFromBatch+, NormalizeAudioLoudness, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, SoundFlow_GetLength, easy showAnything, AudioEncoderEncode, VHS_VideoCombine, AudioSeparation, LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, Reroute, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, WanVideoSampler, CR Prompt Text, LoadImage, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人-Wan2.2-S2V（音频驱动）_2020045393261764609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2020045393261764609.json`

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
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `WanVideoSampler` ★核心
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`ImageResize+`、`AudioEncoderLoader`、`WanVideoDecode`、`ImageFromBatch+`、`NormalizeAudioLoudness`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`SoundFlow_GetLength`、`AudioEncoderEncode`、`VHS_VideoCombine`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`CM_FloatToInt`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`WanVideoSampler`、`CR Prompt Text`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached

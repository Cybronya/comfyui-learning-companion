---
key: 视频生成/图生视频/Wan2.2-S2V数字人(低动态)_2003752068659724290.json
name: Wan2.2-S2V数字人(低动态)_2003752068659724290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-S2V数字人(低动态)_2003752068659724290.json
hash: 76fb424e35a62c76
coverage: 0.944444
learned_at: 2026-10-15 22:33:52
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, WanVideoVAELoader, WanVideoEncode, WanVideoTextEncodeCached, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, SoundFlow_GetLength, easy showAnything, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, Reroute, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, AudioSeparation, LayerUtility: ImageScaleByAspectRatio V2, AudioEncoderLoader, NormalizeAudioLoudness, AudioEncoderEncode, Note _O, WanVideoDecode, ImageFromBatch+, WanVideoSampler, WanVideoContextOptions, VHS_VideoCombine, LoadAudio, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-S2V数字人(低动态)_2003752068659724290.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2003752068659724290.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `Note _O`
- `Note _O`
- `WanVideoVAELoader`
- `WanVideoEncode`
- `WanVideoTextEncodeCached`
- `easy compare`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `SDVN Any Show`
- `SDVN Any Show`
- `SoundFlow_GetLength`
- `easy showAnything`
- `Switch any [Crystools]`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `Reroute`
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `AudioSeparation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AudioEncoderLoader`
- `NormalizeAudioLoudness`
- `AudioEncoderEncode`
- `Note _O`
- `WanVideoDecode`
- `ImageFromBatch+`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`SoundFlow_GetLength`、`Switch any [Crystools]`、`CM_FloatToInt`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`AudioSeparation`、`LayerUtility: ImageScaleByAspectRatio V2`、`AudioEncoderLoader`、`NormalizeAudioLoudness`、`AudioEncoderEncode`、`WanVideoDecode`、`ImageFromBatch+`、`WanVideoSampler`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LoadAudio`、`LoadImage`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached、WanVideoEncode

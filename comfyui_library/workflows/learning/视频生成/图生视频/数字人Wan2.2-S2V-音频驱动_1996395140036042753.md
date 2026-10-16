---
key: 视频生成/图生视频/数字人Wan2.2-S2V-音频驱动_1996395140036042753.json
name: 数字人Wan2.2-S2V-音频驱动_1996395140036042753.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1996395140036042753.json
hash: 5a800513606618a0
coverage: 0.897436
learned_at: 2026-10-15 22:33:26
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, Note _O, WanVideoVAELoader, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncodeCached, PreviewImage, ImageResize+, AudioEncoderLoader, NormalizeAudioLoudness, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, SoundFlow_GetLength, easy showAnything, AudioEncoderEncode, LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, Reroute, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, Note, LoadImage, AudioSeparation, CR Prompt Text, WanVideoSampler, WanVideoDecode, ImageFromBatch+, VHS_VideoCombine, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人Wan2.2-S2V-音频驱动_1996395140036042753.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996395140036042753.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Switch any [Crystools]`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `Reroute`
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `Note`
- `LoadImage`
- `AudioSeparation`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `LoadAudio`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoEncode`、`WanVideoTextEncodeCached`、`ImageResize+`、`AudioEncoderLoader`、`NormalizeAudioLoudness`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`SoundFlow_GetLength`、`AudioEncoderEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`CM_FloatToInt`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`LoadImage`、`AudioSeparation`、`CR Prompt Text`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`VHS_VideoCombine`、`LoadAudio`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached

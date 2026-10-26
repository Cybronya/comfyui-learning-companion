---
key: 数字人/数字人/Wan2.2-S2V数字人_1981607951481872386.json
name: Wan2.2-S2V数字人_1981607951481872386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2-S2V数字人_1981607951481872386.json
hash: 99b1a1f99ba07446
coverage: 0.923077
learned_at: 2026-10-26 01:57:57
nodes: [WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, Note _O, Note _O, WanVideoVAELoader, WanVideoContextOptions, WanVideoEncode, easy compare, CM_IntToFloat, MathExpression|pysssss, SDVN Any Show, SDVN Any Show, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], MathExpression|pysssss, MathExpression|pysssss, CM_FloatToInt, Reroute, WanVideoEmptyEmbeds, WanVideoAddS2VEmbeds, LoadImage, LoadAudio, Note _O, AudioEncoderEncode, ImageResize+, PreviewImage, SoundFlow_GetLength, AudioSeparation, NormalizeAudioLoudness, AudioEncoderLoader, WanVideoTextEncodeCached, WanVideoSampler, ImageFromBatch+, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2-S2V数字人_1981607951481872386.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2-S2V数字人_1981607951481872386.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `Note _O`
- `Note _O`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `WanVideoEncode`
- `easy compare`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `SDVN Any Show`
- `SDVN Any Show`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Switch any [Crystools]`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CM_FloatToInt`
- `Reroute`
- `WanVideoEmptyEmbeds`
- `WanVideoAddS2VEmbeds`
- `LoadImage`
- `LoadAudio`
- `Note _O`
- `AudioEncoderEncode`
- `ImageResize+`
- `PreviewImage`
- `SoundFlow_GetLength`
- `AudioSeparation`
- `NormalizeAudioLoudness`
- `AudioEncoderLoader`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `ImageFromBatch+`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`Note _O`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoEncode`、`easy compare`、`CM_IntToFloat`、`MathExpression|pysssss`、`SDVN Any Show`、`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`CM_FloatToInt`、`WanVideoEmptyEmbeds`、`WanVideoAddS2VEmbeds`、`LoadImage`、`LoadAudio`、`AudioEncoderEncode`、`ImageResize+`、`SoundFlow_GetLength`、`AudioSeparation`、`NormalizeAudioLoudness`、`AudioEncoderLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`ImageFromBatch+`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached

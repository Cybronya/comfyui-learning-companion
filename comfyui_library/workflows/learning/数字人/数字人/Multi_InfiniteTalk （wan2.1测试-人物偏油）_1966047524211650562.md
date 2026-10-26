---
key: 数字人/数字人/Multi_InfiniteTalk （wan2.1测试-人物偏油）_1966047524211650562.json
name: Multi_InfiniteTalk （wan2.1测试-人物偏油）_1966047524211650562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Multi_InfiniteTalk （wan2.1测试-人物偏油）_1966047524211650562.json
hash: 72beac50cdade170
coverage: 0.848485
learned_at: 2026-10-26 01:56:50
nodes: [LoadWanVideoT5TextEncoder, WanVideoLoraSelect, AudioSeparation, easy showAnything, WanVideoDecode, WanVideoVAELoader, MathExpression|pysssss, MathExpression|pysssss, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoContextOptions, DownloadAndLoadWav2VecModel, easy showAnything, Audio Cut (mtb), CM_FloatToNumber, CM_NumberToFloat, PreviewAudio, Float, Reroute, LoadAudio, Float, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, MultiTalkWav2VecEmbeds, CR Text, PreviewImage, easy showAnything, LoadImage, MultiTalkModelLoader, WanVideoModelLoader, WanVideoSampler]
patterns: []
missing: []
---

# 数字人/数字人/Multi_InfiniteTalk （wan2.1测试-人物偏油）_1966047524211650562.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Multi_InfiniteTalk （wan2.1测试-人物偏油）_1966047524211650562.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `AudioSeparation`
- `easy showAnything`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoContextOptions`
- `DownloadAndLoadWav2VecModel`
- `easy showAnything`
- `Audio Cut (mtb)`
- `CM_FloatToNumber`
- `CM_NumberToFloat`
- `PreviewAudio`
- `Float`
- `Reroute`
- `LoadAudio`
- `Float`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `MultiTalkWav2VecEmbeds`
- `CR Text`
- `PreviewImage`
- `easy showAnything`
- `LoadImage`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **85%**（28/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`AudioSeparation`、`WanVideoDecode`、`WanVideoVAELoader`、`MathExpression|pysssss`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoContextOptions`、`DownloadAndLoadWav2VecModel`、`Audio Cut (mtb)`、`CM_FloatToNumber`、`CM_NumberToFloat`、`PreviewAudio`、`Float`、`LoadAudio`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`MultiTalkWav2VecEmbeds`、`CR Text`、`LoadImage`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

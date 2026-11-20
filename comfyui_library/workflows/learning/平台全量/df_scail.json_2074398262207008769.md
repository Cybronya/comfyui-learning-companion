---
key: 平台全量/df_scail.json_2074398262207008769.json
name: df_scail.json_2074398262207008769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/df_scail.json_2074398262207008769.json
hash: b69581a59e2fd24a
coverage: 0.911765
learned_at: 2026-11-14 01:10:03
nodes: [PrimitiveString, easy int, WanVideoEncode, MultiTalkModelLoader, CLIPVisionLoader, DownloadAndLoadWav2VecModel, WanVideoVAELoader, MelBandRoFormerModelLoader, WanVideoLoraSelect, AudioCropProcessUTK, WanVideoModelLoader, WanVideoBlockSwap, GetImageRangeFromBatch, LoadWanVideoT5TextEncoder, WanVideoTextEncode, MathExpression|pysssss, easy int, PreviewAny, MultiTalkWav2VecEmbeds, MelBandRoFormerSampler, AudioCrop, WanVideoDecode, PrimitiveString, CustomAddLabel, LayerUtility: ImageScaleByAspectRatio V2, CM_IntToFloat, WanVideoClipVisionEncode, GetImageRangeFromBatch, WanVideoSampler, WanVideoImageToVideoMultiTalk, CR Text, VHS_LoadVideo, LoadAudio, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/df_scail.json_2074398262207008769.json

> 来源文件 `comfyui_library/workflows/平台全量/df_scail.json_2074398262207008769.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `PrimitiveString`
- `easy int`
- `WanVideoEncode`
- `MultiTalkModelLoader`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `MelBandRoFormerModelLoader`
- `WanVideoLoraSelect`
- `AudioCropProcessUTK`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `GetImageRangeFromBatch`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `MathExpression|pysssss`
- `easy int`
- `PreviewAny`
- `MultiTalkWav2VecEmbeds`
- `MelBandRoFormerSampler` ★核心
- `AudioCrop`
- `WanVideoDecode`
- `PrimitiveString`
- `CustomAddLabel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CM_IntToFloat`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `CR Text`
- `VHS_LoadVideo`
- `LoadAudio`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`easy int`、`WanVideoEncode`、`MultiTalkModelLoader`、`CLIPVisionLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`MelBandRoFormerModelLoader`、`WanVideoLoraSelect`、`AudioCropProcessUTK`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`GetImageRangeFromBatch`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`MathExpression|pysssss`、`MultiTalkWav2VecEmbeds`、`MelBandRoFormerSampler`、`AudioCrop`、`WanVideoDecode`、`CustomAddLabel`、`LayerUtility: ImageScaleByAspectRatio V2`、`CM_IntToFloat`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`CR Text`、`VHS_LoadVideo`、`LoadAudio`、`VHS_VideoCombine`

**用到的条目**：MelBandRoFormerSampler、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader

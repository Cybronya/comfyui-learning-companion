---
key: 视频生成/图生视频/多图视频w-a-n 2.2 自用_2037840182996639745.json
name: 多图视频w-a-n 2.2 自用_2037840182996639745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037840182996639745.json
hash: 0774f1e51c310fb4
coverage: 0.974359
learned_at: 2026-10-15 22:35:59
nodes: [ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, easy forLoopEnd, easy anythingIndexSwitch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LayerUtility: PurgeVRAM V2, ImpactInt, ImpactInt, TurboWanModelLoader, TurboWanModelLoader, AppendImageBatch, TurboWanVAELoader, CLIPTextEncode, easy forLoopStart, CLIPLoader, ImageResizeKJv2, LoadAudio, CR Text, ProcessString, JjkText, easy promptLine, CR Text Concatenate, VHS_VideoCombine, TurboDiffusionI2VSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/多图视频w-a-n 2.2 自用_2037840182996639745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037840182996639745.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（39 个）：
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `easy forLoopEnd`
- `easy anythingIndexSwitch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `ImpactInt`
- `ImpactInt`
- `TurboWanModelLoader`
- `TurboWanModelLoader`
- `AppendImageBatch`
- `TurboWanVAELoader`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `CLIPLoader`
- `ImageResizeKJv2`
- `LoadAudio`
- `CR Text`
- `ProcessString`
- `JjkText`
- `easy promptLine`
- `CR Text Concatenate`
- `VHS_VideoCombine`
- `TurboDiffusionI2VSampler` ★核心

## 知识

覆盖率 **97%**（38/39）

**有卡**：`ImageFromBatch+`、`easy forLoopEnd`、`easy anythingIndexSwitch`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`ImpactInt`、`TurboWanModelLoader`、`AppendImageBatch`、`TurboWanVAELoader`、`CLIPTextEncode`、`easy forLoopStart`、`CLIPLoader`、`ImageResizeKJv2`、`LoadAudio`、`CR Text`、`ProcessString`、`easy promptLine`、`CR Text Concatenate`、`VHS_VideoCombine`、`TurboDiffusionI2VSampler`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、TurboDiffusionI2VSampler、TurboWanVAELoader、easy promptLine、ImageResizeKJv2、ImpactInt

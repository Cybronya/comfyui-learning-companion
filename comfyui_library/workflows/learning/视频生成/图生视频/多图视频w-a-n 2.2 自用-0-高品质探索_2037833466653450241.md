---
key: 视频生成/图生视频/多图视频w-a-n 2.2 自用-0-高品质探索_2037833466653450241.json
name: 多图视频w-a-n 2.2 自用-0-高品质探索_2037833466653450241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多图视频w-a-n 2.2 自用-0-高品质探索_2037833466653450241.json
hash: b4ced6b71408ab9c
coverage: 0.974359
learned_at: 2026-10-15 22:35:59
nodes: [ImpactInt, ImpactInt, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, LoadAudio, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, easy forLoopEnd, easy anythingIndexSwitch, CR Text, AppendImageBatch, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LayerUtility: PurgeVRAM V2, TurboWanModelLoader, TurboWanVAELoader, TurboWanModelLoader, CLIPLoader, VHS_VideoCombine, TurboDiffusionI2VSampler, CLIPTextEncode, easy forLoopStart, ProcessString, easy promptLine, JjkText, CR Text Concatenate]
patterns: []
missing: []
---

# 视频生成/图生视频/多图视频w-a-n 2.2 自用-0-高品质探索_2037833466653450241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037833466653450241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（39 个）：
- `ImpactInt`
- `ImpactInt`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `LoadAudio`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `easy forLoopEnd`
- `easy anythingIndexSwitch`
- `CR Text`
- `AppendImageBatch`
- `ImageResizeKJv2`
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
- `TurboWanModelLoader`
- `TurboWanVAELoader`
- `TurboWanModelLoader`
- `CLIPLoader`
- `VHS_VideoCombine`
- `TurboDiffusionI2VSampler` ★核心
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `ProcessString`
- `easy promptLine`
- `JjkText`
- `CR Text Concatenate`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`ImpactInt`、`ImageFromBatch+`、`LoadAudio`、`easy forLoopEnd`、`easy anythingIndexSwitch`、`CR Text`、`AppendImageBatch`、`ImageResizeKJv2`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`TurboWanModelLoader`、`TurboWanVAELoader`、`CLIPLoader`、`VHS_VideoCombine`、`TurboDiffusionI2VSampler`、`CLIPTextEncode`、`easy forLoopStart`、`ProcessString`、`easy promptLine`、`CR Text Concatenate`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、TurboDiffusionI2VSampler、TurboWanVAELoader、easy promptLine、ImageResizeKJv2、ImpactInt

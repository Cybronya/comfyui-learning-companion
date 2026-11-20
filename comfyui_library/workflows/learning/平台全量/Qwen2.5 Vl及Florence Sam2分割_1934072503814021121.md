---
key: 平台全量/Qwen2.5 Vl及Florence Sam2分割_1934072503814021121.json
name: Qwen2.5 Vl及Florence Sam2分割_1934072503814021121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2.5 Vl及Florence Sam2分割_1934072503814021121.json
hash: 18d42a192610a05f
coverage: 0.791667
learned_at: 2026-11-14 00:52:24
nodes: [LayerUtility: PurgeVRAM, MaskToImage, PreviewImage, LayerMask: LoadFlorence2Model, LayerUtility: PurgeVRAM, LayerMask: SAM2UltraV2, MaskToImage, BBoxesToSAM2, easy showAnything, LayerMask: LoadSAM2Model, SaveImage, LayerUtility: PurgeVRAM, LayerMask: SAM2UltraV2, LayerMask: LoadSAM2Model, LayerMask: ObjectDetectorFL2, PreviewImage, LayerUtility: PurgeVRAM, DownloadAndLoadQwenModel, SaveImage, LoadImage, QwenVLDetection, CR Prompt Text, Note, Note]
patterns: []
missing: []
---

# 平台全量/Qwen2.5 Vl及Florence Sam2分割_1934072503814021121.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2.5 Vl及Florence Sam2分割_1934072503814021121.json`

## 结构

**生成流程**：Output → Other

**节点**（24 个）：
- `LayerUtility: PurgeVRAM`
- `MaskToImage`
- `PreviewImage`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: PurgeVRAM`
- `LayerMask: SAM2UltraV2`
- `MaskToImage`
- `BBoxesToSAM2`
- `easy showAnything`
- `LayerMask: LoadSAM2Model`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `LayerMask: SAM2UltraV2`
- `LayerMask: LoadSAM2Model`
- `LayerMask: ObjectDetectorFL2`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `DownloadAndLoadQwenModel`
- `SaveImage`
- `LoadImage`
- `QwenVLDetection`
- `CR Prompt Text`
- `Note`
- `Note`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`LayerUtility: PurgeVRAM`、`MaskToImage`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2UltraV2`、`BBoxesToSAM2`、`LayerMask: LoadSAM2Model`、`SaveImage`、`LayerMask: ObjectDetectorFL2`、`DownloadAndLoadQwenModel`、`LoadImage`、`QwenVLDetection`、`CR Prompt Text`

**用到的条目**：LoadImage、CR Prompt Text、SaveImage、BBoxesToSAM2、DownloadAndLoadQwenModel、LayerMask: LoadFlorence2Model、LayerMask: LoadSAM2Model、LayerMask: ObjectDetectorFL2

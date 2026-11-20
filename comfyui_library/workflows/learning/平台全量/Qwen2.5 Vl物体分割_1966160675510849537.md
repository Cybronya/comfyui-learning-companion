---
key: 平台全量/Qwen2.5 Vl物体分割_1966160675510849537.json
name: Qwen2.5 Vl物体分割_1966160675510849537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2.5 Vl物体分割_1966160675510849537.json
hash: 759e92b9ba1e010f
coverage: 0.8
learned_at: 2026-11-14 00:52:24
nodes: [LayerUtility: PurgeVRAM, DownloadAndLoadQwenModel, LayerUtility: PurgeVRAM, easy showAnything, PreviewImage, QwenVLDetection, CR Prompt Text, PreviewImage, BBoxesToSAM2, MaskToImage, LayerMask: LoadSAM2Model, SaveImage, LoadImage, ImageConcanate, LayerMask: SAM2UltraV2]
patterns: []
missing: []
---

# 平台全量/Qwen2.5 Vl物体分割_1966160675510849537.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2.5 Vl物体分割_1966160675510849537.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（15 个）：
- `LayerUtility: PurgeVRAM`
- `DownloadAndLoadQwenModel`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `PreviewImage`
- `QwenVLDetection`
- `CR Prompt Text`
- `PreviewImage`
- `BBoxesToSAM2`
- `MaskToImage`
- `LayerMask: LoadSAM2Model`
- `SaveImage`
- `LoadImage`
- `ImageConcanate`
- `LayerMask: SAM2UltraV2`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`LayerUtility: PurgeVRAM`、`DownloadAndLoadQwenModel`、`QwenVLDetection`、`CR Prompt Text`、`BBoxesToSAM2`、`MaskToImage`、`LayerMask: LoadSAM2Model`、`SaveImage`、`LoadImage`、`ImageConcanate`、`LayerMask: SAM2UltraV2`

**用到的条目**：LoadImage、CR Prompt Text、SaveImage、BBoxesToSAM2、DownloadAndLoadQwenModel、ImageConcanate、LayerMask: LoadSAM2Model、LayerMask: SAM2UltraV2

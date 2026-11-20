---
key: 平台全量/批量_一键抠图获取透明图像 (SegmentAnything_Ultra_V2)_1985601847018901506.json
name: 批量_一键抠图获取透明图像 (SegmentAnything_Ultra_V2)_1985601847018901506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/批量_一键抠图获取透明图像 (SegmentAnything_Ultra_V2)_1985601847018901506.json
hash: fb6330ece86249c6
coverage: 0.8125
learned_at: 2026-11-14 02:05:27
nodes: [TransparentImage, PreviewImage, SAMLoader, GroundingDinoModelLoader (segment anything), MaskToImage, LoadImage, GroundingDinoSAMSegment (segment anything), MaskToImage, SaveImage, SaveImage, LoadImage, SaveImage, TransparentImage, Note, Note, LayerMask: SegmentAnythingUltra V2]
patterns: []
missing: []
---

# 平台全量/批量_一键抠图获取透明图像 (SegmentAnything_Ultra_V2)_1985601847018901506.json

> 来源文件 `comfyui_library/workflows/平台全量/批量_一键抠图获取透明图像 (SegmentAnything_Ultra_V2)_1985601847018901506.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（16 个）：
- `TransparentImage`
- `PreviewImage`
- `SAMLoader`
- `GroundingDinoModelLoader (segment anything)`
- `MaskToImage`
- `LoadImage`
- `GroundingDinoSAMSegment (segment anything)`
- `MaskToImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `TransparentImage`
- `Note`
- `Note`
- `LayerMask: SegmentAnythingUltra V2`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`TransparentImage`、`SAMLoader`、`GroundingDinoModelLoader (segment anything)`、`MaskToImage`、`LoadImage`、`GroundingDinoSAMSegment (segment anything)`、`SaveImage`、`LayerMask: SegmentAnythingUltra V2`

**用到的条目**：LoadImage、SaveImage、GroundingDinoModelLoader (segment anything)、GroundingDinoSAMSegment (segment anything)、LayerMask: SegmentAnythingUltra V2、MaskToImage、SAMLoader、TransparentImage

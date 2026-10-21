---
key: 图片生成/图生图/sgm2.5抠图测试_2096796598339727362.json
name: sgm2.5抠图测试_2096796598339727362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/sgm2.5抠图测试_2096796598339727362.json
hash: 6f71a38f85d71c2d
coverage: 0.75
learned_at: 2026-10-21 00:46:28
nodes: [SetNode, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerMask: SegmentAnythingUltra V2, SaveImage, LayerUtility: ImageCombineAlpha, JjkText]
patterns: []
missing: []
---

# 图片生成/图生图/sgm2.5抠图测试_2096796598339727362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/sgm2.5抠图测试_2096796598339727362.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `SetNode`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V2`
- `SaveImage`
- `LayerUtility: ImageCombineAlpha`
- `JjkText`

## 知识

覆盖率 **75%**（6/8）

**有卡**：`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LayerMask: SegmentAnythingUltra V2`、`SaveImage`、`LayerUtility: ImageCombineAlpha`

**用到的条目**：LoadImage、SaveImage、LayerMask: SegmentAnythingUltra V2、LayerUtility: ImageCombineAlpha、LayerUtility: ImageRemoveAlpha、LayerUtility: ImageScaleByAspectRatio V2、sd15-t2i-basic、sd15-t2i-lora

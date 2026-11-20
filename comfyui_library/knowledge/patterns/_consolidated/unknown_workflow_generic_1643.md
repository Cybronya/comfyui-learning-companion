---
name: unknown_workflow_generic_1643
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7905
common_nodes: [ArgosTranslateTextNode, Image Comparer (rgthree), LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorPicker, LayerUtility: ImageCombineAlpha, LayerUtility: ImageRemoveAlpha, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/【商用】服装一键抠图_1926590900036866049.json, 平台全量/SegmentAnything 指定物体抠图_1920319941298556930.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1643

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【商用】服装一键抠图_1926590900036866049.json、平台全量/SegmentAnything 指定物体抠图_1920319941298556930.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `ArgosTranslateTextNode`
- `Image Comparer (rgthree)`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageCombineAlpha`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageInterrogator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

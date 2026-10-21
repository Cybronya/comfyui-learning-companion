---
name: unknown_workflow_generic_358
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.80925
common_nodes: [ImageConcanate, LoadImage, RH_ComfyFluxKontext, SaveImage]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1936979411319050242.json, 图片生成/文生图/1937014343026266114.json, 图片生成/文生图/1938480294855139329.json, 视频生成/图生视频/1928633296190652418.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_358

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1936979411319050242.json、图片生成/文生图/1937014343026266114.json、图片生成/文生图/1938480294855139329.json、视频生成/图生视频/1928633296190652418.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageConcanate`
- `LoadImage`
- `RH_ComfyFluxKontext`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2

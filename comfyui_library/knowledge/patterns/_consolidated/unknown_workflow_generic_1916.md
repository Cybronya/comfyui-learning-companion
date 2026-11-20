---
name: unknown_workflow_generic_1916
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.923
common_nodes: [LayerMask: MaskPreview, LayerMask: PixelSpread, LayerMask: RemBgUltra, LoadImage, SaveImage]
problems: []
missing: []
members: [平台全量/rembg ultra背景移除节点示例 rembg_ultra_example_1899806892221149186.json, 平台全量/像素扩展节点示例 pixel_spread_example_1899805285609779202.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1916

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/rembg ultra背景移除节点示例 rembg_ultra_example_1899806892221149186.json、平台全量/像素扩展节点示例 pixel_spread_example_1899805285609779202.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerMask: MaskPreview`
- `LayerMask: PixelSpread`
- `LayerMask: RemBgUltra`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Remove Background Rembg (mtb)` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

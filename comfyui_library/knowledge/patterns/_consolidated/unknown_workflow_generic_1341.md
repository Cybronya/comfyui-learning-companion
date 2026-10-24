---
name: unknown_workflow_generic_1341
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [LoadImage, RH_RhartImageG25FlareImageToImage, RH_RhartImageG25FlareTextToImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/全能图片G2.5-全能图片G-Image-2.5 Flare-经济版-图生图_2101540406692503554.json, 图片生成/文生图/全能图片G+IMAGE2.5图片生成经济版_2100128306459926530.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1341

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能图片G2.5-全能图片G-Image-2.5 Flare-经济版-图生图_2101540406692503554.json、图片生成/文生图/全能图片G+IMAGE2.5图片生成经济版_2100128306459926530.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `RH_RhartImageG25FlareImageToImage`
- `RH_RhartImageG25FlareTextToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

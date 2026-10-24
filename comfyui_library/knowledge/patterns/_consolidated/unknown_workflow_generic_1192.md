---
name: unknown_workflow_generic_1192
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [LoadImage, PreviewImage, RH_RhartImageG25OfficialTokenSunburstTextToImage, SaveImage, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/反推提示词/全能图片 G-Image-2.5 Flare｜轻量快速版｜文生图+图生图(图片编辑)_2098218264106201090.json, 图片生成/反推提示词/全能图片 全能图片G-Image-2.5 Sunburst｜高精旗舰版｜文生图+图生图(图片编辑)_2098237558626017281.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1192

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/全能图片 G-Image-2.5 Flare｜轻量快速版｜文生图+图生图(图片编辑)_2098218264106201090.json、图片生成/反推提示词/全能图片 全能图片G-Image-2.5 Sunburst｜高精旗舰版｜文生图+图生图(图片编辑)_2098237558626017281.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `RH_RhartImageG25OfficialTokenSunburstTextToImage`
- `SaveImage`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 1/2 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

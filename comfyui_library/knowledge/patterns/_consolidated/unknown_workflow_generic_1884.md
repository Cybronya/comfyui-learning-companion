---
name: unknown_workflow_generic_1884
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [APISR_ModelLoader_Zho, APISR_Zho, Image Comparer (rgthree), LoadImage, SaveImage]
problems: []
missing: []
members: [平台全量/APISR专门针对动漫的高清放大_1972627989563396097.json, 平台全量/二次元图片使用专用放大模型放大_2042121843716399106.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1884

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/APISR专门针对动漫的高清放大_1972627989563396097.json、平台全量/二次元图片使用专用放大模型放大_2042121843716399106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `APISR_ModelLoader_Zho`
- `APISR_Zho`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

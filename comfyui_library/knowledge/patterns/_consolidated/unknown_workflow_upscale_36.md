---
name: unknown_workflow_upscale_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [Google-Gemini-PL, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Gemini 2.0 细节修改+高清放大_1904715758629519362.json, 图片生成/文生图/谷歌Gemini生图_1912139284466597890.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Gemini 2.0 细节修改+高清放大_1904715758629519362.json、图片生成/文生图/谷歌Gemini生图_1912139284466597890.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `Google-Gemini-PL`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

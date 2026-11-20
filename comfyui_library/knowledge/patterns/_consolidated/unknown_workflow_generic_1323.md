---
name: unknown_workflow_generic_1323
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8035
common_nodes: [LoadVideo, RH_LLMAPI_Pro_Node, easy saveText, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/视频反推-gemini_2039620935526912001.json, 数字人/数字人/视频提示词反推 g 3.5 参考提示词提取_2088789079856074753.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1323

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/视频反推-gemini_2039620935526912001.json、数字人/数字人/视频提示词反推 g 3.5 参考提示词提取_2088789079856074753.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadVideo`
- `RH_LLMAPI_Pro_Node`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `SaveVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_generic_1323
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7915
common_nodes: [JjkText, LoadImage, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/全能分镜一致性风格 _ gemini-3.1_2076593725102452738.json, 视频生成/图生视频/S1-1 牛叉产品特效炸裂视频，参考十六宫格底图  产品特效_2050616496979755010.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1323

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能分镜一致性风格 _ gemini-3.1_2076593725102452738.json、视频生成/图生视频/S1-1 牛叉产品特效炸裂视频，参考十六宫格底图  产品特效_2050616496979755010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `JjkText`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

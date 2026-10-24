---
name: unknown_workflow_generic_1211
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7425
common_nodes: [CR Text, CR Text Concatenate, CR Text Replace, Fast Groups Muter (rgthree), GetNode, ImageTile+, ImpactMakeImageBatch, LoadImage, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, SaveImage, SetNode, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/AI漫剧分镜_2026825510570958849.json, 视频生成/图生视频/AI分镜图绘制_2022161330945396737.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1211

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/AI漫剧分镜_2026825510570958849.json、视频生成/图生视频/AI分镜图绘制_2022161330945396737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageTile+`
- `ImpactMakeImageBatch`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `SetNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

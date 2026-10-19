---
name: unknown_workflow_generic_302
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7835
common_nodes: [CreateVideo, GetVideoComponents, PrimitiveFloat, SaveVideo, VHS_LoadVideo, Video Slice]
problems: []
missing: []
members: [视频生成/图生视频/AI丝滑慢动作-RIFE慢放工作流_2094993897243107330.json, 视频生成/图生视频/AI视频换脸-ReActor逐帧工作流_2095018885564157953.json, 视频生成/图生视频/FlashVSR视频超分工作流_2094999239066738689.json, 视频生成/图生视频/视频补帧到60帧-RIFE工作流_2094993862648492034.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_302

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/AI丝滑慢动作-RIFE慢放工作流_2094993897243107330.json、视频生成/图生视频/AI视频换脸-ReActor逐帧工作流_2095018885564157953.json、视频生成/图生视频/FlashVSR视频超分工作流_2094999239066738689.json、视频生成/图生视频/视频补帧到60帧-RIFE工作流_2094993862648492034.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateVideo`
- `GetVideoComponents`
- `PrimitiveFloat`
- `SaveVideo`
- `VHS_LoadVideo`
- `Video Slice`

**可变部分**（部分 workflow 才有）：
- `FL_RIFE` —— 2/4 个有
- `FlashVSRNode` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `ReActorFaceSwap` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

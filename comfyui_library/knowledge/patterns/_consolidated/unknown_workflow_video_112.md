---
name: unknown_workflow_video_112
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.887
common_nodes: [CR Text, CR Value, ImageConcanate, ImageResizeKJ, LoadImage, RIFE VFI, ReActorFaceSwap, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/自用一键换脸工作流_1996420197084962817.json, 视频生成/图生视频/视频换脸+补帧 精准版_2041860257923735554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_112

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/自用一键换脸工作流_1996420197084962817.json、视频生成/图生视频/视频换脸+补帧 精准版_2041860257923735554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CR Value`
- `ImageConcanate`
- `ImageResizeKJ`
- `LoadImage`
- `RIFE VFI`
- `ReActorFaceSwap`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

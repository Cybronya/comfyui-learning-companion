---
name: unknown_workflow_face_detailer_clip_checkpoint
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.720333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, FaceDetailer, Image Comparer (rgthree), LoadImage, SaveImage, UltralyticsDetectorProvider]
problems: []
missing: []
members: [图片生成/图生图/人脸修复（写实）_1935517890713931778.json, 图片生成/图生图/手面部修复工作流_1973297865466490881.json, 图片生成/图生图/脸部手部修复工作流_1988886258426458114.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人脸修复（写实）_1935517890713931778.json、图片生成/图生图/手面部修复工作流_1973297865466490881.json、图片生成/图生图/脸部手部修复工作流_1988886258426458114.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `FaceDetailer`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `UltralyticsDetectorProvider`

**可变部分**（部分 workflow 才有）：
- `easy hiresFix` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

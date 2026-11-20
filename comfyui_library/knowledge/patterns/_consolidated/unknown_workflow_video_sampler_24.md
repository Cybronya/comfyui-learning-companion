---
name: unknown_workflow_video_sampler_24
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.939333
common_nodes: [DownloadAndLoadMimicMotionModel, ImageResizeKJ, LoadImage, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/美女跳舞视频转绘_1900150494789103617.json, 视频生成/图生视频/视频动作迁移—手指舞_1901488680866062338.json, "视频生成/图生视频/让图片跳舞,图片转视频_1883776618446602242.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/美女跳舞视频转绘_1900150494789103617.json、视频生成/图生视频/视频动作迁移—手指舞_1901488680866062338.json、视频生成/图生视频/让图片跳舞,图片转视频_1883776618446602242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadMimicMotionModel`
- `ImageResizeKJ`
- `LoadImage`
- `MimicMotionDecode`
- `MimicMotionGetPoses`
- `MimicMotionSampler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `ReActorFaceSwap` —— 2/3 个有
- `Image Crop Face` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

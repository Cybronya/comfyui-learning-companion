---
name: unknown_workflow_video_sampler_35
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9118
common_nodes: [DownloadAndLoadMimicMotionModel, ImageResizeKJ, LoadImage, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/优化版图转视频加换脸修复加视频放大_1897825295863336961.json, 视频生成/图生视频/图生视频转绘-动作迁移_1896079729521262594.json, 视频生成/图生视频/美女跳舞视频转绘_1900150494789103617.json, 视频生成/图生视频/视频动作迁移—手指舞_1901488680866062338.json, "视频生成/图生视频/让图片跳舞,图片转视频_1883776618446602242.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_35

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/优化版图转视频加换脸修复加视频放大_1897825295863336961.json、视频生成/图生视频/图生视频转绘-动作迁移_1896079729521262594.json、视频生成/图生视频/美女跳舞视频转绘_1900150494789103617.json、视频生成/图生视频/视频动作迁移—手指舞_1901488680866062338.json、视频生成/图生视频/让图片跳舞,图片转视频_1883776618446602242.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `DownloadAndLoadMimicMotionModel`
- `ImageResizeKJ`
- `LoadImage`
- `MimicMotionDecode`
- `MimicMotionGetPoses`
- `MimicMotionSampler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `ReActorFaceSwap` —— 3/5 个有
- `RIFE VFI` —— 2/5 个有
- `CR Upscale Image` —— 1/5 个有
- `Image Crop Face` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `Int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

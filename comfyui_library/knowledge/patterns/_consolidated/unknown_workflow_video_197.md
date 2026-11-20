---
name: unknown_workflow_video_197
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [GPENO Face Restoration, ImageConcatMulti, ImageListToImageBatch, ImpactImageBatchToImageList, JWImageResizeByLongerSide, LayerUtility: PurgeVRAM, LoadImage, ReActorFaceSwap, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/GpenO超快速视频换脸工作流修复版V3_1915060372594982913.json, 视频生成/图生视频/【10秒生成】GpenO 视频换脸工作流修复版_1915223199347576834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_197

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/GpenO超快速视频换脸工作流修复版V3_1915060372594982913.json、视频生成/图生视频/【10秒生成】GpenO 视频换脸工作流修复版_1915223199347576834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `GPENO Face Restoration`
- `ImageConcatMulti`
- `ImageListToImageBatch`
- `ImpactImageBatchToImageList`
- `JWImageResizeByLongerSide`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ReActorFaceSwap`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

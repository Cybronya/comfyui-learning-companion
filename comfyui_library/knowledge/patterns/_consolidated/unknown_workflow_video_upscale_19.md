---
name: unknown_workflow_video_upscale_19
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CR Upscale Image, ImageListToBatch+, ImpactImageBatchToImageList, RIFE VFI, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/wan2.2视频放大修复插帧_1965648278257811457.json, 平台全量/视频放大快速版_1938448833854504961.json, 平台全量/视频放大插帧（简单快速版）_1903035574230622209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/wan2.2视频放大修复插帧_1965648278257811457.json、平台全量/视频放大快速版_1938448833854504961.json、平台全量/视频放大插帧（简单快速版）_1903035574230622209.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Upscale Image`
- `ImageListToBatch+`
- `ImpactImageBatchToImageList`
- `RIFE VFI`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DF_Int_to_Float` —— 2/3 个有
- `Int` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

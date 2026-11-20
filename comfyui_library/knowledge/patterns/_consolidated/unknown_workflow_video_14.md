---
name: unknown_workflow_video_14
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8222
common_nodes: [ImageScaleToTotalPixels, SeedVR2, SeedVR2BlockSwap, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/SeedVR2 支持2K视频放大 v1_2104797844346597378.json, 平台全量/SeedVR2 视频放大工作流（Plus模式支持2K放大）_2097239079011311617.json, 平台全量/自用4K高清放大8-10min：SeedVR2_2011720924340424706.json, 平台全量/视频放大 SeedVR2（2K-Plus模式可运行）_2082739528892239874.json, 平台全量/视频高清化_1988184873150103553.json, 平台全量/视频高清工作流_2094016061862666241.json, 平台全量/视频高清放大+补帧_2091178600597909505.json, 平台全量/视频高清放大+补帧_2092806350140170241.json, 平台全量/视频高清放大_2074696403221303297.json, 平台全量/💗视频放大补帧 SeedVR2+Video_2077934448129175553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_14

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/SeedVR2 支持2K视频放大 v1_2104797844346597378.json、平台全量/SeedVR2 视频放大工作流（Plus模式支持2K放大）_2097239079011311617.json、平台全量/自用4K高清放大8-10min：SeedVR2_2011720924340424706.json、平台全量/视频放大 SeedVR2（2K-Plus模式可运行）_2082739528892239874.json、平台全量/视频高清化_1988184873150103553.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `ImageScaleToTotalPixels`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SeedVR2ExtraArgs` —— 9/10 个有
- `VHS_VideoInfoSource` —— 9/10 个有
- `PreviewImage` —— 7/10 个有
- `Int` —— 5/10 个有
- `MathExpression_UTK` —— 4/10 个有
- `RIFE VFI` —— 4/10 个有
- `SetNode` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImpactSleep` —— 1/10 个有
- `SaveImage` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

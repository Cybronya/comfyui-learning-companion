---
name: unknown_workflow_video_upscale_8
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.762
common_nodes: [PDIMAGE_LongerSize, RTXVideoSuperResolution, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/Vosr 2.0+RTX视频串联-超高清修复-minimax H3_2097507438240026626.json, 平台全量/Vosr 2.0修复视频像素视频超分修复_2097254372022505474.json, 平台全量/Vosr 2视频高清化｜极速版｜级联2K｜4K_2097096807590490113.json, 平台全量/Vosr_2视频高清化｜极速版｜级联2K｜4K_2100053709022650370.json, 平台全量/Vosr_2视频高清化｜极速版｜级联2K｜4K_2100134255883014146.json, 视频生成/文生视频/Vosr_2视频高清化｜极速版｜级联2K｜4K_2101627974746460161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_8

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Vosr 2.0+RTX视频串联-超高清修复-minimax H3_2097507438240026626.json、平台全量/Vosr 2.0修复视频像素视频超分修复_2097254372022505474.json、平台全量/Vosr 2视频高清化｜极速版｜级联2K｜4K_2097096807590490113.json、平台全量/Vosr_2视频高清化｜极速版｜级联2K｜4K_2100053709022650370.json、平台全量/Vosr_2视频高清化｜极速版｜级联2K｜4K_2100134255883014146.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `PDIMAGE_LongerSize`
- `RTXVideoSuperResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `PreviewImage` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `JindouyunShowAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

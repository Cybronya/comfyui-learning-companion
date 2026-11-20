---
name: unknown_workflow_video_sampler_17
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 1
common_nodes: [CM_FloatToInt, GetVideoComponents, LoadImage, LoadVideo, RunningHub_DreamID-V_Loader, RunningHub_DreamID-V_Sampler, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/DreamID-V视频换脸（不报错版）_2007392676399816706.json, 平台全量/极速视频换脸 DreamID-V视频换脸_2021037534406516737.json, 平台全量/视频真实换脸 DreamID-V 超强视频换脸_2017057144763322370.json, 数字人/数字人/DreamID-V视频换脸_2008974813620084738.json, 视频生成/图生视频/DreamID-V视频换脸  精准换脸 口形匹配_2011458263312769025.json, 视频生成/图生视频/DreamID-V视频换脸_2009239491415908354.json, 视频生成/图生视频/DreamID-V视频换脸_2029470335698997249.json, 视频生成/图生视频/视频换脸_2013142770868822018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_17

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/DreamID-V视频换脸（不报错版）_2007392676399816706.json、平台全量/极速视频换脸 DreamID-V视频换脸_2021037534406516737.json、平台全量/视频真实换脸 DreamID-V 超强视频换脸_2017057144763322370.json、数字人/数字人/DreamID-V视频换脸_2008974813620084738.json、视频生成/图生视频/DreamID-V视频换脸  精准换脸 口形匹配_2011458263312769025.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CM_FloatToInt`
- `GetVideoComponents`
- `LoadImage`
- `LoadVideo`
- `RunningHub_DreamID-V_Loader`
- `RunningHub_DreamID-V_Sampler`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `easy imageCount` —— 7/8 个有
- `INTConstant` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

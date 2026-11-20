---
name: unknown_workflow_video_sampler_26
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.806167
common_nodes: [Float to Int, GetVideoComponents, LoadImage, LoadVideo, MathExpression|pysssss, RunningHub_DreamID-V_Loader, RunningHub_DreamID-V_Sampler, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/03-23-01-WAN2.1-DreamID-V视频换脸_2009981518013272065.json, 平台全量/DreamID-V 最好的视频换脸工作流_2009115847930945537.json, 平台全量/DreamID-V视频换脸_2009098702660571138.json, 平台全量/全自动视频换脸_2029952563444981762.json, 平台全量/视频换脸术-加速版-DreamID-V_2011400317048463362.json, 视频生成/图生视频/DreamID-V视频换脸稳定加速版V4（支持非脸空帧）_2009864984473374722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_26

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/03-23-01-WAN2.1-DreamID-V视频换脸_2009981518013272065.json、平台全量/DreamID-V 最好的视频换脸工作流_2009115847930945537.json、平台全量/DreamID-V视频换脸_2009098702660571138.json、平台全量/全自动视频换脸_2029952563444981762.json、平台全量/视频换脸术-加速版-DreamID-V_2011400317048463362.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `Float to Int`
- `GetVideoComponents`
- `LoadImage`
- `LoadVideo`
- `MathExpression|pysssss`
- `RunningHub_DreamID-V_Loader`
- `RunningHub_DreamID-V_Sampler`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 5/6 个有
- `JWInteger` —— 5/6 个有
- `Float` —— 3/6 个有
- `easy showAnything` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `Int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

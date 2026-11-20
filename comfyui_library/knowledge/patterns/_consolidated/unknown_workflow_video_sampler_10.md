---
name: unknown_workflow_video_sampler_10
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.930083
common_nodes: [GetVideoComponents, LoadImage, LoadVideo, RunningHub_DreamID-V_Loader, RunningHub_DreamID-V_Sampler, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/DreamID-V 视频换脸 v1_2107471477367984129.json, 平台全量/DreamID-V 视频换脸_2032719842234605570.json, 平台全量/DreamID-V视频换脸_2009077486029639681.json, 平台全量/DreamID-V视频换脸_2031024374203031553.json, 平台全量/DreamID-V视频换脸_2068983255851954177.json, 平台全量/【Supermate】DreamID-V视频换脸工作流_2009039393289408513.json, 平台全量/一键视频换脸 DreamID-V_2010359099887722498.json, 数字人/数字人/DreamID-V 体验  Vvv-vsien_2010430951473553409.json, 数字人/数字人/视频一键换脸 DreamID_1989358478957441026.json, 视频生成/图生视频/DreamID-V视频换脸_2009145038378373122.json, 视频生成/图生视频/DreamID-V视频换脸_2009449357975756802.json, 视频生成/图生视频/DreamID-V视频换脸_2010268068085239809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_10

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/DreamID-V 视频换脸 v1_2107471477367984129.json、平台全量/DreamID-V 视频换脸_2032719842234605570.json、平台全量/DreamID-V视频换脸_2009077486029639681.json、平台全量/DreamID-V视频换脸_2031024374203031553.json、平台全量/DreamID-V视频换脸_2068983255851954177.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `GetVideoComponents`
- `LoadImage`
- `LoadVideo`
- `RunningHub_DreamID-V_Loader`
- `RunningHub_DreamID-V_Sampler`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 11/12 个有
- `easy imageCount` —— 10/12 个有
- `ImageConcanate` —— 9/12 个有
- `JWInteger` —— 9/12 个有
- `MathExpression|pysssss` —— 9/12 个有
- `RepeatImageBatch` —— 8/12 个有
- `ColorMatch` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `ToInt` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

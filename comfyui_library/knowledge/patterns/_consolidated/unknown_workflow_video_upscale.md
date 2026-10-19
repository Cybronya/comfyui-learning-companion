---
name: unknown_workflow_video_upscale
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.981444
common_nodes: [ImageUpscaleWithModel, LoadImage, RHBatchImages:, RunningHub_FramePack, SeargePromptText, UpscaleModelLoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1913267908083154945.json, 视频生成/图生视频/1913429514767036417.json, 视频生成/图生视频/1912930457355517954.json, 视频生成/图生视频/2042486846139142145.json, 视频生成/图生视频/2044579336837144578.json, 视频生成/图生视频/1934513539719786498.json, 视频生成/文生视频/1913945287872970754.json, 视频生成/文生视频/1934506893593440257.json, 视频生成/文生视频/1934534010339303425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1913267908083154945.json、视频生成/图生视频/1913429514767036417.json、视频生成/图生视频/1912930457355517954.json、视频生成/图生视频/2042486846139142145.json、视频生成/图生视频/2044579336837144578.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `RHBatchImages:`
- `RunningHub_FramePack`
- `SeargePromptText`
- `UpscaleModelLoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `ImageScale` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

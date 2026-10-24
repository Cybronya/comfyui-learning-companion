---
name: unknown_workflow_video_sampler_25
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8915
common_nodes: [AniCrafterLoader, AniCrafterPreImage, AniCrafterPreText, AniCrafterPreVideo, AniCrafterSampler, LoadImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/AniCrafter人物动作迁移_1945997546588434433.json, 视频生成/图生视频/AniCrafter人物动作迁移加速版V2_1947175186761822209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/AniCrafter人物动作迁移_1945997546588434433.json、视频生成/图生视频/AniCrafter人物动作迁移加速版V2_1947175186761822209.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AniCrafterLoader`
- `AniCrafterPreImage`
- `AniCrafterPreText`
- `AniCrafterPreVideo`
- `AniCrafterSampler`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

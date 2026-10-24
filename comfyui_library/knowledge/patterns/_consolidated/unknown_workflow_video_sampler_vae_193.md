---
name: unknown_workflow_video_sampler_vae_193
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/高清FusionX最强文生视频双倍加速版_1934524446843568130.json, 视频生成/文生视频/🤠【大炮视频】AniWan文生视频灵动加速版🤠_1945683257658888194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_193

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/高清FusionX最强文生视频双倍加速版_1934524446843568130.json、视频生成/文生视频/🤠【大炮视频】AniWan文生视频灵动加速版🤠_1945683257658888194.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `WanVideoFreeInitArgs` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_sampler_clip_199
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.957667
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXVConditioning, LTXVScheduler, SamplerCustom, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1899450200354672642.json, 视频生成/文生视频/最快AI视频模型 LTX  文生视频  UP 楚门的AI世界_1897435608137322497.json, 视频生成/文生视频/1897402731693592577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1899450200354672642.json、视频生成/文生视频/最快AI视频模型 LTX  文生视频  UP 楚门的AI世界_1897435608137322497.json、视频生成/文生视频/1897402731693592577.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVScheduler`
- `SamplerCustom`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 2/3 个有
- `CR Upscale Image` —— 1/3 个有
- `Int` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PatchModelPatcherOrder` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `SaveWEBM` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

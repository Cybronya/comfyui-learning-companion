---
name: unknown_workflow_video_sampler_clip_157
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.98325
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXVConditioning, LTXVScheduler, SamplerCustom, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX_文生视频_2099545589217325058.json, 视频生成/文生视频/1922112909130809345.json, 视频生成/文生视频/1920699444994441217.json, 视频生成/文生视频/1947954012728492034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/LTX_文生视频_2099545589217325058.json、视频生成/文生视频/1922112909130809345.json、视频生成/文生视频/1920699444994441217.json、视频生成/文生视频/1947954012728492034.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVScheduler`
- `SamplerCustom`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXAttnOverride` —— 1/4 个有
- `LTXPerturbedAttention` —— 1/4 个有
- `ModifyLTXModel` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

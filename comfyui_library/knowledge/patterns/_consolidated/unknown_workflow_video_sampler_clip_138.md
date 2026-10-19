---
name: unknown_workflow_video_sampler_clip_138
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.946
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXVConditioning, LTXVImgToVideo, LTXVPreprocess, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, LTXVScheduler, LoadImage, SamplerCustom, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1903736923179880450.json, 视频生成/图生视频/1897512765190262785.json, 视频生成/图生视频/1914129189279334401.json, 视频生成/文生视频/1897511691662348290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_138

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1903736923179880450.json、视频生成/图生视频/1897512765190262785.json、视频生成/图生视频/1914129189279334401.json、视频生成/文生视频/1897511691662348290.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVImgToVideo`
- `LTXVPreprocess`
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `LTXVScheduler`
- `LoadImage`
- `SamplerCustom`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Primitive integer [Crystools]` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `Primitive string [Crystools]` —— 2/4 个有
- `EmptyLTXVLatentVideo` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

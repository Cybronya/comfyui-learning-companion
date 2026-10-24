---
name: unknown_workflow_video_sampler_clip_272
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.88
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXVConditioning, LTXVImgToVideo, LTXVScheduler, LoadImage, SamplerCustom, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/All In One Custom Workflow IMG2Vid_1869245784851128321.json, 视频生成/文生视频/LTXV文生图生视频_2058503882573180929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_272

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/All In One Custom Workflow IMG2Vid_1869245784851128321.json、视频生成/文生视频/LTXV文生图生视频_2058503882573180929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVImgToVideo`
- `LTXVScheduler`
- `LoadImage`
- `SamplerCustom`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageCrop+` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

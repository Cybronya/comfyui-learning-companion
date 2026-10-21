---
name: unknown_workflow_video_sampler_clip_92
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.916667
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXVConditioning, LTXVScheduler, SamplerCustom, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2032350611932450818.json, 视频生成/图生视频/LTX  首尾帧视频 关键帧视频_1897656899377287170.json, 视频生成/图生视频/1934953354332151809.json, 视频生成/图生视频/2045019668942950401.json, 视频生成/文生视频/1934987573289000962.json, 视频生成/文生视频/1897448492304912386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2032350611932450818.json、视频生成/图生视频/LTX  首尾帧视频 关键帧视频_1897656899377287170.json、视频生成/图生视频/1934953354332151809.json、视频生成/图生视频/2045019668942950401.json、视频生成/文生视频/1934987573289000962.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVScheduler`
- `SamplerCustom`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVAddGuide` —— 5/6 个有
- `LTXVCropGuides` —— 5/6 个有
- `LTXVPreprocess` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `TextInput_` —— 3/6 个有
- `VAEDecode` —— 3/6 个有
- `VAEDecodeTiled` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `LTXVImgToVideo` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_sampler_clip_138
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92875
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAddGuide, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVScheduler, LoadImage, SamplerCustom, TextInput_, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/最快的视频生成模型 LTX-Video+首尾帧合成视频-StarAI_1898028219306856450.json, 视频生成/图生视频/LTX  首尾帧视频 关键帧视频 _测试_2032350611932450818.json, 视频生成/图生视频/LTX  首尾帧视频 关键帧视频_1897656899377287170.json, 视频生成/图生视频/图生视频LTX  首尾帧视频 关键帧视频_2045019668942950401.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_138

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/最快的视频生成模型 LTX-Video+首尾帧合成视频-StarAI_1898028219306856450.json、视频生成/图生视频/LTX  首尾帧视频 关键帧视频 _测试_2032350611932450818.json、视频生成/图生视频/LTX  首尾帧视频 关键帧视频_1897656899377287170.json、视频生成/图生视频/图生视频LTX  首尾帧视频 关键帧视频_2045019668942950401.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAddGuide`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LoadImage`
- `SamplerCustom`
- `TextInput_`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `PatchModelPatcherOrder` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

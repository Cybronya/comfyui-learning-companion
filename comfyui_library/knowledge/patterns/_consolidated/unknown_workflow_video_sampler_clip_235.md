---
name: unknown_workflow_video_sampler_clip_235
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.847
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetLatentRangeFromBatch, ImageScale, KSamplerSelect, LoadImage, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, ScheduledCFGGuidance, SplitSigmas, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ]
problems: []
missing: []
members: [平台全量/wan2.1图生视频带加速版8g显存可用_1909149443008901121.json, 视频生成/图生视频/万相Wan2.1图生视频_8G显存可用_捏捏乐特效_1900549940203134978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_235

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/wan2.1图生视频带加速版8g显存可用_1909149443008901121.json、视频生成/图生视频/万相Wan2.1图生视频_8G显存可用_捏捏乐特效_1900549940203134978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetLatentRangeFromBatch`
- `ImageScale`
- `KSamplerSelect`
- `LoadImage`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ScheduledCFGGuidance`
- `SplitSigmas`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerFilter: Sharp & Soft` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `Reroute (rgthree)` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

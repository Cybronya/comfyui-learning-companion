---
name: unknown_workflow_video_sampler_clip_238
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.831
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DisableNoise, GetImageSizeAndCount, HYFlowEditGuiderCFG, HYFlowEditSampler, HYReverseModelSamplingPred, Image Comparer (rgthree), ImageFromBatch+, ImageResizeKJ, LoadImage, SamplerCustomAdvanced, VAEDecodeTiled, VAEEncode, VAELoader, VHS_LoadVideo, VHS_MergeImages, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [平台全量/一键视频转绘flowedit方案_1906594887872221186.json, 平台全量/一键视频转绘flowedit方案_1943667999297404930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_238

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一键视频转绘flowedit方案_1906594887872221186.json、平台全量/一键视频转绘flowedit方案_1943667999297404930.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DisableNoise`
- `GetImageSizeAndCount`
- `HYFlowEditGuiderCFG`
- `HYFlowEditSampler`
- `HYReverseModelSamplingPred`
- `Image Comparer (rgthree)`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `LoadImage`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `EnhancedLoadDiffusionModel` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `TextInputBasic` —— 1/2 个有
- `TorchCompileModelWanVideo` —— 1/2 个有
- `TorchCompileModelWanVideoV2` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

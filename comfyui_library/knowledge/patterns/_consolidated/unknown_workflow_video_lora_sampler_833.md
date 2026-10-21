---
name: unknown_workflow_video_lora_sampler_833
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9145
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, FL_KsamplerPlus, FL_PathAnimator, GetImageSizeAndCount, ImageResizeKJ, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, TorchCompileModelWanVideo, UNETLoader, VAELoader, VHS_DuplicateImages, VHS_VideoCombine, WanTrackToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1929052305113432066.json, 视频生成/图生视频/2039588649964150785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_833

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1929052305113432066.json、视频生成/图生视频/2039588649964150785.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `FL_KsamplerPlus`
- `FL_PathAnimator`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `TorchCompileModelWanVideo`
- `UNETLoader`
- `VAELoader`
- `VHS_DuplicateImages`
- `VHS_VideoCombine`
- `WanTrackToVideo`

**可变部分**（部分 workflow 才有）：
- `AudioEncoderEncode` —— 1/2 个有
- `AudioEncoderLoader` —— 1/2 个有
- `WanSoundImageToVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

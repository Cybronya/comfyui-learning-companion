---
name: unknown_workflow_video_sampler_vae_185
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9275
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, HyVideoDecode, HyVideoEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoTextEmbedBridge, HyVideoVAELoader, ImageConcatMulti, LoadImage, PreviewImage, TextEncodeHunyuanVideo_ImageToVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/一键跨时空拥抱-混元图生视频_1946557222581362690.json, 视频生成/文生视频/2025-05-14 hyvideo_custom_1922219217268178946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_185

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/一键跨时空拥抱-混元图生视频_1946557222581362690.json、视频生成/文生视频/2025-05-14 hyvideo_custom_1922219217268178946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoTextEmbedBridge`
- `HyVideoVAELoader`
- `ImageConcatMulti`
- `LoadImage`
- `PreviewImage`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `HyVideoBlockSwap` —— 1/2 个有
- `HyVideoLoraSelect` —— 1/2 个有
- `HyVideoTorchCompileSettings` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `RMBG` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

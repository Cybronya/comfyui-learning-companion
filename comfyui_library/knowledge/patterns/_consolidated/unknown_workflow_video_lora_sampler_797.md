---
name: unknown_workflow_video_lora_sampler_797
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [CLIPVisionLoader, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SaveImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 FusionX ｜ Self-Forcing 极速图生视频_1935274607635267585.json, 视频生成/图生视频/Wan2.1-FusionX+lightx2v极速高质量图生视频_1935260517701177345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_797

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 FusionX ｜ Self-Forcing 极速图生视频_1935274607635267585.json、视频生成/图生视频/Wan2.1-FusionX+lightx2v极速高质量图生视频_1935260517701177345.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SaveImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `FILM VFI` —— 1/2 个有
- `Image Aspect Ratio` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Int` —— 1/2 个有
- `Logic Boolean` —— 1/2 个有
- `Number to Float` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

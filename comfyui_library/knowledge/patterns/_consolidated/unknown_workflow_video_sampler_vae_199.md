---
name: unknown_workflow_video_sampler_vae_199
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.963
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/🦖wan 2.1 MoviiGen 首尾帧_1932721199510081537.json, 视频生成/文生视频/Wan2.1首尾帧动画VACE+高清放大_1922107883666997249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_199

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/🦖wan 2.1 MoviiGen 首尾帧_1932721199510081537.json、视频生成/文生视频/Wan2.1首尾帧动画VACE+高清放大_1922107883666997249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ResizeLongestToNode` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

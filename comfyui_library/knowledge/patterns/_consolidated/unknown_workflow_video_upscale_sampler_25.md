---
name: unknown_workflow_video_upscale_sampler_25
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9525
common_nodes: [CR Upscale Image, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, RIFE VFI, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1万相1080P60帧图生视频KJ版（提示词优化+高清放大+插帧）_1900072045734932482.json, 视频生成/图生视频/万相1080P60帧图生视频360度旋转（360°旋转lora）_1900153764635095042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.1万相1080P60帧图生视频KJ版（提示词优化+高清放大+插帧）_1900072045734932482.json、视频生成/图生视频/万相1080P60帧图生视频360度旋转（360°旋转lora）_1900153764635095042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Upscale Image`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageSizeAndBatchSize` —— 1/2 个有
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_upscale_sampler_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9415
common_nodes: [FILM VFI, ImageScale, ImageUpscaleWithModel, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.1图生视频开源之光_1912762337353265153.json, 视频生成/图生视频/啊癫 通义万相wan2.1 超级大摆锤 图片跳舞_1914988219354574849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WAN2.1图生视频开源之光_1912762337353265153.json、视频生成/图生视频/啊癫 通义万相wan2.1 超级大摆锤 图片跳舞_1914988219354574849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `FILM VFI`
- `ImageScale`
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Aspect Ratio` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `Int` —— 1/2 个有
- `Logic Boolean` —— 1/2 个有
- `Number to Float` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

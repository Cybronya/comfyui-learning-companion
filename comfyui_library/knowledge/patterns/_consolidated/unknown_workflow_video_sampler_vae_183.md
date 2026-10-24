---
name: unknown_workflow_video_sampler_vae_183
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ImageConcatMulti, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], Primitive string [Crystools], VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1-Tile视频高清控制_1899280548576055298.json, 视频生成/图生视频/一键爆火热舞迁移(Wan2.1-KJ)_1895658256604266497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_183

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-Tile视频高清控制_1899280548576055298.json、视频生成/图生视频/一键爆火热舞迁移(Wan2.1-KJ)_1895658256604266497.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcatMulti`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `Primitive string [Crystools]`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageBlur` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageScaleDownToSize` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `WanVideoControlEmbeds` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

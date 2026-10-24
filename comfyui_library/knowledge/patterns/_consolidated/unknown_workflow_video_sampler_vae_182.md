---
name: unknown_workflow_video_sampler_vae_182
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.976
common_nodes: [GetImageSize+, ImagePadKJ, ImageResizeKJ, LoadWanVideoT5TextEncoder, MaskToImage, String Literal, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN-VACE（视频扩展）_1982061265277337602.json, 视频生成/文生视频/WAN2.2-AllInOne视频扩展_1963909570361966594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_182

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WAN-VACE（视频扩展）_1982061265277337602.json、视频生成/文生视频/WAN2.2-AllInOne视频扩展_1963909570361966594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize+`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `String Literal`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

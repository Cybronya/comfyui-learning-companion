---
name: unknown_workflow_video_sampler_vae_154
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.953667
common_nodes: [GetImageSize+, ImagePadKJ, ImageResizeKJ, LoadWanVideoT5TextEncoder, MaskToImage, String Literal, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: [String Literal, GetImageSize+]
members: [视频生成/图生视频/1982061265277337602.json, 视频生成/文生视频/1963909570361966594.json, 视频生成/文生视频/WAN2.2-AllInOne视频扩展_2072999602540027904.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_154

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1982061265277337602.json、视频生成/文生视频/1963909570361966594.json、视频生成/文生视频/WAN2.2-AllInOne视频扩展_2072999602540027904.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
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
- `GrowMaskWithBlur` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `WanVideoSetLoRAs` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、GetImageSize+

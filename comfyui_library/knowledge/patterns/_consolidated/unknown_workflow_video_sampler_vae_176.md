---
name: unknown_workflow_video_sampler_vae_176
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.667
common_nodes: [ImageConcatMulti, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/03-13-02-WAN2.1-元素融合生成视频-phantom_14B_1990781927823187970.json, 视频生成/图生视频/phantom加速60%稳定版视频编辑工作流_1916898231614111746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_176

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/03-13-02-WAN2.1-元素融合生成视频-phantom_14B_1990781927823187970.json、视频生成/图生视频/phantom加速60%稳定版视频编辑工作流_1916898231614111746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerMask: RemBgUltra` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoMagCache` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

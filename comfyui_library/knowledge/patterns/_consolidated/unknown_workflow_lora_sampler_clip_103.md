---
name: unknown_workflow_lora_sampler_clip_103
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9026
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, ConditioningZeroOut, CreateVideo, EmptyImage, GetImageSizeAndCount, ImageCompositeMasked, ImageFromBatch, ImageScaleToTotalPixels, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MaskPreview, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveBoolean, ResolutionSelector, SAM3_Detect, SAM3_TrackToMask, SAM3_VideoTrack, SaveVideo, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3_视频驱动角色替换2采工作流动作迁移角色替换_2114253541887004673.json, 视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2102585296163528705.json, 视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2107756778111983618.json, 视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2113781010742734849.json, 视频生成/图生视频/MiniMaxH3_视频驱动角色替换（2采工作流动作迁移角色替换）_2111280464731398146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3_视频驱动角色替换2采工作流动作迁移角色替换_2114253541887004673.json、视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2102585296163528705.json、视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2107756778111983618.json、视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2113781010742734849.json、视频生成/图生视频/MiniMaxH3_视频驱动角色替换（2采工作流动作迁移角色替换）_2111280464731398146.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `SAM3_Detect`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SaveVideo`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `DA3Inference` —— 3/5 个有
- `DA3Render` —— 3/5 个有
- `FeatherMask` —— 3/5 个有
- `GrowMask` —— 3/5 个有
- `LoadDA3Model` —— 3/5 个有
- `MiniMaxH3FunControlNetApply` —— 3/5 个有
- `ModelPatchLoader` —— 3/5 个有
- `PreviewImage` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.2 | 0.2 - 0.2 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.2，观测区间 0.2 - 0.2，3 个样本，取值集中（一致性 100%）

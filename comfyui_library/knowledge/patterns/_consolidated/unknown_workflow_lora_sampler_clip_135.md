---
name: unknown_workflow_lora_sampler_clip_135
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.903667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, ConditioningZeroOut, CreateVideo, EmptyImage, GetImageSizeAndCount, ImageCompositeMasked, ImageFromBatch, ImageScaleToTotalPixels, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MaskPreview, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveBoolean, ResolutionSelector, SAM3_Detect, SAM3_TrackToMask, SAM3_VideoTrack, SaveVideo, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2102585296163528705.json, 视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2107756778111983618.json, 视频生成/图生视频/MiniMaxH3_视频驱动角色替换（2采工作流动作迁移角色替换）_2111280464731398146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_135

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2102585296163528705.json、视频生成/图生视频/MiniMaxH3_视频驱动角色替换_2107756778111983618.json、视频生成/图生视频/MiniMaxH3_视频驱动角色替换（2采工作流动作迁移角色替换）_2111280464731398146.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
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
- `DA3Inference` —— 1/3 个有
- `DA3Render` —— 1/3 个有
- `FeatherMask` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `LoadDA3Model` —— 1/3 个有
- `MiniMaxH3FunControlNetApply` —— 1/3 个有
- `ModelPatchLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.2 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

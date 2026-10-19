---
name: unknown_workflow_video_sampler_clip_212
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.928
common_nodes: [ApplyFBCacheOnModel, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, JWImageResizeByLongerSide, KSamplerSelect, LTXVApplySTG, LTXVPreprocess, LTXVScheduler, LayerUtility: PurgeVRAM, LoadImage, Note Plus (mtb), PatchModelPatcherOrder, PathchSageAttentionKJ, RH_Captioner, RandomNoise, STGGuider, SamplerCustomAdvanced, String Replace (mtb), StringFunction|pysssss, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1897665923870838786.json, 视频生成/图生视频/1897684164685320194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_212

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1897665923870838786.json、视频生成/图生视频/1897684164685320194.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LTXVApplySTG`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Note Plus (mtb)`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `RH_Captioner`
- `RandomNoise`
- `STGGuider`
- `SamplerCustomAdvanced`
- `String Replace (mtb)`
- `StringFunction|pysssss`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyLTXVLatentVideo` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LTXVAddGuide` —— 1/2 个有
- `LTXVConditioning` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LTXVImgToVideo` —— 1/2 个有
- `Note _O` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

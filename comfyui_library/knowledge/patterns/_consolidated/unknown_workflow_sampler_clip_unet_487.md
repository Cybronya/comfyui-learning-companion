---
name: unknown_workflow_sampler_clip_unet_487
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.678
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein-视觉小说立绘生【生成全身+6种表情+去除背景】_2022937768967540738.json, 平台全量/klein+人物一键三视图V2+一致性增强版（6G显存可运行）_2073351426272747521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_487

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/klein-视觉小说立绘生【生成全身+6种表情+去除背景】_2022937768967540738.json、平台全量/klein+人物一键三视图V2+一致性增强版（6G显存可运行）_2073351426272747521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Get resolution [Crystools]` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageConcatFromBatch` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImageListToBatch+` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

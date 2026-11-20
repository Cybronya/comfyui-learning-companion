---
name: unknown_workflow_sampler_clip_unet_301
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.798
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2 klein一键无损放大+细节增强_2082363830050578433.json, 图片生成/图生图/flux_特征转换iden_transfer_v3_2051150744098754562.json, 图片生成/图生图/klein单图编辑_图像修复_2018568599132184578.json, 图片生成/文生图/图片生成和编辑_Flux-2-Klein_2012115517577891842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_301

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux2 klein一键无损放大+细节增强_2082363830050578433.json、图片生成/图生图/flux_特征转换iden_transfer_v3_2051150744098754562.json、图片生成/图生图/klein单图编辑_图像修复_2018568599132184578.json、图片生成/文生图/图片生成和编辑_Flux-2-Klein_2012115517577891842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `ColorMatch` —— 1/4 个有
- `IdentityFeatureTransferV3` —— 1/4 个有
- `ImageLoader` —— 1/4 个有
- `ImageSharpen` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `JWImageResizeByLongerSide` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `ResizeImagesByLongerEdge` —— 1/4 个有
- `TTP_text_mix` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

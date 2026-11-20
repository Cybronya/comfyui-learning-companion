---
name: unknown_workflow_clip_unet_vae_13
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91675
common_nodes: [CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, FluxGuidance, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext[Dev]—图片编辑_1938506351540920321.json, 图片生成/图生图/Kontext万物迁移-无需PS加强溶图_1952551302192672769.json, 图片生成/图生图/Kontext单图万物迁移_1950471483208421377.json, 图片生成/图生图/Kontext多图万物迁移_1950078595554263041.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext[Dev]—图片编辑_1938506351540920321.json、图片生成/图生图/Kontext万物迁移-无需PS加强溶图_1952551302192672769.json、图片生成/图生图/Kontext单图万物迁移_1950471483208421377.json、图片生成/图生图/Kontext多图万物迁移_1950078595554263041.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `FluxGuidance`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 3/4 个有
- `FastCanvas` —— 3/4 个有
- `FastCanvasTool` —— 3/4 个有
- `InpaintCrop` —— 3/4 个有
- `InpaintStitch` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `LayerUtility: CropByMask V3` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `SamplerCustomAdvanced` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `BasicGuider` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `ModelSamplingFlux` —— 2/4 个有
- `RBGImageStitchPlus` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `RepeatLatentBatch` —— 2/4 个有
- `easy imageScaleDownToSize` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `NAGCFGGuider` —— 1/4 个有
- `easy isMaskEmpty` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `workflow>采样器` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_clip_unet_130
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9016
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein 多图编辑工作流_2012031209374748673.json, 图片生成/文生图/Flux2-Klein文生图+图生图_2012291526050717697.json, 图片生成/文生图/Klein 9b 文生图&编辑  工作流_2013047540010192898.json, 图片生成/文生图/klein建筑，室内工作流+Klein放大工作流_2087711918889984002.json, 图片生成/文生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2060292542750613506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_130

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein 多图编辑工作流_2012031209374748673.json、图片生成/文生图/Flux2-Klein文生图+图生图_2012291526050717697.json、图片生成/文生图/Klein 9b 文生图&编辑  工作流_2013047540010192898.json、图片生成/文生图/klein建筑，室内工作流+Klein放大工作流_2087711918889984002.json、图片生成/文生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2060292542750613506.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `AddLabel` —— 2/5 个有
- `ColorMatch` —— 2/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `DrawMaskOnImage` —— 1/5 个有
- `INPAINT_ExpandMask` —— 1/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImageSharpen` —— 1/5 个有
- `InpaintModelConditioning` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `TextBox` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

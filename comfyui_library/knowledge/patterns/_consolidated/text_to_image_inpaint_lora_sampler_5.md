---
name: text_to_image_inpaint_lora_sampler_5
type: Text To Image
frequency: 2
level: weak
coverage: 0.9535
common_nodes: [AddMask, BlendInpaint, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntBinaryOperation, CM_NumberToInt, CachePreviewBridge, ColorMatch, ConditioningZeroOut, CutForInpaint, DifferentialDiffusion, DownloadAndLoadFlorence2Model, EmptyLatentImage, Florence2Run, FluxGuidance, Get Image Size, GrowMaskWithBlur, ImageAndMaskPreview, ImageConcanate, ImageCrop+, ImageMaskSwitch, ImageScale, ImageToMask, ImpactInt, InpaintModelConditioning, Int Literal, IsMaskEmpty, JjkText, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, RHHiddenNodes, RepeatLatentBatch, SaveImage, StyleModelApply, StyleModelLoader, SubtractMask, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageSize, easy mathInt, solarL_SaveImagesToZip, workflow>123, workflow>zz, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Face Swap智能换脸｜支持眼镜妆容图生图生成_2095959250995601409.json, 图片生成/图生图/Face_Swap换脸新玩法｜眼镜妆容都能保住，换脸不毁妆细节_2099422220891287553.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Face Swap智能换脸｜支持眼镜妆容图生图生成_2095959250995601409.json、图片生成/图生图/Face_Swap换脸新玩法｜眼镜妆容都能保住，换脸不毁妆细节_2099422220891287553.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `BlendInpaint`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntBinaryOperation`
- `CM_NumberToInt`
- `CachePreviewBridge`
- `ColorMatch`
- `ConditioningZeroOut`
- `CutForInpaint`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `EmptyLatentImage`
- `Florence2Run`
- `FluxGuidance`
- `Get Image Size`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageCrop+`
- `ImageMaskSwitch`
- `ImageScale`
- `ImageToMask`
- `ImpactInt`
- `InpaintModelConditioning`
- `Int Literal`
- `IsMaskEmpty`
- `JjkText`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `RHHiddenNodes`
- `RepeatLatentBatch`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy mathInt`
- `solarL_SaveImagesToZip`
- `workflow>123`
- `workflow>zz`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

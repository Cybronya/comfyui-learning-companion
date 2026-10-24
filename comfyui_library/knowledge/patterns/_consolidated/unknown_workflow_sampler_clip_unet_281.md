---
name: unknown_workflow_sampler_clip_unet_281
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92625
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 抠图 白底 透明材质_2076477973649256450.json, 图片生成/图生图/flux Klein 图像编辑版 fluxklein克莱因图像编辑，图生图_2016676554306232322.json, 图片生成/文生图/FLUX2 Klein 9B Consistency 一致性工作流_2073316611037163521.json, 图片生成/文生图/FLUX2 Klein 9B Image Edit_2073301759640035330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_281

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Klein 抠图 白底 透明材质_2076477973649256450.json、图片生成/图生图/flux Klein 图像编辑版 fluxklein克莱因图像编辑，图生图_2016676554306232322.json、图片生成/文生图/FLUX2 Klein 9B Consistency 一致性工作流_2073316611037163521.json、图片生成/文生图/FLUX2 Klein 9B Image Edit_2073301759640035330.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
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
- `Image Comparer (rgthree)` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `JoinImageWithAlpha` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/4 个有
- `LayerUtility: ImageCombineAlpha` —— 1/4 个有
- `Mask Invert` —— 1/4 个有
- `SDMatteApply` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_clip_unet_92
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.948091
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 三图编辑 多元素提取融合特征保持_2014171959289978882.json, 图片生成/图生图/Flux2 Klein-三图编辑-9B版本_2012148907626733570.json, 图片生成/图生图/Flux2 Klein图像编辑-9B版官方版（单图编辑）_2012123953627668482.json, 图片生成/图生图/Flux2 Klein批量去除水印9B版_2012709119131652097.json, 图片生成/图生图/Flux2-Klein-动作迁移_2012197021490356226.json, 图片生成/图生图/Flux2Klein图像编辑9B版官方版（加速版）_2012060623399559170.json, 图片生成/图生图/Flux2_Klein 图像编辑9B版-官方版_2012026824955531265.json, 图片生成/图生图/单图编辑版+10秒出图（FLUX2+Klein）_2012861610414575618.json, 图片生成/图生图/最新Flux2-Klein 9B-换脸换头_2013812519105728513.json, 图片生成/图生图/😶_🌫️FLUX新王炸 Klein 图像编辑版 急速10秒出图😶_🌫️_2012100971706458113.json, 图片生成/图生图/😶‍🌫️FLUX新王炸 Klein 双图编辑版😶‍🌫️_2012282965887291393.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_92

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 三图编辑 多元素提取融合特征保持_2014171959289978882.json、图片生成/图生图/Flux2 Klein-三图编辑-9B版本_2012148907626733570.json、图片生成/图生图/Flux2 Klein图像编辑-9B版官方版（单图编辑）_2012123953627668482.json、图片生成/图生图/Flux2 Klein批量去除水印9B版_2012709119131652097.json、图片生成/图生图/Flux2-Klein-动作迁移_2012197021490356226.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `GetImageSize` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `CFGGuider` —— 9/11 个有
- `ConditioningZeroOut` —— 9/11 个有
- `Flux2Scheduler` —— 9/11 个有
- `ImageScaleToTotalPixels` —— 9/11 个有
- `CR Text` —— 8/11 个有
- `EmptyFlux2LatentImage` —— 7/11 个有
- `PreviewImage` —— 7/11 个有
- `LayerUtility: ImageReel` —— 4/11 个有
- `LayerUtility: ImageReelComposit` —— 4/11 个有
- `BasicGuider` —— 2/11 个有
- `BasicScheduler` —— 2/11 个有
- `EmptyLatentImage` —— 2/11 个有
- `FluxKontextImageScale` —— 2/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `ColorMatch` —— 1/11 个有
- `HAIGC_LoadImagesFromZip` —— 1/11 个有
- `HAIGC_SaveImagesToZip` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `ImageFromBatch+` —— 1/11 个有
- `ImageListToBatch+` —— 1/11 个有
- `OpenposePreprocessor` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 648 | - | 2 | 100% |
| 高度 | 888 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 648，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 888，样本不足，未给区间，2 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_sampler_clip_unet_16
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.962321
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 三图编辑 多元素提取融合特征保持_2014171959289978882.json, 图片生成/图生图/Flux2 Klein-三图编辑-9B版本_2012148907626733570.json, 图片生成/图生图/Flux2 dev 多图编辑工作流 - 一致性_1994746929441542145.json, 图片生成/图生图/Flux2 dev 多图编辑能力_1994452506996510722.json, 图片生成/图生图/Flux2-Klein+产品精修_2017042202211389442.json, 图片生成/图生图/Flux2-Klein+模特换姿势_2012147180743692290.json, 图片生成/图生图/Flux2-Klein+模特换装_2012142481311277058.json, 图片生成/图生图/Flux2-klein-4B单图编辑基础工作流_2012509428817338370.json, 图片生成/图生图/Flux2-klein-4B双图编辑基础工作流_2012520965321789441.json, 图片生成/图生图/Flux2-klein-9B单图编辑基础工作流_2012518759935778817.json, 图片生成/图生图/Flux2-klein-9B双图编辑基础工作流_2012525390807441410.json, 图片生成/图生图/Flux2-klein三图编辑_2014894419652120577.json, 图片生成/图生图/Flux2-klein双图编辑_2014262671088029698.json, 图片生成/图生图/Flux2-klein双图编辑_2071856786591801345.json, 图片生成/图生图/Flux2-klein双图编辑_2094963496629923841.json, 图片生成/图生图/Flux2-klein双图编辑_2099463529001738242.json, 图片生成/图生图/Flux2.Klein_KV 4steps_2046833812876824578.json, 图片生成/图生图/Flux2DEV发布啦！保持面部一致性试用_1993517880908120065.json, 图片生成/图生图/Flux2DEV多图编辑_2019571127059746818.json, 图片生成/图生图/Flux2DEV多图编辑_2048716611548356610.json, 图片生成/图生图/Flux2Klein 单图编辑_2012572910803755010.json, 图片生成/图生图/Flux2Klein 去水印马赛克_2013545657268703234.json, 图片生成/图生图/Flux2Klein 高清化_2013543196827066370.json, 图片生成/图生图/Q版色稿转成品_2092805656247099393.json, 图片生成/图生图/flux-2-klein-4b单图编辑_2033454491990761473.json, 图片生成/图生图/flux-2-klein-9b模型图像编辑_2094963430150201346.json, 图片生成/图生图/kelin精修V2_2061361375989035010.json, 图片生成/文生图/Flux2_Klein 多图编辑精简版_2012069622740164610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 三图编辑 多元素提取融合特征保持_2014171959289978882.json、图片生成/图生图/Flux2 Klein-三图编辑-9B版本_2012148907626733570.json、图片生成/图生图/Flux2 dev 多图编辑工作流 - 一致性_1994746929441542145.json、图片生成/图生图/Flux2 dev 多图编辑能力_1994452506996510722.json、图片生成/图生图/Flux2-Klein+产品精修_2017042202211389442.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 26/28 个有
- `Flux2Scheduler` —— 26/28 个有
- `GetImageSize` —— 22/28 个有
- `CFGGuider` —— 21/28 个有
- `BasicGuider` —— 8/28 个有
- `CR Text` —— 8/28 个有
- `ImageConcanate` —— 7/28 个有
- `String Literal` —— 7/28 个有
- `FluxGuidance` —— 5/28 个有
- `PreviewImage` —— 5/28 个有
- `BasicScheduler` —— 3/28 个有
- `EmptyLatentImage` —— 3/28 个有
- `Image Comparer (rgthree)` —— 3/28 个有
- `LoraLoaderModelOnly` —— 3/28 个有
- `easy promptList` —— 3/28 个有
- `ConditioningZeroOut` —— 2/28 个有
- `Anything Everywhere3` —— 1/28 个有
- `Fast Groups Muter (rgthree)` —— 1/28 个有
- `ImageColorMatch+` —— 1/28 个有
- `ImageScale` —— 1/28 个有
- `OpenposePreprocessor` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 648 | 640 - 648 | 3 | 99% |
| 高度 | 888 | 512 - 888 | 3 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 648，观测区间 640 - 648，3 个样本，取值集中（一致性 99%）
- 高度 中位数 888，观测区间 512 - 888，3 个样本

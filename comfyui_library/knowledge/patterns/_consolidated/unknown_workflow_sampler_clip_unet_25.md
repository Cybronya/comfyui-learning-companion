---
name: unknown_workflow_sampler_clip_unet_25
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.904458
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 单图编辑【用于绘世comfyui批量管理系统】_2089195480411623426.json, 图片生成/图生图/Klein-i2i_2089727593099649025.json, 图片生成/图生图/Klein-is2i_2068689580571844609.json, 图片生成/图生图/Klein-一致性编辑_2086324766218215426.json, 图片生成/图生图/Klein9B一键生成姿态变换 改变姿势_2071187621459619841.json, 图片生成/图生图/Klein9B一键生成姿态变换 改变姿势图生图_2071957948699602945.json, 图片生成/图生图/Klein9B图片编辑_深度+线稿+法线+硬边缘控制_2070761465564459010.json, 图片生成/图生图/Klein9B姿态变换_2070588045203693570.json, 图片生成/图生图/Klein9B姿态变换_2070762335559577601.json, 图片生成/图生图/Klein9B姿态变换_2070886463251771394.json, 图片生成/图生图/Klein9B深度+线稿+法线+硬边缘控制图片编辑_2070582560786313218.json, 图片生成/图生图/Klein9B深度+线稿+法线+硬边缘控制图片编辑图生图工作流_2083137344915460098.json, 图片生成/图生图/Klein9B深度+线稿+法线+硬边缘控制图片编辑工作流_2071184794939125761.json, 图片生成/图生图/Klein9B深度+线稿+法线+硬边缘控制图片编辑工作流_2071950437573545986.json, 图片生成/图生图/Klein用方框进行图像增改删_2042840062538289154.json, 图片生成/图生图/klein 单图参考_2048402694292901891.json, 图片生成/图生图/klein 双图编辑_2048417433756639234.json, 图片生成/图生图/klein 扩图_2018209439236493313.json, 图片生成/图生图/klein 扩图_局部重绘_2012965333056888833.json, 图片生成/图生图/klein 扩图_局部重绘_2016153153808371714.json, 图片生成/图生图/klein单图编辑_2014331376341880834.json, 图片生成/图生图/klein单图编辑_2026469050368397313.json, 图片生成/图生图/klein单图编辑——修改版_2033387043891449857.json, 图片生成/图生图/klein扩图工作流_2013942199481798658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/Klein 单图编辑【用于绘世comfyui批量管理系统】_2089195480411623426.json、图片生成/图生图/Klein-i2i_2089727593099649025.json、图片生成/图生图/Klein-is2i_2068689580571844609.json、图片生成/图生图/Klein-一致性编辑_2086324766218215426.json、图片生成/图生图/Klein9B一键生成姿态变换 改变姿势_2071187621459619841.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 24 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
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
- `ImageScaleToTotalPixels` —— 23/24 个有
- `EmptyFlux2LatentImage` —— 21/24 个有
- `GetImageSize` —— 20/24 个有
- `PreviewImage` —— 18/24 个有
- `ConditioningZeroOut` —— 16/24 个有
- `LoraLoaderModelOnly` —— 12/24 个有
- `AIO_Preprocessor` —— 10/24 个有
- `ImageConcatMulti` —— 10/24 个有
- `easy seed` —— 8/24 个有
- `ImagePadForOutpaint` —— 7/24 个有
- `ImageConcanate` —— 6/24 个有
- `ColorMatch` —— 4/24 个有
- `Image Comparer (rgthree)` —— 4/24 个有
- `DrawMaskOnImage` —— 3/24 个有
- `EmptyLatentImage` —— 3/24 个有
- `INTConstant` —— 3/24 个有
- `PrimitiveStringMultiline` —— 2/24 个有
- `CR Text` —— 1/24 个有
- `ConstrainImage|pysssss` —— 1/24 个有
- `EasySizeSimpleImage` —— 1/24 个有
- `ImageUpscaleWithModel` —— 1/24 个有
- `UpscaleModelLoader` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）

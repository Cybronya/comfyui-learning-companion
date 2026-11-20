---
name: image_to_image_sampler_clip_unet_4
type: Image To Image
frequency: 34
level: strong
coverage: 0.911853
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext [dev]极简基础工作流_1938804683022782466.json, 图片生成/图生图/Kontext dev  -remove watermark_1942780220313112578.json, 图片生成/图生图/Kontext dev  neon style_1942229764629278721.json, 图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json, 图片生成/图生图/Kontext dev 像素风格_1942206684389642242.json, 图片生成/图生图/Kontext-DEV一键三视图_1939869541839052801.json, 图片生成/图生图/Kontext-DEV一键三视图_1951214560822931457.json, 图片生成/图生图/Kontext-DEV人物、产品换背景 产品一致性工作流   效果很不错_1967778723778932737.json, 图片生成/图生图/Kontext-Emoj风格转换_1951268420702646274.json, 图片生成/图生图/Kontext-最强老照片修复_1972212168999497729.json, 图片生成/图生图/Kontext-老破照片修复_1972137847203557378.json, 图片生成/图生图/Kontext一键人像高清美颜（添加lora）_1944545954299039745.json, 图片生成/图生图/chibi转真实动漫_Kontext-LORA_1940818567921299457.json, 图片生成/图生图/minimalist极简主义风格_Kontext-dev_1943852515488071682.json, 图片生成/图生图/mosaic马赛克艺术风格_Kontext-dev_1943857459070926850.json, 图片生成/图生图/一张图片生成 3D Chibi可爱风格_2027185278074494977.json, 图片生成/图生图/一键三视图_Kontext-DEV图像编辑_1939142169158410241.json, 图片生成/图生图/一键人像精修_Kontext-dev_1944091800334139394.json, 图片生成/图生图/万物国画风格转绘_Kontext-dev_1943327017553043458.json, 图片生成/图生图/人物转身首尾帧_Kontext-LORA_1940624522338873345.json, 图片生成/图生图/去除马赛克LORA_Kontext-dev_1943348611730337794.json, 图片生成/图生图/取衣去人_Kontext-DEV-LORA_1940461645275754497.json, 图片生成/图生图/图像局部修改_服装_家具_人物Kontext-DEV开源官方版_1938894823174950914.json, 图片生成/图生图/图像局部修改_服装编辑_Kontext-DEV开源ComfyUI官方版_1938389852155215873.json, 图片生成/图生图/手绘风格3视图_Kontext-DEV-LORA_1940464345698693121.json, 图片生成/图生图/拍立得照片_Kontext-dev TeaCache加速方案_1944531646655942658.json, 图片生成/图生图/智能水印擦除_Kontext-DEV图像编辑_1938936115401252866.json, 图片生成/图生图/木刻版画转绘_Kontext-LORA_1941099293753372673.json, 图片生成/图生图/毛坯房精装方案设计图_Kontext-DEV图像编辑_1938944918020612098.json, 图片生成/图生图/电商服装加模特_Kontext-DEV开源ComfyUI官方版_1938390435477786625.json, 图片生成/图生图/电影颗粒质感风格_Kontext-dev_1943855045148545025.json, 图片生成/图生图/线稿提取_Kontext-DEV图像编辑_1938971620017164289.json, 图片生成/图生图/赛博波普风格_Kontext-dev_1944528687922335745.json, 图片生成/图生图/马克笔风格风格转绘_1943325807521505281.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（图片生成/图生图/Kontext [dev]极简基础工作流_1938804683022782466.json、图片生成/图生图/Kontext dev  -remove watermark_1942780220313112578.json、图片生成/图生图/Kontext dev  neon style_1942229764629278721.json、图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json、图片生成/图生图/Kontext dev 像素风格_1942206684389642242.json…）

- **类型**：Image To Image
- **样本数**：34
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 34 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 33/34 个有
- `Text Multiline` —— 33/34 个有
- `ImageConcatMulti` —— 32/34 个有
- `ImageStitch` —— 29/34 个有
- `ShowText|pysssss` —— 28/34 个有
- `LoraLoaderModelOnly` —— 26/34 个有
- `PreviewImage` —— 24/34 个有
- `EmptySD3LatentImage` —— 14/34 个有
- `GetImageSizeAndCount` —— 14/34 个有
- `GoogleTranslateTextNode` —— 11/34 个有
- `ImageScaleDownToSize` —— 7/34 个有
- `LoaderGGUF` —— 6/34 个有
- `RH_Translator` —— 6/34 个有
- `ImageResize` —— 4/34 个有
- `TeaCache` —— 2/34 个有
- `Image Comparer (rgthree)` —— 1/34 个有
- `JjkText` —— 1/34 个有
- `PreviewTextNode` —— 1/34 个有
- `easy showAnything` —— 1/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 30 | 34 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 34 | 100% |
| 采样算法 | euler | - | 34 | 100% |
| 调度器 | simple | - | 34 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 34 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 30，34 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，34 个样本，一致性 100%
- 调度器 最常用 simple，34 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）

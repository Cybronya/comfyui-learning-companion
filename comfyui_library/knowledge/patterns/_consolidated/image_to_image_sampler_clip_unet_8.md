---
name: image_to_image_sampler_clip_unet_8
type: Image To Image
frequency: 21
level: strong
coverage: 0.897762
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-三视图_1938913966724669442.json, 图片生成/图生图/Kontext-动漫人物转绘_1940651426446209025.json, 图片生成/图生图/Kontext-最强老照片修复_1972212168999497729.json, 图片生成/图生图/Kontext-老破照片修复_1972137847203557378.json, 图片生成/图生图/Kontext【一键3D转2D】欧卡风_1979193772133224449.json, 图片生成/图生图/Kontext一键人像高清美颜（添加lora）_1944545954299039745.json, 图片生成/图生图/Kontext人台模特衣服展示_1938854583487619073.json, 图片生成/图生图/Kontext老照片修复_2005923453268099074.json, 图片生成/图生图/PS1游戏风格_Kontext-DEV-LORA_1945035820526133249.json, 图片生成/图生图/Sketch手绘风格_Kontext-DEV-LORA_1948604464042246145.json, 图片生成/图生图/chibi转真实动漫_Kontext-LORA_1940818567921299457.json, 图片生成/图生图/minimalist极简主义风格_Kontext-dev_1943852515488071682.json, 图片生成/图生图/mosaic马赛克艺术风格_Kontext-dev_1943857459070926850.json, 图片生成/图生图/拍立得手持风格_Kontext-DEV-LORA_1947997286562430978.json, 图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1970697389088645122.json, 图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1986368699110223874.json, 图片生成/图生图/赛博波普风格_Kontext-dev_1944528687922335745.json, 图片生成/图生图/镜头缩放主体可见_Kontext-DEV-LORA_1948295169715109889.json, 图片生成/图生图/青铜雕塑_Kontext-DEV-LORA_1946225600609546241.json, 图片生成/图生图/高清扩图_Kontext-DEV-LORA_1944993249007427586.json, 图片生成/图生图/高清扩图_Kontext-DEV-LORA_1945760609537290241.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/Kontext-三视图_1938913966724669442.json、图片生成/图生图/Kontext-动漫人物转绘_1940651426446209025.json、图片生成/图生图/Kontext-最强老照片修复_1972212168999497729.json、图片生成/图生图/Kontext-老破照片修复_1972137847203557378.json、图片生成/图生图/Kontext【一键3D转2D】欧卡风_1979193772133224449.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 20/21 个有
- `ShowText|pysssss` —— 20/21 个有
- `LoraLoaderModelOnly` —— 19/21 个有
- `ImageStitch` —— 18/21 个有
- `Text Multiline` —— 18/21 个有
- `PreviewImage` —— 14/21 个有
- `ImageConcatMulti` —— 13/21 个有
- `TeaCache` —— 10/21 个有
- `Image Padding` —— 8/21 个有
- `EmptySD3LatentImage` —— 6/21 个有
- `CR Simple Image Compare` —— 5/21 个有
- `GetImageSizeAndCount` —— 5/21 个有
- `ImageScaleDownToSize` —— 4/21 个有
- `RH_Translator` —— 4/21 个有
- `ImagePadKJ` —— 3/21 个有
- `Image Comparer (rgthree)` —— 2/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/21 个有
- `ImageConcanate` —— 1/21 个有
- `LayerUtility: PurgeVRAM` —— 1/21 个有
- `PMRF` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 25 | 21 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 21 | 70% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 25，21 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，21 个样本
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）

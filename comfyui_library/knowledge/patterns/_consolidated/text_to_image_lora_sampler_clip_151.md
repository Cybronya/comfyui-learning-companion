---
name: text_to_image_lora_sampler_clip_151
type: Text To Image
frequency: 10
level: strong
coverage: 0.8353
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json, 图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json, 图片生成/图生图/AI换装双图试穿工作流｜Qwen-Image_2.1智能提示词｜服装上身效果图秒出_2112076955049873410.json, 图片生成/图生图/FLUX 3 Image Klein图像编辑，图片换背景图生图_2111961472422203393.json, 图片生成/图生图/FLUX 3 Image Klein图像编辑｜换背景抠图一站式处理_2111754100328189953.json, 图片生成/图生图/Flux3-klein常规图像编辑PUP增强版｜图生图精修更稳_2111740631423995905.json, 图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json, 图片生成/图生图/Qwen image 2.1多合一图像编辑加速工作流V1.5 高效改图方案_2105409388168171522.json, 图片生成/图生图/Qwen+image+2.1图片编辑｜图生图局部修改轻松改细节_2104555432860807170.json, 图片生成/图生图/多合一图像编辑提速 Qwen image 2.1局部重绘抠图一站搞定_2104295137974251521.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json、图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json、图片生成/图生图/AI换装双图试穿工作流｜Qwen-Image_2.1智能提示词｜服装上身效果图秒出_2112076955049873410.json、图片生成/图生图/FLUX 3 Image Klein图像编辑，图片换背景图生图_2111961472422203393.json、图片生成/图生图/FLUX 3 Image Klein图像编辑｜换背景抠图一站式处理_2111754100328189953.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `PreviewAny` —— 9/10 个有
- `QwenImage21Cache` —— 7/10 个有
- `ResolutionSelector` —— 7/10 个有
- `TextEncodeQwenImage21` —— 7/10 个有
- `BatchImagesNode` —— 6/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `PrimitiveBoolean` —— 6/10 个有
- `SaveImageAdvanced` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `ImageScaleToTotalPixels` —— 4/10 个有
- `EmptyFlux2LatentImage` —— 3/10 个有
- `PrimitiveInt` —— 3/10 个有
- `ReferenceMultiLatent` —— 3/10 个有
- `StringConcatenate` —— 3/10 个有
- `Any Switch (rgthree)` —— 2/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `Fast Bypasser (rgthree)` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 2/10 个有
- `ImageConcanate` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `RegexExtract` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `EasyCache` —— 1/10 个有
- `SeedNode` —— 1/10 个有
- `Textbox` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_260
type: Text To Image
frequency: 7
level: strong
coverage: 0.882
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1精准扩图｜按25%或300像素延展画布，一键扩展16_9_2104507613303107585.json, 图片生成/图生图/Qwen Image 2.1角色四视图及三视图生成，图生图角色设计方案_2103618237505294338.json, 图片生成/图生图/Qwen image 2.1二合一工作流｜万物移除与局部重绘，擦除修复全能_2104547539398778881.json, 图片生成/图生图/Qwen image 2.1模特一键换装，服装迁移商品替换_2112341971791597570.json, 图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json, 图片生成/图生图/Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090.json, 图片生成/图生图/万物移除加局部重绘二合一 Qwen image 2.1图像编辑工作流_2104778416783446018.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_260

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1精准扩图｜按25%或300像素延展画布，一键扩展16_9_2104507613303107585.json、图片生成/图生图/Qwen Image 2.1角色四视图及三视图生成，图生图角色设计方案_2103618237505294338.json、图片生成/图生图/Qwen image 2.1二合一工作流｜万物移除与局部重绘，擦除修复全能_2104547539398778881.json、图片生成/图生图/Qwen image 2.1模特一键换装，服装迁移商品替换_2112341971791597570.json、图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `PreviewImage` —— 5/7 个有
- `Mask Fill Holes` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `DrawMaskOnImage` —— 3/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `ImpactSwitch` —— 3/7 个有
- `Int` —— 3/7 个有
- `InpaintModelConditioning` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `LayerUtility: CropByMask V2` —— 1/7 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/7 个有
- `LayerUtility: RestoreCropBox` —— 1/7 个有
- `easy imageSizeByLongerSide` —— 1/7 个有
- `easy int` —— 1/7 个有
- `孤海外补画板按方向` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足

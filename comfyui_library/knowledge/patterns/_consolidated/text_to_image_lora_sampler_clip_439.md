---
name: text_to_image_lora_sampler_clip_439
type: Text To Image
frequency: 4
level: strong
coverage: 0.87775
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1无痕扩图 指定大小零偏移零色差工具_2113723580210044929.json, 图片生成/图生图/Qwen image 2.1模特一键换装，服装迁移商品替换_2112341971791597570.json, 图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json, 图片生成/图生图/Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_439

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1无痕扩图 指定大小零偏移零色差工具_2113723580210044929.json、图片生成/图生图/Qwen image 2.1模特一键换装，服装迁移商品替换_2112341971791597570.json、图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json、图片生成/图生图/Qwen image2.1万能局部重绘低像素重绘 精准控制改图_2109734236285657090.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `InpaintModelConditioning` —— 2/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `DapaoImagePadDirectionNode` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: CropByMask V2` —— 1/4 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/4 个有
- `LayerUtility: RestoreCropBox` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Switch any [Crystools]` —— 1/4 个有
- `长边短边` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

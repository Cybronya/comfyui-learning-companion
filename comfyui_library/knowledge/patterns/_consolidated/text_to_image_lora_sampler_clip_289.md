---
name: text_to_image_lora_sampler_clip_289
type: Text To Image
frequency: 7
level: strong
coverage: 0.88
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2113806381106163713.json, 图片生成/图生图/全能图片G2.0低价渠道版图生图工作流，通用图片生成与编辑_2106559678716137474.json, 图片生成/图生图/全能图片G2.5全能图片V2文生图图生图处理生成工具_2102151973511454722.json, 图片生成/图生图/平铺图白底精修处理｜抠图去水印图生图商品优化_2097056787252989954.json, 图片生成/图生图/黑鹤出品｜SeedVR2高清放大工作流｜图生图画质提升必备工具_2101846943638056961.json, 图片生成/文生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2110455043114758145.json, 图片生成/文生图/全能图片全能图片G2.5文生图与图生图 角色一致性高质量创作_2098123716503891970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_289

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2113806381106163713.json、图片生成/图生图/全能图片G2.0低价渠道版图生图工作流，通用图片生成与编辑_2106559678716137474.json、图片生成/图生图/全能图片G2.5全能图片V2文生图图生图处理生成工具_2102151973511454722.json、图片生成/图生图/平铺图白底精修处理｜抠图去水印图生图商品优化_2097056787252989954.json、图片生成/图生图/黑鹤出品｜SeedVR2高清放大工作流｜图生图画质提升必备工具_2101846943638056961.json…）

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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/7 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 5/7 个有
- `RH_RhartImageG2ImageToImage` —— 5/7 个有
- `孤海注释` —— 5/7 个有
- `RH_RhartImageG25SunburstImageToImage` —— 4/7 个有
- `SeedVR2` —— 4/7 个有
- `SeedVR2BlockSwap` —— 4/7 个有
- `easy int` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `RH_RhartImageNNb21ImageToImage` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `SaveImageAndMetadata_` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

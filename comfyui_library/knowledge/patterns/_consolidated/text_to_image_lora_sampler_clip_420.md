---
name: text_to_image_lora_sampler_clip_420
type: Text To Image
frequency: 4
level: strong
coverage: 0.88875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换装商品替换｜Seedream-v5-pro图生图直出_2090560787105533953.json, 图片生成/图生图/一键换装完美保纹理｜Seedream-v5-pro商品替换图生图_2090864701696724993.json, 图片生成/图生图/九宫格切割工作流｜图像批量分割拼接处理图生图_2096745684694290434.json, 图片生成/图生图/全能图像Image2.5三图编辑 多图合成处理_2098301067544055810.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_420

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换装商品替换｜Seedream-v5-pro图生图直出_2090560787105533953.json、图片生成/图生图/一键换装完美保纹理｜Seedream-v5-pro商品替换图生图_2090864701696724993.json、图片生成/图生图/九宫格切割工作流｜图像批量分割拼接处理图生图_2096745684694290434.json、图片生成/图生图/全能图像Image2.5三图编辑 多图合成处理_2098301067544055810.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `RH_SeedreamV5ProImageToImage` —— 2/4 个有
- `图像缩放V2_孤海` —— 2/4 个有
- `1hew_ImageGridSplit` —— 1/4 个有
- `ImageGridSplitter` —— 1/4 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/4 个有

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

---
name: text_to_image_lora_sampler_clip_312
type: Text To Image
frequency: 6
level: strong
coverage: 0.875667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SFT图像编辑｜SenseNova 1.5局部重绘换背景_2093781245145731073.json, 图片生成/图生图/全能图片G image 2.5图生图，最强生图模型实测_2110838624374845441.json, 图片生成/图生图/全能图片G image 2.5图生图｜最强生图模型一站直出_2111080841748242433.json, 图片生成/图生图/全能图片G image 2.5图生图｜最强生图模型质感天花板_2110688249055367169.json, 图片生成/图生图/全能图片G2.5视觉重构图生图 风格迁移多维局部重绘_2099223557640380417.json, 图片生成/图生图/全能图片G2.5视觉重构图生图 风格迁移多维局部重绘_2099592794041049089.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_312

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/SFT图像编辑｜SenseNova 1.5局部重绘换背景_2093781245145731073.json、图片生成/图生图/全能图片G image 2.5图生图，最强生图模型实测_2110838624374845441.json、图片生成/图生图/全能图片G image 2.5图生图｜最强生图模型一站直出_2111080841748242433.json、图片生成/图生图/全能图片G image 2.5图生图｜最强生图模型质感天花板_2110688249055367169.json、图片生成/图生图/全能图片G2.5视觉重构图生图 风格迁移多维局部重绘_2099223557640380417.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `RH_RhartImageG25FlareImageToImage` —— 5/6 个有
- `EmptySenseNovaLatentImage` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `SenseNovaReferenceImage` —— 1/6 个有
- `SenseNovaSamplingOptions` —— 1/6 个有
- `SenseNovaU15Loader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

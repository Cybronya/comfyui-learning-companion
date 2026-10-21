---
name: text_to_image_lora_sampler_clip_207
type: Text To Image
frequency: 6
level: strong
coverage: 0.881167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/全能图片G2.5双模型自由切换 文生图4K画质输出_2098708483548995586.json, 图片生成/文生图/全能图片G2.5双模型自由切换文生图4K画质_2100270591503847426.json, 图片生成/文生图/全能图片G2.5图生图图像编辑 文生图极速高品质处理_2098650019942461442.json, 图片生成/文生图/全能图片G2.5图生图高品质版处理工具_2100659592215744513.json, 图片生成/文生图/全能图片G2.5文生图经济版 低成本多风格高清出图_2099224723895971841.json, 图片生成/文生图/全能图片G2.5文生图经济版 低成本多风格高清出图_2099591235303464962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_207

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/全能图片G2.5双模型自由切换 文生图4K画质输出_2098708483548995586.json、图片生成/文生图/全能图片G2.5双模型自由切换文生图4K画质_2100270591503847426.json、图片生成/文生图/全能图片G2.5图生图图像编辑 文生图极速高品质处理_2098650019942461442.json、图片生成/文生图/全能图片G2.5图生图高品质版处理工具_2100659592215744513.json、图片生成/文生图/全能图片G2.5文生图经济版 低成本多风格高清出图_2099224723895971841.json…）

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
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG25SunburstTextToImage` —— 5/6 个有
- `LoadImage` —— 3/6 个有
- `ExecutionBlocker` —— 2/6 个有
- `ImpactNeg` —— 2/6 个有
- `MuyeTextEditOutput` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `RH_RhartImageG25FlareImageToImage` —— 2/6 个有
- `RH_RhartImageG25FlareTextToImage` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 1/6 个有

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

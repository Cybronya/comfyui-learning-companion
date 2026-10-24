---
name: text_to_image_lora_sampler_clip_233
type: Text To Image
frequency: 8
level: strong
coverage: 0.862
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能图片G2.5全能图片V2文生图图生图处理生成工具_2102151973511454722.json, 图片生成/图生图/全能图片G2.5换装 虚拟试衣图生图处理工具_2099929509331034114.json, 图片生成/图生图/全能图片G2.5换装+虚拟试衣图生图处理工具_2101571060582928385.json, 图片生成/图生图/全能图片G2图生图0.1元版处理生成工具_2102487881666351105.json, 图片生成/图生图/地表最强全能图片G2图生图｜GP-T-Image-2单次0.1元｜改图超划算_2102222773492994049.json, 图片生成/图生图/平铺图白底精修处理｜抠图去水印图生图商品优化_2097056787252989954.json, 图片生成/图生图/黑鹤出品｜SeedVR2高清放大工作流｜图生图画质提升必备工具_2101846943638056961.json, 图片生成/文生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2110455043114758145.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_233

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/全能图片G2.5全能图片V2文生图图生图处理生成工具_2102151973511454722.json、图片生成/图生图/全能图片G2.5换装 虚拟试衣图生图处理工具_2099929509331034114.json、图片生成/图生图/全能图片G2.5换装+虚拟试衣图生图处理工具_2101571060582928385.json、图片生成/图生图/全能图片G2图生图0.1元版处理生成工具_2102487881666351105.json、图片生成/图生图/地表最强全能图片G2图生图｜GP-T-Image-2单次0.1元｜改图超划算_2102222773492994049.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 6/8 个有
- `RH_RhartImageG25SunburstImageToImage` —— 4/8 个有
- `RH_RhartImageG2ImageToImage` —— 4/8 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 3/8 个有
- `SeedVR2` —— 3/8 个有
- `SeedVR2BlockSwap` —— 3/8 个有
- `Float` —— 2/8 个有
- `RTXVideoSuperResolution` —— 2/8 个有
- `easy int` —— 2/8 个有
- `RH_RhartImageNNb21ImageToImage` —— 1/8 个有
- `SaveImageAndMetadata_` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

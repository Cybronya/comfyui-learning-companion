---
name: text_to_image_lora_sampler_clip_493
type: Text To Image
frequency: 3
level: strong
coverage: 0.871
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, ShowText|pysssss, Text, UNETLoader, VAEDecode, VAELoader, easy promptConcat, easy promptLine, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能图片V1_Pro电商详情页｜一键生成整套详情，上架图不用求设计_2099474049553494017.json, 图片生成/图生图/最新G_image2官方全量稳定版V1.0｜跨境电商主图详情页图生图一键出_2100503932853379073.json, 图片生成/图生图/电商主图详情图12图全能图片2.0自动分割经济版，图生图低成本方案_2103965668390559746.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_493

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全能图片V1_Pro电商详情页｜一键生成整套详情，上架图不用求设计_2099474049553494017.json、图片生成/图生图/最新G_image2官方全量稳定版V1.0｜跨境电商主图详情页图生图一键出_2100503932853379073.json、图片生成/图生图/电商主图详情图12图全能图片2.0自动分割经济版，图生图低成本方案_2103965668390559746.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `ShowText|pysssss`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`
- `easy promptLine`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `HAIGC_CombineUnits` —— 2/3 个有
- `HAIGC_Layer` —— 2/3 个有
- `HAIGC_SavePSD` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_RhartImageNG31FlashOfficialImageToImage` —— 2/3 个有
- `GuHaiAutoImageSplit` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

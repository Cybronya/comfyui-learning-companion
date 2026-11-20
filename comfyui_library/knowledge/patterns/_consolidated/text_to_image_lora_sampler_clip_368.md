---
name: text_to_image_lora_sampler_clip_368
type: Text To Image
frequency: 5
level: strong
coverage: 0.7982
common_nodes: [CLIPLoader, CLIPTextEncode, ConstrainImage|pysssss, EmptyLatentImage, Get Image Size, Image Comparer (rgthree), ImageFromBatch, ImageResize+, ImageScaleBy, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy joinImageBatch, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2K高清分镜切割机｜图生图一键拆分镜帧出图_2092142854641635329.json, 图片生成/图生图/分镜切割机-2k_2087408324949139457.json, 图片生成/图生图/新春贺岁变身相机｜表情包人像写真妆容图生图_2092161264884731906.json, 图片生成/图生图/新春贺岁表情包变身相机人像写真妆容图生图_2087414745233186817.json, 图片生成/图生图/表情包变身相机 一键新春贺岁妆容人像写真生成_2110350405938012162.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_368

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2K高清分镜切割机｜图生图一键拆分镜帧出图_2092142854641635329.json、图片生成/图生图/分镜切割机-2k_2087408324949139457.json、图片生成/图生图/新春贺岁变身相机｜表情包人像写真妆容图生图_2092161264884731906.json、图片生成/图生图/新春贺岁表情包变身相机人像写真妆容图生图_2087414745233186817.json、图片生成/图生图/表情包变身相机 一键新春贺岁妆容人像写真生成_2110350405938012162.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `EmptyLatentImage`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy joinImageBatch`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 3/5 个有
- `RH_Nano_Banana2_Image2Image` —— 3/5 个有
- `easy anythingIndexSwitch` —— 3/5 个有
- `CR Image Grid Panel` —— 2/5 个有
- `ImageListToBatch+` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

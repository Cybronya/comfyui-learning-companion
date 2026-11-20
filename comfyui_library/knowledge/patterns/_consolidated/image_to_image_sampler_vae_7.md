---
name: image_to_image_sampler_vae_7
type: Image To Image
frequency: 16
level: moderate
coverage: 0.86725
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/【官方】去除照片光影_1988973930666921986.json, 平台全量/一键换装-qwen-image-edit-2511_2083150953930383361.json, 平台全量/一键生成背景 Qwen-Image-Edit 白底产品生成场景  电商产品生成场景产品图位置保持不变_2001851330203402241.json, 平台全量/产品_模特一键换背景  生成场景背景 Qwen-Image-Edit 产品图位置保持不变，产品场景随_1999354149709938689.json, 平台全量/产品多角度展示-Qwen2509_1985704266025377793.json, 平台全量/光影迁移_2000120367702212609.json, 平台全量/图像精准编辑｜+特效 LoRA（图中需绘线条（黑色或白色）大致范围）Qwen Edit 2511_2044313799485820930.json, 平台全量/图片视角转变 千问Qwen-Edit2509 （PLus版）_1990226876994121730.json, 平台全量/工作流进阶功能篇5-电商精准溶图重打光_2036367196527529985.json, 平台全量/电商精准溶图重打光_2034168341111246850.json, 平台全量/角度随心换_1990768553055952898.json, 平台全量/角度随心换_2022240416229236737.json, 平台全量/🔥电商产品“精准溶图 + 重打光” 告别生硬抠图，让产品完美融入场景!_2106687430463156225.json, 数字人/数字人/【老金驿站】Qwen2509肌肤改善器工作流_1985948966875537410.json, 数字人/数字人/替换物品，人物，让人物穿上你想要的衣服，鞋子_2032482079761502210.json, 视频生成/图生视频/qwen多视角转换工作流_1987730871912435714.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_7

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（平台全量/【官方】去除照片光影_1988973930666921986.json、平台全量/一键换装-qwen-image-edit-2511_2083150953930383361.json、平台全量/一键生成背景 Qwen-Image-Edit 白底产品生成场景  电商产品生成场景产品图位置保持不变_2001851330203402241.json、平台全量/产品_模特一键换背景  生成场景背景 Qwen-Image-Edit 产品图位置保持不变，产品场景随_1999354149709938689.json、平台全量/产品多角度展示-Qwen2509_1985704266025377793.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 15/16 个有
- `UNETLoader` —— 15/16 个有
- `Image Comparer (rgthree)` —— 14/16 个有
- `easy imageSize` —— 8/16 个有
- `PreviewImage` —— 5/16 个有
- `AIO_Preprocessor` —— 2/16 个有
- `Note Plus (mtb)` —— 1/16 个有
- `PainterNode` —— 1/16 个有
- `Power Lora Loader (rgthree)` —— 1/16 个有
- `TT_img_enc` —— 1/16 个有
- `UnetLoaderGGUF` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 16 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 16 | 67% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，16 个样本
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（15/16 个样本）：Steps较低可能导致细节不足

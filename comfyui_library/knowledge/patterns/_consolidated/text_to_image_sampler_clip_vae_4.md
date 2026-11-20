---
name: text_to_image_sampler_clip_vae_4
type: Text To Image
frequency: 19
level: moderate
coverage: 0.976579
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json, 图片生成/文生图/Z-Image_1996570015086297090.json, 图片生成/文生图/Z-Image文生图_2094304743563812866.json, 图片生成/文生图/Z-image 全能模型_1994451694316625922.json, 图片生成/文生图/Z-image 文生图_2006288280186265601.json, 图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json, 图片生成/文生图/Z-image+lora人像更换_2007628288839127041.json, 图片生成/文生图/Z-image-turbo极速文生图（内置身材调节Lora）_2101265914195955713.json, 图片生成/文生图/Z-image基础文生图工作流（含放大）_2001871745982296066.json, 图片生成/文生图/Z-image文生图-网图生成器（超快）_2029000243047567361.json, 图片生成/文生图/Z-image文生图-（超快）_2056293996040900610.json, 图片生成/文生图/Z-image超写实文生图工作流_2099335310260916225.json, 图片生成/文生图/Z-image超极速文生图（内置巨乳身材调节Lora）_2047308071554256898.json, 图片生成/文生图/Z-image，文生图，10秒出图zip_2048723569391181825.json, 图片生成/文生图/Z-image，新王登基，Flux2退散_1993500745689481218.json, 图片生成/文生图/女装工作流_2009116986424430593.json, 图片生成/文生图/摄影-文生图-Z-image-turbo_2096447342345015297.json, 图片生成/文生图/摄影质感文生图_2113993779647705089.json, 图片生成/文生图/摄影质感文生图工作流｜Z-image turbo快速出图生成_2096729113515089922.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json、图片生成/文生图/Z-Image_1996570015086297090.json、图片生成/文生图/Z-Image文生图_2094304743563812866.json、图片生成/文生图/Z-image 全能模型_1994451694316625922.json、图片生成/文生图/Z-image 文生图_2006288280186265601.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 18/19 个有
- `UNETLoader` —— 18/19 个有
- `ImageUpscaleWithModel` —— 15/19 个有
- `UpscaleModelLoader` —— 15/19 个有
- `ImageSharpen` —— 8/19 个有
- `LoraLoaderModelOnly` —— 6/19 个有
- `ImageFromBatch` —— 4/19 个有
- `PreviewImage` —— 4/19 个有
- `LayerColor: Brightness & Contrast` —— 3/19 个有
- `JjkText` —— 2/19 个有
- `solarL_SaveImagesToZip` —— 2/19 个有
- `CompressImages` —— 1/19 个有
- `Int` —— 1/19 个有
- `LoraLoader` —— 1/19 个有
- `UnetLoaderGGUF` —— 1/19 个有
- `孤海注释` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1920 | 19 | 68% |
| 高度 | 1920 | 80 - 1920 | 19 | 68% |
| 采样步数 | 10 | 4 - 20 | 19 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 19 | 22% |
| 采样算法 | euler | - | 19 | 79% |
| 调度器 | simple | - | 19 | 84% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1920，19 个样本
- 高度 中位数 1920，观测区间 80 - 1920，19 个样本
- 采样步数 中位数 10，观测区间 4 - 20，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，19 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，19 个样本，一致性 79%
- 调度器 最常用 simple，19 个样本，一致性 84%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）

---
name: text_to_image_lora_sampler_clip_377
type: Text To Image
frequency: 5
level: strong
coverage: 0.9114
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/背景图批量出图神器｜文生图一句提示词直出，场景背景素材随心换_2100476653272129538.json, 图片生成/文生图/逼真美女人像写真美少女文生图 Krea2 高清质感_2094223594124566529.json, 图片生成/文生图/逼真美女人像写真｜Krea2文生图美少女生成_2094345828281438210.json, 图片生成/文生图/逼真美女人像写真｜Krea2文生图美少女生成_2094581026407407618.json, 图片生成/文生图/长腿模特人像写真美少女文生图 Krea2 身材比例优化_2094214837135036417.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_377

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/背景图批量出图神器｜文生图一句提示词直出，场景背景素材随心换_2100476653272129538.json、图片生成/文生图/逼真美女人像写真美少女文生图 Krea2 高清质感_2094223594124566529.json、图片生成/文生图/逼真美女人像写真｜Krea2文生图美少女生成_2094345828281438210.json、图片生成/文生图/逼真美女人像写真｜Krea2文生图美少女生成_2094581026407407618.json、图片生成/文生图/长腿模特人像写真美少女文生图 Krea2 身材比例优化_2094214837135036417.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `VOSR2ModelLoader` —— 1/5 个有
- `VOSR2Upscale` —— 1/5 个有

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
| Steps较低可能导致细节不足 | 11/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（11/5 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_113
type: Text To Image
frequency: 13
level: weak
coverage: 0.912385
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-双采大胸版_2089250736138964993.json, 图片生成/文生图/Krea2-模糊感美女生成_2091102588728074241.json, 图片生成/文生图/Krea2-百变美女2_2094969323881320450.json, 图片生成/文生图/Krea2-百变美女_2093983095182684161.json, 图片生成/文生图/Krea2-美女生成双采_2088668185955491842.json, 图片生成/文生图/Krea2-美女生成语义增强版_2089887983045533698.json, 图片生成/文生图/Krea2模糊感美女生成｜文生图一键直出创作_2091289552974598145.json, 图片生成/文生图/Krea2美女生成双采｜文生图高清直出创作_2091314568529276929.json, 图片生成/文生图/Krea2美女生成语义增强版｜文生图一键生成直出_2091315805886697473.json, 图片生成/文生图/Pornmaster krea2 t2i Raw加Turbo｜人像写真写实文生图_2099150332872978434.json, 图片生成/文生图/双采自用版｜Krea2文生图大胸写真生成_2089470548073078786.json, 图片生成/文生图/百变美女一键生成｜Krea2文生图高清工作流_2094343906937888769.json, 图片生成/文生图/百变美女不锁脸文生图 Krea2 多样人像lora生成_2094219223668191233.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea2-双采大胸版_2089250736138964993.json、图片生成/文生图/Krea2-模糊感美女生成_2091102588728074241.json、图片生成/文生图/Krea2-百变美女2_2094969323881320450.json、图片生成/文生图/Krea2-百变美女_2093983095182684161.json、图片生成/文生图/Krea2-美女生成双采_2088668185955491842.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 12/13 个有
- `PrimitiveBoolean` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `Switch string [Crystools]` —— 12/13 个有
- `JjkText` —— 7/13 个有
- `solarL_SaveImagesToZip` —— 7/13 个有
- `孤海注释` —— 7/13 个有
- `KSamplerAdvanced` —— 5/13 个有
- `ConditioningRebalanceKrea2` —— 2/13 个有
- `StringConcatenate` —— 2/13 个有
- `CompressImages` —— 1/13 个有
- `Int` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 12 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 2.5 - 8 | 13 | 64% |
| 采样算法 | er_sde | - | 13 | 54% |
| 调度器 | beta | - | 13 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 1024 | 13 | 8% |
| 高度 | 80 | 80 - 1536 | 13 | 2% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 2.5 - 8，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 54%
- 调度器 最常用 beta，13 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，13 个样本，取值分散，一致性仅 8%
- 高度 中位数 80，观测区间 80 - 1536，13 个样本，取值分散，一致性仅 2%
- 高发问题（27/13 个样本）：Steps较低可能导致细节不足

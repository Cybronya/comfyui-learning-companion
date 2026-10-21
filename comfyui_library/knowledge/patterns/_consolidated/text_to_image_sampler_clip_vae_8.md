---
name: text_to_image_sampler_clip_vae_8
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9064
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [SDXL Resolutions (JPS), CR Text Concatenate]
members: [图片生成/文生图/1930910447648571394.json, 图片生成/文生图/1948416477526392833.json, 图片生成/文生图/1953069809741271041.json, 图片生成/文生图/1953112797149392898.json, 图片生成/文生图/1953349482882760705.json, 图片生成/文生图/1957421621072031746.json, 图片生成/文生图/1959617318458437634.json, 图片生成/文生图/1987561612901068801.json, 图片生成/文生图/Y-qwen_image_2512_workflow_2006635024417824770.json, 图片生成/文生图/z_mage+古风_lora直出高清图_2001669410228170753.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1930910447648571394.json、图片生成/文生图/1948416477526392833.json、图片生成/文生图/1953069809741271041.json、图片生成/文生图/1953112797149392898.json、图片生成/文生图/1953349482882760705.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `UNETLoader` —— 8/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `PreviewImage` —— 3/10 个有
- `NunchakuQwenImageDiTLoader` —— 2/10 个有
- `SDXL Resolutions (JPS)` —— 2/10 个有
- `TextEncodeQwenImageEditPlus` —— 2/10 个有
- `Textbox` —— 2/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `DyPE_FLUX` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 4 - 50 | 10 | 26% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 3.5 | 10 | 50% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 932 | 720 - 1280 | 10 | 82% |
| 高度 | 1280 | 720 - 1584 | 10 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 4 - 50，10 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 3.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 932，观测区间 720 - 1280，10 个样本，取值集中（一致性 82%）
- 高度 中位数 1280，观测区间 720 - 1584，10 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：SDXL Resolutions (JPS)、CR Text Concatenate

---
name: text_to_image_lora_sampler_clip_292
type: Text To Image
frequency: 3
level: strong
coverage: 0.763667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR Text Replace]
members: [图片生成/文生图/1985265291271749633.json, 图片生成/文生图/1986356775588921346.json, 图片生成/文生图/Z-image-base-极速自动文生图（4步出图）_2021738815794188290.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_292

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1985265291271749633.json、图片生成/文生图/1986356775588921346.json、图片生成/文生图/Z-image-base-极速自动文生图（4步出图）_2021738815794188290.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `CR Text Replace` —— 2/3 个有
- `ProcessString` —— 2/3 个有
- `BetterFilmGrain` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1536 | 3 | 69% |
| 高度 | 1280 | 1280 - 1536 | 3 | 91% |
| 采样步数 | 8 | 6 - 8 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2m | - | 3 | 33% |
| 调度器 | sgm_uniform | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1536，3 个样本
- 高度 中位数 1280，观测区间 1280 - 1536，3 个样本，取值集中（一致性 91%）
- 采样步数 中位数 8，观测区间 6 - 8，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，3 个样本，一致性 33%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Replace

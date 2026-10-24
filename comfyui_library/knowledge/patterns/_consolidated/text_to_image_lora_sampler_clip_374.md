---
name: text_to_image_lora_sampler_clip_374
type: Text To Image
frequency: 5
level: strong
coverage: 0.9746
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json, 图片生成/文生图/Z-image基础文生图，zimage文生图_1998203845559902209.json, 图片生成/文生图/Z-image文生图_2002645259123322881.json, 图片生成/文生图/Z-image文生图_2003370209052401665.json, 图片生成/文生图/krea2文生图+官方LORA_2069978232052600834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_374

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image_lora  （丝袜版）_1995812666759327745.json、图片生成/文生图/Z-image基础文生图，zimage文生图_1998203845559902209.json、图片生成/文生图/Z-image文生图_2002645259123322881.json、图片生成/文生图/Z-image文生图_2003370209052401665.json、图片生成/文生图/krea2文生图+官方LORA_2069978232052600834.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/5 个有
- `CompressImages` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Float` —— 1/5 个有
- `JoinStringMulti` —— 1/5 个有
- `VHS_Unbatch` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1024 - 1920 | 5 | 75% |
| 高度 | 1080 | 720 - 1920 | 5 | 67% |
| 采样步数 | 10 | 8 - 10 | 5 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1024 - 1920，5 个样本
- 高度 中位数 1080，观测区间 720 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

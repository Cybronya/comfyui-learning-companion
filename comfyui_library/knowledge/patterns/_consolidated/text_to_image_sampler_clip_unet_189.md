---
name: text_to_image_sampler_clip_unet_189
type: Text To Image
frequency: 3
level: strong
coverage: 0.841
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, EmptyLatentImage, JDCN_StringToList, KSampler, ProcessString, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2纯欲美学工作流_2069352137276088322.json, 图片生成/文生图/极致美学文生图（姿态向）V2.0_1986356775588921346.json, 图片生成/文生图/极致美学文生图（真实+姿态向）V3.0_1993866096310763521.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_189

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2纯欲美学工作流_2069352137276088322.json、图片生成/文生图/极致美学文生图（姿态向）V2.0_1986356775588921346.json、图片生成/文生图/极致美学文生图（真实+姿态向）V3.0_1993866096310763521.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `easy int` —— 2/3 个有
- `BetterFilmGrain` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1024 - 1280 | 3 | 90% |
| 高度 | 1536 | 1536 - 1920 | 3 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
- 高度 中位数 1536，观测区间 1536 - 1920，3 个样本，取值集中（一致性 89%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

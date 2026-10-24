---
name: text_to_image_lora_sampler_clip_650
type: Text To Image
frequency: 2
level: weak
coverage: 0.872
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Replace, EmptyLatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/极致美学文生图（姿态向）V2.0_1986356775588921346.json, 图片生成/文生图/极致美学文生图（姿态向）v1.5_1985265291271749633.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_650

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/极致美学文生图（姿态向）V2.0_1986356775588921346.json、图片生成/文生图/极致美学文生图（姿态向）v1.5_1985265291271749633.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `BetterFilmGrain` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 1408 | - | 2 | 91% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

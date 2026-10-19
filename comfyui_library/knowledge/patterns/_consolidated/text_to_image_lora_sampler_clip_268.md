---
name: text_to_image_lora_sampler_clip_268
type: Text To Image
frequency: 2
level: weak
coverage: 0.7795
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [String Literal, CR Text Concatenate, Text Multiline, easy isMaskEmpty]
members: [图片生成/图生图/2071358346015371266.json, 图片生成/文生图/1962073493561085953.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_268

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2071358346015371266.json、图片生成/文生图/1962073493561085953.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `MultiTextConcatenate` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `String Literal` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `easy isMaskEmpty` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 80% |
| 高度 | 1232 | - | 2 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 1232，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、CR Text Concatenate、Text Multiline、easy isMaskEmpty
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

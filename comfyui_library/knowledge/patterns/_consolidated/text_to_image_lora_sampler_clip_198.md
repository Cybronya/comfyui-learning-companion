---
name: text_to_image_lora_sampler_clip_198
type: Text To Image
frequency: 4
level: weak
coverage: 0.79225
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, Switch any [Crystools]]
members: [图片生成/文生图/1969762845573476353.json, 图片生成/文生图/1969885972878008322.json, 图片生成/文生图/1986279659136569345.json, 图片生成/文生图/1988431547948818433.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_198

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1969762845573476353.json、图片生成/文生图/1969885972878008322.json、图片生成/文生图/1986279659136569345.json、图片生成/文生图/1988431547948818433.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ConcatText_Zho` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `Switch any [Crystools]` —— 2/4 个有
- `InversionDemoLazyIndexSwitch` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `QwenEditResolution` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16.5 | 8 - 25 | 4 | 48% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 3.5 | 4 | 44% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1004 | 16 - 1600 | 4 | 37% |
| 高度 | 1188 | 16 - 1600 | 4 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16.5，观测区间 8 - 25，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1004，观测区间 16 - 1600，4 个样本，取值分散，一致性仅 37%
- 高度 中位数 1188，观测区间 16 - 1600，4 个样本，取值分散，一致性仅 37%
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Switch any [Crystools]

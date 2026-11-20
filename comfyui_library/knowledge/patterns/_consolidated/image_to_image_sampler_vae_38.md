---
name: image_to_image_sampler_vae_38
type: Image To Image
frequency: 3
level: moderate
coverage: 0.703333
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PrimitiveStringMultiline, ReferenceLatent, SDXLEmptyLatentSizePicker+, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超火的图片转手办（极速版）_2028761764279619585.json, 平台全量/人物一致性文字控图_qwenedit极速版_nunchaku_1965787226070257665.json, 平台全量/手办_qwenedit双节棍版本（30s出图急速版）_1966141523383545858.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/超火的图片转手办（极速版）_2028761764279619585.json、平台全量/人物一致性文字控图_qwenedit极速版_nunchaku_1965787226070257665.json、平台全量/手办_qwenedit双节棍版本（30s出图急速版）_1966141523383545858.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PrimitiveStringMultiline`
- `ReferenceLatent`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningAverage` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `Bjornulf_AnythingToText` —— 1/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 3 | 67% |
| 高度 | 1 | 1 - 1328 | 3 | 0% |
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，3 个样本，一致性 67%
- 高度 中位数 1，观测区间 1 - 1328，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

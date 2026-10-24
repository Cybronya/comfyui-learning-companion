---
name: image_to_image_sampler_vae_33
type: Image To Image
frequency: 2
level: weak
coverage: 0.7305
common_nodes: [CFGNorm, CLIPLoader, ConditioningAverage, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PrimitiveStringMultiline, ReferenceLatent, SDXLEmptyLatentSizePicker+, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/三视图一键生成多视角三视图_人物一致性人物转（加速版）_1967533621051580418.json, 图片生成/图生图/超火的图片转手办（极速版）_2028761764279619585.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/三视图一键生成多视角三视图_人物一致性人物转（加速版）_1967533621051580418.json、图片生成/图生图/超火的图片转手办（极速版）_2028761764279619585.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningAverage`
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
- `CR Simple Image Compare` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy imageSize` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1328 | - | 1 | 100% |
| 高度 | 664.5 | - | 2 | 0% |
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高度 中位数 664.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

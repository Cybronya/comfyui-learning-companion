---
name: image_to_image_sampler_vae_20
type: Image To Image
frequency: 6
level: moderate
coverage: 0.852667
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen edit 双人合影_1972189838340517889.json, 图片生成/图生图/qwen 双人合影_1970745203600596993.json, 图片生成/图生图/qwen 双人拍立得合影_1972850394676285442.json, 图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1971470726085722113.json, 图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1977867242929016833.json, 图片生成/图生图/站立拍摄 2511_2037007001368141825.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/qwen edit 双人合影_1972189838340517889.json、图片生成/图生图/qwen 双人合影_1970745203600596993.json、图片生成/图生图/qwen 双人拍立得合影_1972850394676285442.json、图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1971470726085722113.json、图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1977867242929016833.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ReferenceLatent` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `easy imageConcat` —— 4/6 个有
- `ConditioningAverage` —— 3/6 个有
- `SDXLEmptyLatentSizePicker+` —— 3/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `JjkText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 704x1408 (0.5) | - | 4 | 75% |
| 高度 | 1 | 1 - 1664 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 最常用 704x1408 (0.5)，4 个样本，一致性 75%
- 高度 中位数 1，观测区间 1 - 1664，4 个样本，取值分散，一致性仅 0%
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

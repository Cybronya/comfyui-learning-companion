---
name: image_to_image_sampler_clip_vae_42
type: Image To Image
frequency: 4
level: moderate
coverage: 0.89225
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物线稿提取_2031290016340647937.json, 图片生成/图生图/最好用的 nunchaku flux kontext 去水印_2053752457087467522.json, 图片生成/图生图/比中指_1953770429464891394.json, 图片生成/图生图/陶瓷浮雕_2032083602745331713.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物线稿提取_2031290016340647937.json、图片生成/图生图/最好用的 nunchaku flux kontext 去水印_2053752457087467522.json、图片生成/图生图/比中指_1953770429464891394.json、图片生成/图生图/陶瓷浮雕_2032083602745331713.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `EnhancedLoadDiffusionModel` —— 2/4 个有
- `NunchakuFluxDiTLoader` —— 2/4 个有
- `RepeatLatentBatch` —— 2/4 个有
- `Text` —— 2/4 个有
- `ColorCorrectOfUtils` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `NunchakuFluxLoraLoader` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `easy indexAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | 8 - 25 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17.5，观测区间 8 - 25，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

---
name: image_to_image_sampler_unet_vae_46
type: Image To Image
frequency: 4
level: moderate
coverage: 0.897
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/251114 换yi_1987458941137391617.json, 图片生成/图生图/【遇见AI】Qwen-image-edit 图生图基础_2051187067786407937.json, 图片生成/文生图/万物cheems狗-qwen_1960294148945358849.json, 图片生成/文生图/双胞胎 2511_2027523066724618241.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_46

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/251114 换yi_1987458941137391617.json、图片生成/图生图/【遇见AI】Qwen-image-edit 图生图基础_2051187067786407937.json、图片生成/文生图/万物cheems狗-qwen_1960294148945358849.json、图片生成/文生图/双胞胎 2511_2027523066724618241.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MultiTextConcatenate` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `easy int` —— 2/4 个有
- `CR Prompt List` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `Float` —— 1/4 个有
- `LatentUpscaleBy` —— 1/4 个有
- `PIP_图像联结` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `孤海图像缩放按像素` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1200 | 3 | 92% |
| 高度 | 1536 | 1024 - 1640 | 3 | 81% |
| 采样步数 | 17 | 4 - 40 | 4 | 18% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 3.5 | 4 | 47% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.98 - 1 | 4 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1200，3 个样本，取值集中（一致性 92%）
- 高度 中位数 1536，观测区间 1024 - 1640，3 个样本，取值集中（一致性 81%）
- 采样步数 中位数 17，观测区间 4 - 40，4 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.98 - 1，4 个样本，取值集中（一致性 99%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足

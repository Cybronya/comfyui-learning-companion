---
name: image_to_image_lora_sampler_unet_156
type: Image To Image
frequency: 4
level: moderate
coverage: 0.9905
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenImage-Edit-2511电影分镜自动生成_2059802568074809346.json, 图片生成/图生图/双图分镜 2511_2024081531601424385.json, 图片生成/图生图/提取服装为产品图 2511_2020424468195184642.json, 图片生成/图生图/马甲线 2511_2021155007344676865.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_156

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QwenImage-Edit-2511电影分镜自动生成_2059802568074809346.json、图片生成/图生图/双图分镜 2511_2024081531601424385.json、图片生成/图生图/提取服装为产品图 2511_2020424468195184642.json、图片生成/图生图/马甲线 2511_2021155007344676865.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/4 个有
- `PIP_图像联结` —— 3/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `SomethingToString` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy promptLine` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 928 - 1536 | 3 | 77% |
| 高度 | 1536 | 1024 - 1664 | 3 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 928 - 1536，3 个样本
- 高度 中位数 1536，观测区间 1024 - 1664，3 个样本，取值集中（一致性 80%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

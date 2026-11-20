---
name: image_to_image_sampler_vae_31
type: Image To Image
frequency: 3
level: moderate
coverage: 0.670667
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, GetNode, ImageScaleToTotalPixels, ImageStitch, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/双节棍版Qwen-Image模型2509多图编辑_1976884280855085057.json, 图片生成/图生图/双节棍版千问编辑模型_1987197398025965570.json, 图片生成/文生图/一致性角色生成器_1959543923909799937.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_31

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/双节棍版Qwen-Image模型2509多图编辑_1976884280855085057.json、图片生成/图生图/双节棍版千问编辑模型_1987197398025965570.json、图片生成/文生图/一致性角色生成器_1959543923909799937.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `AILab_QwenVL_Advanced` —— 1/3 个有
- `JWStringGetLine` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 8 - 50 | 3 | 45% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 8 - 50，3 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（8/3 个样本）：Steps较低可能导致细节不足

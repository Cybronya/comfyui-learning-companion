---
name: image_to_image_sampler_clip_unet_124
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8494
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen2512洗图&批量获取不同比例图_2054158368167743489.json, 图片生成/图生图/Z-image图生图-真实感洗图_1996077315346087937.json, 图片生成/图生图/Z-image洗图图生图_1995800646467072001.json, 图片生成/文生图/2课_文生图_图生图工作流_2116702727358205954.json, 图片生成/文生图/2课_文生图_图生图工作流_2116716960980492290.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen2512洗图&批量获取不同比例图_2054158368167743489.json、图片生成/图生图/Z-image图生图-真实感洗图_1996077315346087937.json、图片生成/图生图/Z-image洗图图生图_1995800646467072001.json、图片生成/文生图/2课_文生图_图生图工作流_2116702727358205954.json、图片生成/文生图/2课_文生图_图生图工作流_2116716960980492290.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `QwenImageLatentAspectRatio` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `ImageScaleBy` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 10 - 15 | 5 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 0.78 | 0.3 - 1 | 5 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 10 - 15，5 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 0.78，观测区间 0.3 - 1，5 个样本

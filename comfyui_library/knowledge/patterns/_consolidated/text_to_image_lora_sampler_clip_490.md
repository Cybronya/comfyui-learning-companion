---
name: text_to_image_lora_sampler_clip_490
type: Text To Image
frequency: 3
level: moderate
coverage: 0.920333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-IMAGE-BASE-真人转动漫_2027600635322961922.json, 图片生成/图生图/qwen编辑plus漫画分格_1980222586971992066.json, 图片生成/图生图/wojk画风-qwen_2000345669170757633.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_490

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-IMAGE-BASE-真人转动漫_2027600635322961922.json、图片生成/图生图/qwen编辑plus漫画分格_1980222586971992066.json、图片生成/图生图/wojk画风-qwen_2000345669170757633.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1528 | 1024 - 1536 | 3 | 82% |
| 采样步数 | 8 | 8 - 15 | 3 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1528，观测区间 1024 - 1536，3 个样本，取值集中（一致性 82%）
- 采样步数 中位数 8，观测区间 8 - 15，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

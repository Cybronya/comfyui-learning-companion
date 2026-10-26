---
name: text_to_image_lora_sampler_clip_536
type: Text To Image
frequency: 3
level: strong
coverage: 0.923667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/躺在沙发上qwen_2004684453886783489.json, 图片生成/图生图/车拍女生qwen_2002233071887892481.json, 图片生成/文生图/影视二创自定义-人物多角度_2008857414627495938.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_536

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/躺在沙发上qwen_2004684453886783489.json、图片生成/图生图/车拍女生qwen_2002233071887892481.json、图片生成/文生图/影视二创自定义-人物多角度_2008857414627495938.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
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
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `FlashVSRNode` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 928 | 928 - 1024 | 3 | 95% |
| 高度 | 1664 | 1536 - 1664 | 3 | 96% |
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 928，观测区间 928 - 1024，3 个样本，取值集中（一致性 95%）
- 高度 中位数 1664，观测区间 1536 - 1664，3 个样本，取值集中（一致性 96%）
- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

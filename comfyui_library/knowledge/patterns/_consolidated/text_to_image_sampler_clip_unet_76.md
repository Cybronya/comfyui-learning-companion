---
name: text_to_image_sampler_clip_unet_76
type: Text To Image
frequency: 6
level: moderate
coverage: 0.872833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1959919853350105089.json, 图片生成/文生图/1969671833953988610.json, 图片生成/文生图/1970727639172476929.json, 图片生成/文生图/1988965178039480322.json, 图片生成/文生图/9 个 Krea 2 LoRA 测试_2069657247956946945.json, 图片生成/文生图/Krea2-二次元模型总控-云端版_2095727543704965121.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_76

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1959919853350105089.json、图片生成/文生图/1969671833953988610.json、图片生成/文生图/1970727639172476929.json、图片生成/文生图/1988965178039480322.json、图片生成/文生图/9 个 Krea 2 LoRA 测试_2069657247956946945.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `FluxResolutionNode` —— 3/6 个有
- `ModelSamplingSD3` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 512 - 1280 | 6 | 70% |
| 高度 | 1072 | 512 - 1984 | 6 | 55% |
| 采样步数 | 19.5 | 8 - 35 | 6 | 41% |
| Prompt 约束强度(CFG) | 2 | 1 - 4 | 6 | 44% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 512 - 1280，6 个样本
- 高度 中位数 1072，观测区间 512 - 1984，6 个样本
- 采样步数 中位数 19.5，观测区间 8 - 35，6 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 4，6 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（14/6 个样本）：Steps较低可能导致细节不足

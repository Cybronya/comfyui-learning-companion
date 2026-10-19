---
name: image_to_image_lora_sampler_unet_13
type: Image To Image
frequency: 3
level: strong
coverage: 0.816667
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [SimpleMath+, Text Load Line From File, Text Multiline, easy batchAnything, easy forLoopEnd, easy forLoopStart]
members: [图片生成/图生图/2062044352884592641.json, 图片生成/文生图/1963120825828356098.json, 图片生成/文生图/1977629873571287042.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2062044352884592641.json、图片生成/文生图/1963120825828356098.json、图片生成/文生图/1977629873571287042.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `TextEncodeQwenImageEdit` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `LynxInsightFaceCrop` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `Text Load Line From File` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、Text Load Line From File、Text Multiline、easy batchAnything、easy forLoopEnd

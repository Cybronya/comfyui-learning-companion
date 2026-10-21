---
name: image_to_image_lora_sampler_unet_24
type: Image To Image
frequency: 4
level: strong
coverage: 0.85175
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [SimpleMath+, Text Load Line From File, Text Multiline, easy batchAnything, easy forLoopEnd, easy forLoopStart]
members: [图片生成/图生图/2062044352884592641.json, 图片生成/文生图/1963120825828356098.json, 图片生成/文生图/1977629873571287042.json, 图片生成/文生图/多重视角的人物_2010964416438738945.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_24

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2062044352884592641.json、图片生成/文生图/1963120825828356098.json、图片生成/文生图/1977629873571287042.json、图片生成/文生图/多重视角的人物_2010964416438738945.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PreviewImage` —— 3/4 个有
- `TextEncodeQwenImageEdit` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `SimpleMath+` —— 2/4 个有
- `Text Load Line From File` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy batchAnything` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LynxInsightFaceCrop` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、Text Load Line From File、Text Multiline、easy batchAnything、easy forLoopEnd

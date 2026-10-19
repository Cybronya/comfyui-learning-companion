---
name: text_to_image_lora_sampler_clip_174
type: Text To Image
frequency: 5
level: moderate
coverage: 0.6258
common_nodes: [CLIPTextEncode, CR Aspect Ratio, CR Text, DualCLIPLoader, EmptyLatentImage, KSampler, LoraLoader, SaveImage, Text Load Line From File, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart]
problems: []
missing: [CR Aspect Ratio, CR Text, Text Load Line From File, easy forLoopEnd, easy forLoopStart]
members: [图片生成/文生图/1962501033920446466.json, 图片生成/文生图/1971808932454985729.json, 图片生成/文生图/1981980642160320514.json, 图片生成/文生图/1985473405493329922.json, 图片生成/文生图/1986280122842054657.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_174

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1962501033920446466.json、图片生成/文生图/1971808932454985729.json、图片生成/文生图/1981980642160320514.json、图片生成/文生图/1985473405493329922.json、图片生成/文生图/1986280122842054657.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Aspect Ratio`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `Text Load Line From File`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 5 | 51% |
| 采样算法 | dpmpp_2m | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 896 | 512 - 896 | 5 | 81% |
| 高度 | 1152 | 512 - 1152 | 5 | 75% |
| LoRA 模型强度 | 0.6 | 0.6 - 1 | 5 | 76% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，5 个样本
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 896，5 个样本，取值集中（一致性 81%）
- 高度 中位数 1152，观测区间 512 - 1152，5 个样本
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Aspect Ratio、CR Text、Text Load Line From File、easy forLoopEnd、easy forLoopStart

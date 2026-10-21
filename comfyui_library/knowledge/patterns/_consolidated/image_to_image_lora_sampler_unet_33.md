---
name: image_to_image_lora_sampler_unet_33
type: Image To Image
frequency: 2
level: weak
coverage: 0.643
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy imageConcat, CR Prompt List]
members: [图片生成/文生图/1959223893091364865.json, 图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1959223893091364865.json、图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 928 | - | 1 | 100% |
| 高度 | 1664 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy imageConcat、CR Prompt List
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

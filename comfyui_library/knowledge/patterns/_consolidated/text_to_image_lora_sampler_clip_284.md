---
name: text_to_image_lora_sampler_clip_284
type: Text To Image
frequency: 2
level: weak
coverage: 0.4555
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, ConstrainImage|pysssss, Create Grid Image from Batch, EmptyLatentImage, GetImageSize, GetNode, ImpactMakeImageList, Int, JWInteger, JjkText, JoinStrings, KSampler, LoadImage, Lora Loader, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, RH_Captioner, ReActorImageDublicator, SaveImage, Seed_, SetNode, Text, UNETLoader, VAEDecode, VAELoader, easy convertAnything, easy imageListToImageBatch, easy rangeFloat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [ConstrainImage|pysssss, Create Grid Image from Batch, easy convertAnything, easy imageListToImageBatch, easy rangeFloat, Lora Loader]
members: [图片生成/文生图/1960228137802084354.json, 图片生成/文生图/1970132982562496514.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_284

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1960228137802084354.json、图片生成/文生图/1970132982562496514.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `Create Grid Image from Batch`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `ImpactMakeImageList`
- `Int`
- `JWInteger`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `Lora Loader`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveInt`
- `RH_Captioner`
- `ReActorImageDublicator`
- `SaveImage`
- `Seed_`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy convertAnything`
- `easy imageListToImageBatch`
- `easy rangeFloat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PMRF` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ConstrainImage|pysssss、Create Grid Image from Batch、easy convertAnything、easy imageListToImageBatch、easy rangeFloat
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

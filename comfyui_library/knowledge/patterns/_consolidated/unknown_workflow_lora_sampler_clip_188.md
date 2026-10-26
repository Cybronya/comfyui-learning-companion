---
name: unknown_workflow_lora_sampler_clip_188
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.491
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Seed, ConditioningZeroOut, EmptyFlux2LatentImage, GetNode, KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler (Efficient), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SetNode, UNETLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-2-klein-9b-KV-fp8   EDIT  多图编辑_2032700123880361985.json, 图片生成/图生图/一键运行：flux-2-klein 各种人物证件照 、护照、学历照、驾驶证等 图生图_2035222817037357057.json, 图片生成/图生图/一间运行：flux-2-klein-fp8 多图edit 图像编辑控制_2012693709321670658.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_188

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux-2-klein-9b-KV-fp8   EDIT  多图编辑_2032700123880361985.json、图片生成/图生图/一键运行：flux-2-klein 各种人物证件照 、护照、学历照、驾驶证等 图生图_2035222817037357057.json、图片生成/图生图/一间运行：flux-2-klein-fp8 多图edit 图像编辑控制_2012693709321670658.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetNode`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler (Efficient)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SetNode`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `FluxKVCache` —— 2/3 个有
- `PromptExpand` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `easy textSwitch` —— 2/3 个有
- `AddBackgroundNode` —— 1/3 个有
- `HivisionLayOutNode` —— 1/3 个有
- `HivisionNode` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `ZHHivisionParamsNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

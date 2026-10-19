---
name: image_to_image_lora_sampler_clip_3
type: Image To Image
frequency: 4
level: strong
coverage: 0.78075
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, EasyCache, EmptySD3LatentImage, FluxGuidance, FluxKontextMultiReferenceLatentMethod, ImageScaleToMaxDimension, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ReferenceLatent, SaveImage, USOStyleReference, VAEDecode, VAEEncode]
problems: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy int]
members: [图片生成/文生图/1964700278945628161.json, 图片生成/文生图/1964700301171245058.json, 图片生成/文生图/1967842899364839426.json, 图片生成/文生图/1967842931103137793.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1964700278945628161.json、图片生成/文生图/1964700301171245058.json、图片生成/文生图/1967842899364839426.json、图片生成/文生图/1967842931103137793.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EasyCache`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToMaxDimension`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ReferenceLatent`
- `SaveImage`
- `USOStyleReference`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy int` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio V2、easy int

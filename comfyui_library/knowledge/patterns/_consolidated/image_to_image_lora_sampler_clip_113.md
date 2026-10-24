---
name: image_to_image_lora_sampler_clip_113
type: Image To Image
frequency: 3
level: strong
coverage: 0.959
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, DrawMaskOnImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MaskFillHoles, PreviewImage, PrimitiveFloat, RMBG, SAM3_Detect, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2082650396622934017.json, 图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2105123839469510658.json, 图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2105502599876268033.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2082650396622934017.json、图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2105123839469510658.json、图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2105502599876268033.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFillHoles`
- `PreviewImage`
- `PrimitiveFloat`
- `RMBG`
- `SAM3_Detect`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（12/3 个样本）：Steps较低可能导致细节不足

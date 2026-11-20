---
name: image_to_image_lora_sampler_clip_151
type: Image To Image
frequency: 3
level: strong
coverage: 0.703667
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DF_Integer, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageColorMatch+, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, ReferenceLatent, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy float, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/迄今超强人像商用级1分钟极速版可选8K无损超分高清放大！去油_AI味_胶粒加皮肤质感真实高清可选最大8K放大-优化3_1968904593688154114.json, 图片生成/图生图/迄今超强人像商用级1分钟极速版可选8K无损超分高清放大！去油_AI味_胶粒加皮肤质感真实高清可选最大8K放大-优化3_2114897437746880514.json, 图片生成/图生图/迄今超强人像商用级1分钟极速版可选8K无损超分高清放大！去油_AI味_胶粒加皮肤质感真实高清可选最大8K放大-优化3_2115341755087409153.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/迄今超强人像商用级1分钟极速版可选8K无损超分高清放大！去油_AI味_胶粒加皮肤质感真实高清可选最大8K放大-优化3_1968904593688154114.json、图片生成/图生图/迄今超强人像商用级1分钟极速版可选8K无损超分高清放大！去油_AI味_胶粒加皮肤质感真实高清可选最大8K放大-优化3_2114897437746880514.json、图片生成/图生图/迄今超强人像商用级1分钟极速版可选8K无损超分高清放大！去油_AI味_胶粒加皮肤质感真实高清可选最大8K放大-优化3_2115341755087409153.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DF_Integer`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageColorMatch+`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2Preprocess`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy float`
- `easy int`

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
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足

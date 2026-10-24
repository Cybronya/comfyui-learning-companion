---
name: image_to_image_lora_sampler_clip_23
type: Image To Image
frequency: 9
level: moderate
coverage: 0.907222
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI智能补光_1952658829760770050.json, 图片生成/图生图/AI智能补光_2099326768569217026.json, 图片生成/图生图/AI智能补光_2099666438209499137.json, 图片生成/图生图/F.Kontext 电商万物光影融合全能溶图产品打光_2043694360822288386.json, 图片生成/图生图/F.Kontext电商万物光影融合溶图产品打光_2054460915776532482.json, 图片生成/图生图/F.Kontext电商万物光影融合溶图产品打光_2057709154202120193.json, 图片生成/图生图/FLUX + LoRA 图生图工作流_2087431336314363906.json, 图片生成/图生图/Flux Kontext 万物移除_2010532864927997953.json, 图片生成/图生图/qwen2511 AIO老照片修复高清直出版_2005785362125520898.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/AI智能补光_1952658829760770050.json、图片生成/图生图/AI智能补光_2099326768569217026.json、图片生成/图生图/AI智能补光_2099666438209499137.json、图片生成/图生图/F.Kontext 电商万物光影融合全能溶图产品打光_2043694360822288386.json、图片生成/图生图/F.Kontext电商万物光影融合溶图产品打光_2054460915776532482.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `ReferenceLatent` —— 8/9 个有
- `PreviewImage` —— 6/9 个有
- `ImageUpscaleWithModel` —— 4/9 个有
- `UpscaleModelLoader` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `ImpactInt` —— 3/9 个有
- `LayerUtility: ImageScaleRestore V2` —— 3/9 个有
- `easy imageConcat` —— 3/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `CheckpointLoaderSimple` —— 1/9 个有
- `Image Compare (mtb)` —— 1/9 个有
- `ImageAndMaskPreview` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `Int` —— 1/9 个有
- `RepeatLatentBatch` —— 1/9 个有
- `TextEncodeQwenImageEditPlus` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 0.35 - 1 | 9 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，9 个样本

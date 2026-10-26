---
name: image_to_image_lora_sampler_clip_58
type: Image To Image
frequency: 5
level: strong
coverage: 0.8036
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), ImageResize+, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, Qwen3VL_Chat, ReferenceLatent, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlusPro_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen 洗图_2045070272067276801.json, 图片生成/图生图/光影融图 溶图打光 Product Lighting and Blending_ Lighting_2098935257696399361.json, 图片生成/图生图/光影融图_溶图打光_Product_Lighting_and_Blending_Lighting_2099338977345101825.json, 图片生成/图生图/光影融图_溶图打光_Product_Lighting_and_Blending_Lighting_2099670963033038849.json, 图片生成/图生图/融图_2049034534498344961.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen 洗图_2045070272067276801.json、图片生成/图生图/光影融图 溶图打光 Product Lighting and Blending_ Lighting_2098935257696399361.json、图片生成/图生图/光影融图_溶图打光_Product_Lighting_and_Blending_Lighting_2099338977345101825.json、图片生成/图生图/光影融图_溶图打光_Product_Lighting_and_Blending_Lighting_2099670963033038849.json、图片生成/图生图/融图_2049034534498344961.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3VL_Chat`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 4/5 个有
- `ColorMatch` —— 4/5 个有
- `SeedVR2` —— 4/5 个有
- `SeedVR2BlockSwap` —— 4/5 个有
- `CR Value` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 5 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，5 个样本，取值集中（一致性 96%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足

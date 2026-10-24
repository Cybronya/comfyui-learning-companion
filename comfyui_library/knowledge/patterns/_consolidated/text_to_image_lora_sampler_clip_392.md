---
name: text_to_image_lora_sampler_clip_392
type: Text To Image
frequency: 4
level: strong
coverage: 0.831
common_nodes: [AutoCropFaces, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), Image Paste Crop, ImageAndMaskPreview, ImageConcanate, ImageFlip+, ImageResizeKJv2, ImpactInt, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, Seed (rgthree), TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026Z-image人物换脸，超真实两种预览图像_2021387892832079874.json, 图片生成/图生图/Z-image_ 图生图 + 换脸 2025-12-01_1995429280454729730.json, 图片生成/图生图/图片通过文生图换脸_1999859296542261249.json, 图片生成/文生图/小钢炮最强Z-image 文生图换脸_1994240289994899457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_392

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2026Z-image人物换脸，超真实两种预览图像_2021387892832079874.json、图片生成/图生图/Z-image_ 图生图 + 换脸 2025-12-01_1995429280454729730.json、图片生成/图生图/图片通过文生图换脸_1999859296542261249.json、图片生成/文生图/小钢炮最强Z-image 文生图换脸_1994240289994899457.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `Image Paste Crop`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageFlip+`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `FaceAlign` —— 2/4 个有
- `FaceAnalysisModels` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Note Plus (mtb)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 720 | 4 | 100% |
| 高度 | 1280 | 1280 - 1280 | 4 | 100% |
| 采样步数 | 9 | 9 - 9 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 100% |
| 调度器 | bong_tangent | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 720，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，观测区间 9 - 9，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 100%
- 调度器 最常用 bong_tangent，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足

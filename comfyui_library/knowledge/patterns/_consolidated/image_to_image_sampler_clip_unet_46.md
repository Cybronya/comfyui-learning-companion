---
name: image_to_image_sampler_clip_unet_46
type: Image To Image
frequency: 8
level: moderate
coverage: 0.8885
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ComfyUI_qwen_image姿势控制自动穿戴_1971197174509977602.json, 图片生成/图生图/F2_klein单图改图_2056203791569039361.json, 图片生成/图生图/F2_klein图洗图_2056009934218768386.json, 图片生成/图生图/F2_klein图洗图_2056577800190119938.json, 图片生成/图生图/F2_klein指定区域重绘_2056253513142988802.json, 图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2015965598240477186.json, 图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2068640783539982338.json, 图片生成/图生图/Flux-2-klein-多图精准控制编辑工作流-万能贴_2016050666283732994.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_46

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/ComfyUI_qwen_image姿势控制自动穿戴_1971197174509977602.json、图片生成/图生图/F2_klein单图改图_2056203791569039361.json、图片生成/图生图/F2_klein图洗图_2056009934218768386.json、图片生成/图生图/F2_klein图洗图_2056577800190119938.json、图片生成/图生图/F2_klein指定区域重绘_2056253513142988802.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/8 个有
- `EmptyFlux2LatentImage` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `ReferenceLatent` —— 5/8 个有
- `GetImageSize` —— 4/8 个有
- `ImageCompositeMasked` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `LayerUtility: ColorImage` —— 3/8 个有
- `取色器_孤海` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `BiRefNetRMBG` —— 1/8 个有
- `FastCanvas` —— 1/8 个有
- `FastCanvasTool` —— 1/8 个有
- `OpenposePreprocessor` —— 1/8 个有
- `TextEncodeQwenImageEditPlus` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 20 | 8 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 8 | 84% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 8 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 20，8 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，8 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，8 个样本
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足

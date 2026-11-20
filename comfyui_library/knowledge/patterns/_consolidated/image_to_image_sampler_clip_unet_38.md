---
name: image_to_image_sampler_clip_unet_38
type: Image To Image
frequency: 9
level: moderate
coverage: 0.886111
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ComfyUI_qwen_image姿势控制自动穿戴_1971197174509977602.json, 图片生成/图生图/F2_klein单图改图_2056203791569039361.json, 图片生成/图生图/F2_klein指定区域重绘_2056253513142988802.json, 图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2015965598240477186.json, 图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2068640783539982338.json, 图片生成/图生图/flux-2-klein-单图编辑工作流_2015742060871028738.json, 图片生成/图生图/flux-Klein-OpenPose姿势参考_2016816089824501761.json, 图片生成/文生图/FLUX板块：FLUX2-Klein单图编辑工作流_2050044921289166849.json, 图片生成/文生图/FLUX板块：FLUX2-Klein多图编辑工作流_2050045080513327106.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/ComfyUI_qwen_image姿势控制自动穿戴_1971197174509977602.json、图片生成/图生图/F2_klein单图改图_2056203791569039361.json、图片生成/图生图/F2_klein指定区域重绘_2056253513142988802.json、图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2015965598240477186.json、图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2068640783539982338.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ReferenceLatent` —— 8/9 个有
- `PreviewImage` —— 7/9 个有
- `EmptyFlux2LatentImage` —— 6/9 个有
- `GetImageSize` —— 6/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `ImageCompositeMasked` —— 3/9 个有
- `LayerUtility: ColorImage` —— 3/9 个有
- `取色器_孤海` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `OpenposePreprocessor` —— 1/9 个有
- `TextEncodeQwenImageEditPlus` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 9 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 9 | 85% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，9 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，9 个样本，取值集中（一致性 85%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足

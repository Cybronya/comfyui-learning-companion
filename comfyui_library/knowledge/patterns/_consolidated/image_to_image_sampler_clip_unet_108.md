---
name: image_to_image_sampler_clip_unet_108
type: Image To Image
frequency: 4
level: weak
coverage: 0.87225
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F1图生图+SD放大-真人转动漫_1926456591355383809.json, 图片生成/图生图/F1图生图动漫转3D_1924937268736237570.json, 图片生成/图生图/FLUX1-DEV-FP16 SD放大工作流_1950552715225124865.json, 图片生成/图生图/FLUX1-DEV-FP16 SD放大工作流_2028354206830174210.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/F1图生图+SD放大-真人转动漫_1926456591355383809.json、图片生成/图生图/F1图生图动漫转3D_1924937268736237570.json、图片生成/图生图/FLUX1-DEV-FP16 SD放大工作流_1950552715225124865.json、图片生成/图生图/FLUX1-DEV-FP16 SD放大工作流_2028354206830174210.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `UltimateSDUpscale` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `ClipInterrogator` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `WD14Tagger|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | 4 - 30 | 4 | 24% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 3.5 | 4 | 44% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.3 | 0.1 - 0.75 | 4 | 24% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，观测区间 4 - 30，4 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.1 - 0.75，4 个样本，取值分散，一致性仅 24%
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足

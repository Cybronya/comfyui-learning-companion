---
name: image_to_image_upscale_sampler_clip_38
type: Image To Image
frequency: 4
level: moderate
coverage: 0.80075
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image图生图、反推、放大，无controlnet_1998247610295156737.json, 图片生成/图生图/Z-image超真实高清洗图-无AI感_2007465177616228353.json, 图片生成/图生图/z-image洗图_2064621958779727873.json, 平台全量/一键人物换装加强版-可更换头饰-自定义输出图像分辨率-FLUX2-Klein_2018496196620324866.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-image图生图、反推、放大，无controlnet_1998247610295156737.json、图片生成/图生图/Z-image超真实高清洗图-无AI感_2007465177616228353.json、图片生成/图生图/z-image洗图_2064621958779727873.json、平台全量/一键人物换装加强版-可更换头饰-自定义输出图像分辨率-FLUX2-Klein_2018496196620324866.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `JjkShowText` —— 1/4 个有
- `Qwen2.5VL` —— 1/4 个有
- `RH_Captioner_Pro` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy imageSize` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7.5 | 4 - 12 | 4 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.53 | 0.15 - 1 | 4 | 40% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7.5，观测区间 4 - 12，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.53，观测区间 0.15 - 1，4 个样本，取值分散，一致性仅 40%
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足

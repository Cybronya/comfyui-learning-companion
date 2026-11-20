---
name: image_to_image_sampler_clip_unet_77
type: Image To Image
frequency: 7
level: strong
coverage: 0.852857
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2、原创图-Piao-去AI感真实感洗图4K版_1998366496474718209.json, 图片生成/图生图/Red-Z-image + Qwen3自动二阶段真实感洗图2K版_1998245914441580545.json, 图片生成/图生图/Z image turbo反推洗图重绘+SeedVR放大_2009271280842838017.json, 图片生成/图生图/Z-image洗图_1995506021877604354.json, 图片生成/图生图/二次元转真人洗图工作流_2009091309725818882.json, 图片生成/图生图/图片洗图 去ai感_2020023646076538881.json, 图片生成/图生图/洗图+高清+Z-image+DPO_1994756022692614145.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2、原创图-Piao-去AI感真实感洗图4K版_1998366496474718209.json、图片生成/图生图/Red-Z-image + Qwen3自动二阶段真实感洗图2K版_1998245914441580545.json、图片生成/图生图/Z image turbo反推洗图重绘+SeedVR放大_2009271280842838017.json、图片生成/图生图/Z-image洗图_1995506021877604354.json、图片生成/图生图/二次元转真人洗图工作流_2009091309725818882.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `SeedVR2LoadDiTModel` —— 6/7 个有
- `SeedVR2LoadVAEModel` —— 6/7 个有
- `SeedVR2VideoUpscaler` —— 6/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ImageScaleBy` —— 4/7 个有
- `Any To Any` —— 3/7 个有
- `Anything Everywhere3` —— 3/7 个有
- `Float` —— 3/7 个有
- `VHS_SelectFilename` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `Int` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 7 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 0.49 - 1 | 7 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，7 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.49 - 1，7 个样本

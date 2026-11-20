---
name: image_to_image_upscale_lora_sampler_25
type: Image To Image
frequency: 7
level: moderate
coverage: 0.872
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json, 图片生成/图生图/打光参考图一到图二+图片编辑+打光+氛围感+高清放大+全节点注释_2056218566550147074.json, 平台全量/Qwen-Edit-2509-光线迁移_2055572848839798786.json, 平台全量/千问丰胸Qwen2511_2004207069454626817.json, 平台全量/打光_2017990297606688769.json, 平台全量/电商模特多镜头多视角生图工作流_1999306029613674497.json, 视频生成/图生视频/Qwen-Edit-2509-光线迁移 (1)_2058721719896076290.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json、图片生成/图生图/打光参考图一到图二+图片编辑+打光+氛围感+高清放大+全节点注释_2056218566550147074.json、平台全量/Qwen-Edit-2509-光线迁移_2055572848839798786.json、平台全量/千问丰胸Qwen2511_2004207069454626817.json、平台全量/打光_2017990297606688769.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `ConstrainImage|pysssss` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Int` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `RepeatLatentBatch` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有
- `easy imageSize` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 7 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足

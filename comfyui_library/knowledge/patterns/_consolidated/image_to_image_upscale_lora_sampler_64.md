---
name: image_to_image_upscale_lora_sampler_64
type: Image To Image
frequency: 3
level: strong
coverage: 0.788
common_nodes: [CLIPLoader, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json, 图片生成/图生图/打光参考图一到图二+图片编辑+打光+氛围感+高清放大+全节点注释_2056218566550147074.json, 视频生成/图生视频/Qwen-Edit-2509-光线迁移 (1)_2058721719896076290.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json、图片生成/图生图/打光参考图一到图二+图片编辑+打光+氛围感+高清放大+全节点注释_2056218566550147074.json、视频生成/图生视频/Qwen-Edit-2509-光线迁移 (1)_2058721719896076290.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleBy`
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
- `CFGNorm` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

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
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_upscale_sampler_clip_24
type: Image To Image
frequency: 5
level: weak
coverage: 0.8476
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-Image 智能高清修复与放大工作流_2036626914529513473.json, 图片生成/图生图/千问2512图生图洗图+SeedVR2高清工作流_2020867500254175234.json, 图片生成/图生图/千问2512洗图+SeedVR2高清放大工作流_2069347143063789569.json, 图片生成/图生图/图生图洗图修复+SeedVR2高清工作流_2050168318803365889.json, 图片生成/图生图/洗图去ai+放大_1998033674337681409.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/z-Image 智能高清修复与放大工作流_2036626914529513473.json、图片生成/图生图/千问2512图生图洗图+SeedVR2高清工作流_2020867500254175234.json、图片生成/图生图/千问2512洗图+SeedVR2高清放大工作流_2069347143063789569.json、图片生成/图生图/图生图洗图修复+SeedVR2高清工作流_2050168318803365889.json、图片生成/图生图/洗图去ai+放大_1998033674337681409.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ModelSamplingAuraFlow` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `RepeatLatentBatch` —— 1/5 个有
- `ShowAnything|Mie` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 30 | 5 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 33% |
| 采样算法 | res_multistep | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.5 | 0.27 - 0.88 | 5 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 30，5 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 res_multistep，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.27 - 0.88，5 个样本

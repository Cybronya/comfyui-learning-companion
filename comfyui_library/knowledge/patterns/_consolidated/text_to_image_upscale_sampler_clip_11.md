---
name: text_to_image_upscale_sampler_clip_11
type: Text To Image
frequency: 6
level: weak
coverage: 0.899333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json, 图片生成/文生图/AA--超真实Super Zimage文生图+超清放大_2025977545518223361.json, 图片生成/文生图/Z-image文生图+直逼真实摄影+最新seedvr2高清放大工作流_1994801677821730818.json, 图片生成/文生图/啊癫 krea2 人物多角度4视图_2091908917856129025.json, 图片生成/文生图/啊癫z-image 角色资产四视图_2091918692912287745.json, 图片生成/文生图/自动提示词巨物视觉文生图 Krea2 海报风格化制作_2094262430330343425.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json、图片生成/文生图/AA--超真实Super Zimage文生图+超清放大_2025977545518223361.json、图片生成/文生图/Z-image文生图+直逼真实摄影+最新seedvr2高清放大工作流_1994801677821730818.json、图片生成/文生图/啊癫 krea2 人物多角度4视图_2091908917856129025.json、图片生成/文生图/啊癫z-image 角色资产四视图_2091918692912287745.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `llama_cpp_instruct_adv` —— 3/6 个有
- `llama_cpp_model_loader` —— 3/6 个有
- `llama_cpp_parameters` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `Int` —— 2/6 个有
- `JjkText` —— 1/6 个有
- `SaveImagePlus` —— 1/6 个有
- `TTResolutionSelector` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy promptLine` —— 1/6 个有
- `solarL_SaveImagesToZip` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 80 - 1920 | 6 | 40% |
| 高度 | 1308 | 80 - 1920 | 6 | 41% |
| 采样步数 | 8 | 4 - 15 | 6 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 18% |
| 采样算法 | euler | - | 6 | 33% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 80 - 1920，6 个样本，取值分散，一致性仅 40%
- 高度 中位数 1308，观测区间 80 - 1920，6 个样本，取值分散，一致性仅 41%
- 采样步数 中位数 8，观测区间 4 - 15，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足

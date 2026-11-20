---
name: text_to_image_sampler_clip_unet_121
type: Text To Image
frequency: 6
level: weak
coverage: 0.818667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-巨物_2080320653038804994.json, 图片生成/文生图/Krea2-文生图全套工作流_2070287516590235649.json, 图片生成/文生图/Krea2-法天象地_2080277177148469249.json, 图片生成/文生图/Krea2-风情万种+魔鬼身材极简工作流_2078747709145698306.json, 图片生成/文生图/boogu文生图全套工作流_2070307243643465730.json, "图片生成/文生图/z-image,krea2,boogu横向对比评测_2070143176618364929.json"]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_121

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea2-巨物_2080320653038804994.json、图片生成/文生图/Krea2-文生图全套工作流_2070287516590235649.json、图片生成/文生图/Krea2-法天象地_2080277177148469249.json、图片生成/文生图/Krea2-风情万种+魔鬼身材极简工作流_2078747709145698306.json、图片生成/文生图/boogu文生图全套工作流_2070307243643465730.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `MuyeTextEditOutput` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `SeedVR2LoadDiTModel` —— 5/6 个有
- `SeedVR2LoadVAEModel` —— 5/6 个有
- `SeedVR2VideoUpscaler` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `llama_cpp_parameters` —— 5/6 个有
- `Any Switch (rgthree)` —— 3/6 个有
- `CompressImages` —— 3/6 个有
- `Getter` —— 3/6 个有
- `GoohaiUniversalSlider` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `Lora Loader Stack (rgthree)` —— 3/6 个有
- `Setter` —— 3/6 个有
- `easy promptList` —— 3/6 个有
- `CR Prompt Text` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 40 | 6 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | er_sde | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1052 | 1024 - 1920 | 6 | 73% |
| 高度 | 1308 | 1024 - 1920 | 6 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 40，6 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 er_sde，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 1024 - 1920，6 个样本
- 高度 中位数 1308，观测区间 1024 - 1920，6 个样本
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足

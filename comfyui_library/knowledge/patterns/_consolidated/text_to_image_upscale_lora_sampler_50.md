---
name: text_to_image_upscale_lora_sampler_50
type: Text To Image
frequency: 5
level: weak
coverage: 0.8086
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FastFilmGrain, Image Comparer (rgthree), ImageCASharpening+, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PhotoShakeNode, PreviewAny, PreviewImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowAnything|Mie, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 角色资产+胶片颗粒+SEEDVR2放大_2112375027357282305.json, 图片生成/文生图/krea2全能角色资产制作｜动漫写实文生图一站搞定_2107647533790089217.json, 图片生成/文生图/krea2全能角色资产制作｜动漫写实文生图一站搞定_2111862337148899330.json, 图片生成/文生图/全能角色资产制作Krea2工作流，动漫角色文生图写实风格处理工具_2107888627882745857.json, 图片生成/文生图/全能角色资产制作【krea2】_2107465584882569218.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/krea2 角色资产+胶片颗粒+SEEDVR2放大_2112375027357282305.json、图片生成/文生图/krea2全能角色资产制作｜动漫写实文生图一站搞定_2107647533790089217.json、图片生成/文生图/krea2全能角色资产制作｜动漫写实文生图一站搞定_2111862337148899330.json、图片生成/文生图/全能角色资产制作Krea2工作流，动漫角色文生图写实风格处理工具_2107888627882745857.json、图片生成/文生图/全能角色资产制作【krea2】_2107465584882569218.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FastFilmGrain`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PhotoShakeNode`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/5 个有
- `solarL_SaveImagesToZip` —— 3/5 个有
- `孤海注释` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 45% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 1080 | 5 | 0% |
| 高度 | 80 | 80 - 1920 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，5 个样本，取值分散，一致性仅 0%
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足

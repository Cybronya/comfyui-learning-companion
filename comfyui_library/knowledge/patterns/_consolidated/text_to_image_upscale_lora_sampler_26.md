---
name: text_to_image_upscale_lora_sampler_26
type: Text To Image
frequency: 8
level: weak
coverage: 0.80525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/开源角色资产制作工作流1【krea2+kook大佬真实幻想lora+SeedVR2放大+自动提示词_2113046772636536834.json, 图片生成/文生图/MOSS-Prompt短剧角色定妆照生成器，主角配角形象设定一步出图_2114476619871113217.json, 图片生成/文生图/MOSS一键人物三视图生成工作流，输入单图快速出全身多角度设定_2114445738783633409.json, 图片生成/文生图/krea2 角色资产+胶片颗粒+SEEDVR2放大_2112375027357282305.json, 图片生成/文生图/krea2全能角色资产制作｜动漫写实文生图一站搞定_2107647533790089217.json, 图片生成/文生图/krea2全能角色资产制作｜动漫写实文生图一站搞定_2111862337148899330.json, 图片生成/文生图/全能角色资产制作Krea2工作流，动漫角色文生图写实风格处理工具_2107888627882745857.json, 图片生成/文生图/全能角色资产制作【krea2】_2107465584882569218.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/开源角色资产制作工作流1【krea2+kook大佬真实幻想lora+SeedVR2放大+自动提示词_2113046772636536834.json、图片生成/文生图/MOSS-Prompt短剧角色定妆照生成器，主角配角形象设定一步出图_2114476619871113217.json、图片生成/文生图/MOSS一键人物三视图生成工作流，输入单图快速出全身多角度设定_2114445738783633409.json、图片生成/文生图/krea2 角色资产+胶片颗粒+SEEDVR2放大_2112375027357282305.json、图片生成/文生图/krea2全能角色资产制作｜动漫写实文生图一站搞定_2107647533790089217.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `llama_cpp_instruct_adv` —— 7/8 个有
- `llama_cpp_model_loader` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `FastFilmGrain` —— 6/8 个有
- `ImageCASharpening+` —— 6/8 个有
- `PhotoShakeNode` —— 6/8 个有
- `ShowAnything|Mie` —— 6/8 个有
- `llama_cpp_parameters` —— 6/8 个有
- `JjkText` —— 5/8 个有
- `solarL_SaveImagesToZip` —— 5/8 个有
- `孤海注释` —— 5/8 个有
- `EmptyFlux2LatentImage` —— 2/8 个有
- `INTConstant` —— 2/8 个有
- `SkipLayerGuidanceDiTSimple` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `TextEncodeQwenImage21` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 47% |
| 采样算法 | er_sde | - | 8 | 62% |
| 调度器 | beta | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 1080 | 8 | 0% |
| 高度 | 80 | 80 - 1920 | 8 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 er_sde，8 个样本，一致性 62%
- 调度器 最常用 beta，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，8 个样本，取值分散，一致性仅 0%
- 高发问题（12/8 个样本）：Steps较低可能导致细节不足

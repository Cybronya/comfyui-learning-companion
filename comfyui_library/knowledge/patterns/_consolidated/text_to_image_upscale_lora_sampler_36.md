---
name: text_to_image_upscale_lora_sampler_36
type: Text To Image
frequency: 7
level: weak
coverage: 0.830429
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), INTConstant, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超美资产设计_2114188619610152962.json, 图片生成/文生图/Moss一键人物三视图_2113674193341607938.json, 图片生成/文生图/Moss一键人物三视图工作流｜文生图直出多角度人设图_2114279345836613634.json, 图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json, 图片生成/文生图/Qwen Image 2.1角色设计参考表，四视图多角度角色一致性文生图_2102832066093215745.json, 图片生成/文生图/超美资产设计~~~_2110392866790002690.json, 视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/超美资产设计_2114188619610152962.json、图片生成/文生图/Moss一键人物三视图_2113674193341607938.json、图片生成/文生图/Moss一键人物三视图工作流｜文生图直出多角度人设图_2114279345836613634.json、图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json、图片生成/文生图/Qwen Image 2.1角色设计参考表，四视图多角度角色一致性文生图_2102832066093215745.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `ComfySwitchNode` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有
- `Anything Everywhere3` —— 3/7 个有
- `LayerUtility: TextJoin` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `QwenImage21Cache` —— 3/7 个有
- `TextGenerateLTX2Prompt` —— 3/7 个有
- `easy setNode` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `忽略多组孤海` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `EmptyFlux2LatentImage` —— 2/7 个有
- `EmptyImage` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `SkipLayerGuidanceDiTSimple` —— 2/7 个有
- `QwenPERewriteT8` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 7 | 3% |
| 高度 | 80 | 80 - 1920 | 7 | 0% |
| 采样步数 | 4 | 4 - 25 | 7 | 13% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 42% |
| 采样算法 | er_sde | - | 7 | 57% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，7 个样本，取值分散，一致性仅 3%
- 高度 中位数 80，观测区间 80 - 1920，7 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 25，7 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，7 个样本，一致性 57%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

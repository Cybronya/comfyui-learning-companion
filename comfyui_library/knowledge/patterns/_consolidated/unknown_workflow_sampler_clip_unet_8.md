---
name: unknown_workflow_sampler_clip_unet_8
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.849778
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, ImageSharpen, KSamplerAdvanced, KSamplerSelect, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text, LayerUtility: PurgeVRAM V2]
members: [图片生成/图生图/2091343877964910593.json, 图片生成/文生图/Dark Deco 暗黑装饰艺术 三采工作流（无反推模板）_2081052417982033921.json, 图片生成/文生图/Dark Deco 暗黑装饰艺术 全自动三采工作流_2081041992469012482.json, 图片生成/文生图/Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418.json, 图片生成/文生图/Krea2-文生图全模式_2074293554280751106.json, 图片生成/文生图/Krea2-文生图全自动风格迁移_2074293504108490754.json, 图片生成/文生图/Krea2三采-全自动文生图_2075218791964962818.json, 图片生成/文生图/Krea2三采-全自动文生图_2079754578903523329.json, 图片生成/文生图/Krea2三采-全自动文生图_2090250296709705730.json, 图片生成/文生图/Krea2三采-全自动文生图_2090254777090400258.json, 图片生成/文生图/Krea2三采-全自动文生图_2090303123905662977.json, 图片生成/文生图/Krea2三采-全自动文生图全模式_2071985841202880514.json, 图片生成/文生图/Krea2三采-文生图全模式_2089265262427205633.json, 图片生成/文生图/Krea2三采文生图_2076913794516869122.json, 图片生成/文生图/Krea2三采流-全自动文生图全模式_2070098937662496769.json, 图片生成/文生图/Z Image Air 空灵感 8K 直出_2075064355628081154.json, 图片生成/文生图/Z Image Air 空灵感 8K 直出_2076658759031681026.json, 图片生成/文生图/Z Image 极致人体文生图 Extreme Asthetics Text to Image_2075065299652669442.json, 图片生成/文生图/Z+Image+Air+空灵感+8K+直出_2080464179739324418.json, 图片生成/文生图/Z+Image+Air+空灵感_2081903340920852482.json, 图片生成/文生图/Z-image-base-邪修双采+高清放大_2016379330103873538.json, 图片生成/文生图/Z-image-base-邪修双采+高清放大_2018103457047126018.json, 图片生成/文生图/万能图像生成器-直出4K_2055990233665155073.json, 图片生成/文生图/万能图像生成器_2028113030734680066.json, 图片生成/文生图/文生图 角色生成 仙侠 古风 现代（超清）_2100600038656405506.json, 图片生成/文生图/超强自定义角色生成_2024732759662530561.json, 图片生成/文生图/超级双采8k 出图_2073110455563939841.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/2091343877964910593.json、图片生成/文生图/Dark Deco 暗黑装饰艺术 三采工作流（无反推模板）_2081052417982033921.json、图片生成/文生图/Dark Deco 暗黑装饰艺术 全自动三采工作流_2081041992469012482.json、图片生成/文生图/Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418.json、图片生成/文生图/Krea2-文生图全模式_2074293554280751106.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 27 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 23/27 个有
- `PreviewImage` —— 22/27 个有
- `INTConstant` —— 19/27 个有
- `Int` —— 19/27 个有
- `llama_cpp_instruct_adv` —— 17/27 个有
- `llama_cpp_model_loader` —— 17/27 个有
- `LoraLoaderModelOnly` —— 15/27 个有
- `CR Prompt Text` —— 14/27 个有
- `Image Comparer (rgthree)` —— 14/27 个有
- `PreviewAny` —— 13/27 个有
- `SeedVR2LoadDiTModel` —— 13/27 个有
- `SeedVR2LoadVAEModel` —— 13/27 个有
- `SeedVR2VideoUpscaler` —— 13/27 个有
- `llama_cpp_parameters` —— 13/27 个有
- `Fast Groups Bypasser (rgthree)` —— 10/27 个有
- `ShowText|pysssss` —— 8/27 个有
- `LoadImage` —— 6/27 个有
- `PrimitiveInt` —— 6/27 个有
- `PrimitiveStringMultiline` —— 6/27 个有
- `StringReplace` —— 6/27 个有
- `CR Text` —— 5/27 个有
- `Label (rgthree)` —— 5/27 个有
- `GetNode` —— 3/27 个有
- `SetNode` —— 3/27 个有
- `AILab_QwenVL` —— 2/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/27 个有
- `RH_LLMAPI_Pro_Node` —— 2/27 个有
- `MemoryCleaner` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1536 | 27 | 85% |
| 高度 | 1536 | 1024 - 2584 | 27 | 80% |
| 采样步数 | randomize | - | 27 | 78% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 27 | 100% |
| 采样算法 | 1 | 1 - 2 | 27 | 66% |
| 调度器 | euler | - | 27 | 96% |
| 重绘幅度 | simple | - | 27 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1536，27 个样本，取值集中（一致性 85%）
- 高度 中位数 1536，观测区间 1024 - 2584，27 个样本
- 采样步数 最常用 randomize，27 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，27 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 2，27 个样本
- 调度器 最常用 euler，27 个样本，一致性 96%
- 重绘幅度 最常用 simple，27 个样本，一致性 96%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: PurgeVRAM V2

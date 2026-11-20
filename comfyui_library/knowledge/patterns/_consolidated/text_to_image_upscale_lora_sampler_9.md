---
name: text_to_image_upscale_lora_sampler_9
type: Text To Image
frequency: 14
level: weak
coverage: 0.877214
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, INTConstant, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewAny, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json, 图片生成/文生图/Krea2-自动提示词巨物视觉文生图_2093609030823538690.json, 图片生成/文生图/Krea2生成角色四视图_2081393034020876290.json, 图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json, 图片生成/文生图/Krea2角色四视图｜文生图角色设定生成_2095127528628379650.json, 图片生成/文生图/Krea大合集-文生图 _ 风格参考 _ 巨物 _ 人物分镜图_2079781209659502594.json, 图片生成/文生图/Krea大合集-文生图 _ 风格参考 _ 巨物 _ 人物分镜图_2080522767677612034.json, 图片生成/文生图/Krea大合集-文生图 _ 风格参考 _ 巨物 _ 人物分镜图_2081553250591006721.json, 图片生成/文生图/Krea大合集-文生图-风格参考-巨物-人物分镜图_2089695358371848193.json, 图片生成/文生图/Krea大合集-文生图_风格参考_巨物_人物分镜图_2087404155089543170.json, 图片生成/文生图/Krea大合集：文生图  风格参考  巨物  人物分镜图_2079881543497117698.json, 图片生成/文生图/Krea文生图 - 风格参考 -巨物 -人物分镜图-大合集_2080098316074971137.json, 图片生成/文生图/自动提示词巨物视觉文生图 Krea2 海报风格化制作_2094262430330343425.json, 图片生成/文生图/角色四视图生成｜Krea2文生图设计表工作流_2095089848884490242.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json、图片生成/文生图/Krea2-自动提示词巨物视觉文生图_2093609030823538690.json、图片生成/文生图/Krea2生成角色四视图_2081393034020876290.json、图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json、图片生成/文生图/Krea2角色四视图｜文生图角色设定生成_2095127528628379650.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 9/14 个有
- `Krea2StyleReference` —— 7/14 个有
- `Krea2StyleTransfer` —— 7/14 个有
- `LoadImage` —— 7/14 个有
- `PrimitiveStringMultiline` —— 4/14 个有
- `孤海注释` —— 4/14 个有
- `Int` —— 3/14 个有
- `JjkText` —— 3/14 个有
- `PDRatioSelector` —— 3/14 个有
- `TTResolutionSelector` —— 3/14 个有
- `ratio_selector` —— 3/14 个有
- `solarL_SaveImagesToZip` —— 3/14 个有
- `ConditioningKrea2Rebalance` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `LazySwitch1way` —— 1/14 个有
- `easy boolean` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 14 | 53% |
| 高度 | 1536 | 80 - 1536 | 14 | 51% |
| 采样步数 | 8 | 4 - 8 | 14 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 14 | 18% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 39/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，14 个样本
- 高度 中位数 1536，观测区间 80 - 1536，14 个样本
- 采样步数 中位数 8，观测区间 4 - 8，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，14 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（39/14 个样本）：Steps较低可能导致细节不足

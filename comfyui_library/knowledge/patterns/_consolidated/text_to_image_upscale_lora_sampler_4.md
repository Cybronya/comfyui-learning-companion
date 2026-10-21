---
name: text_to_image_upscale_lora_sampler_4
type: Text To Image
frequency: 13
level: moderate
coverage: 0.877385
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, INTConstant, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewAny, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json, 图片生成/文生图/Krea2-自动提示词巨物视觉文生图_2093609030823538690.json, 图片生成/文生图/Krea2生成角色四视图_2081393034020876290.json, 图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json, 图片生成/文生图/Krea2角色四视图｜文生图角色设定生成_2095127528628379650.json, 图片生成/文生图/Krea大合集-文生图 _ 风格参考 _ 巨物 _ 人物分镜图_2079781209659502594.json, 图片生成/文生图/Krea大合集-文生图 _ 风格参考 _ 巨物 _ 人物分镜图_2080522767677612034.json, 图片生成/文生图/Krea大合集-文生图 _ 风格参考 _ 巨物 _ 人物分镜图_2081553250591006721.json, 图片生成/文生图/Krea大合集-文生图-风格参考-巨物-人物分镜图_2089695358371848193.json, 图片生成/文生图/Krea大合集-文生图_风格参考_巨物_人物分镜图_2087404155089543170.json, 图片生成/文生图/Krea大合集：文生图  风格参考  巨物  人物分镜图_2079881543497117698.json, 图片生成/文生图/Krea文生图 - 风格参考 -巨物 -人物分镜图-大合集_2080098316074971137.json, 图片生成/文生图/角色四视图生成｜Krea2文生图设计表工作流_2095089848884490242.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea2-文生图-v1.1_2094718098157948930.json、图片生成/文生图/Krea2-自动提示词巨物视觉文生图_2093609030823538690.json、图片生成/文生图/Krea2生成角色四视图_2081393034020876290.json、图片生成/文生图/Krea2角色四视图-文生图1.1_2094675007816425474.json、图片生成/文生图/Krea2角色四视图｜文生图角色设定生成_2095127528628379650.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
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
- `CR Prompt Text` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `Krea2StyleReference` —— 7/13 个有
- `Krea2StyleTransfer` —— 7/13 个有
- `LoadImage` —— 7/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `Int` —— 3/13 个有
- `PDRatioSelector` —— 3/13 个有
- `ratio_selector` —— 3/13 个有
- `孤海注释` —— 3/13 个有
- `JjkText` —— 2/13 个有
- `TTResolutionSelector` —— 2/13 个有
- `solarL_SaveImagesToZip` —— 2/13 个有
- `ConditioningKrea2Rebalance` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LazySwitch1way` —— 1/13 个有
- `easy boolean` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 13 | 61% |
| 高度 | 1536 | 80 - 1536 | 13 | 60% |
| 采样步数 | 8 | 4 - 8 | 13 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 13 | 18% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 37/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，13 个样本
- 高度 中位数 1536，观测区间 80 - 1536，13 个样本
- 采样步数 中位数 8，观测区间 4 - 8，13 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（37/13 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_303
type: Text To Image
frequency: 6
level: strong
coverage: 0.653833
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, DapaoImagePadDirectionNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511 扩图工作流｜画面边界自由延伸_2112436437365903362.json, 图片生成/图生图/Qwen 2511百分比可控扩图，画面精准延展局部重绘不崩_2112647034019864578.json, 图片生成/图生图/Qwen Image 2.1按百分比可控扩图 精准延展画布一键放大_2104685153539936257.json, 图片生成/图生图/Qwen-Image-2.1按百分比可控扩图｜精准延展画布局部重绘，一键放大画布_2104543456440967169.json, 图片生成/图生图/Qwen-Image-2.1百分比可控扩图，画布精准延展一键放大_2112266614245773314.json, 图片生成/图生图/Qwen-Image-2.1百分比可控扩图｜精准延展画布保留构图｜一键放大出全景_2112123239035133954.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_303

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen 2511 扩图工作流｜画面边界自由延伸_2112436437365903362.json、图片生成/图生图/Qwen 2511百分比可控扩图，画面精准延展局部重绘不崩_2112647034019864578.json、图片生成/图生图/Qwen Image 2.1按百分比可控扩图 精准延展画布一键放大_2104685153539936257.json、图片生成/图生图/Qwen-Image-2.1按百分比可控扩图｜精准延展画布局部重绘，一键放大画布_2104543456440967169.json、图片生成/图生图/Qwen-Image-2.1百分比可控扩图，画布精准延展一键放大_2112266614245773314.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `DapaoImagePadDirectionNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 5/6 个有
- `SeedVR2LoadVAEModel` —— 5/6 个有
- `SeedVR2VideoUpscaler` —— 5/6 个有
- `QwenImage21Cache` —— 4/6 个有
- `RHHiddenNodes` —— 4/6 个有
- `TextEncodeQwenImage21` —— 4/6 个有
- `TextGenerateLTX2Prompt` —— 4/6 个有
- `easy imageSizeByLongerSide` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `CFGNorm` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足

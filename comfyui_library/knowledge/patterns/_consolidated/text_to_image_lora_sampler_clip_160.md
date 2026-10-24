---
name: text_to_image_lora_sampler_clip_160
type: Text To Image
frequency: 10
level: strong
coverage: 0.8921
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1替换工作流_2109602458845667330.json, 图片生成/图生图/Qwen image2.1最佳换头换脸 人物面部精准替换_2104627780217561090.json, 图片生成/图生图/Qwen-Image-2.1一键抠图，产品换背景透明底直出_2111571619721338881.json, 图片生成/图生图/Qwen-Image-2.1一键抠图｜电商产品照透明背景自动生成_2105114072894238722.json, 图片生成/图生图/Qwen-image2.1万能局部重绘｜图生图精准修改神器_2108390020116729858.json, 图片生成/图生图/Qwen-image2.1万能局部重绘｜细节修补改图不求人_2111143256166846465.json, 图片生成/图生图/Qwen-image2.1图像高清修复，老图翻新细节重建_2112296348044316674.json, 图片生成/图生图/Qwen-image2.1最佳换头换脸｜图生图精准换脸不崩脸_2104521060145258498.json, 图片生成/图生图/Qwen-image2.1服装迁移，图生图款式面料高还原_2112294809196126209.json, 图片生成/图生图/Qwen-image2.1终极局部重绘，接缝色差完美解决图生图_2112669048118013953.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_160

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1替换工作流_2109602458845667330.json、图片生成/图生图/Qwen image2.1最佳换头换脸 人物面部精准替换_2104627780217561090.json、图片生成/图生图/Qwen-Image-2.1一键抠图，产品换背景透明底直出_2111571619721338881.json、图片生成/图生图/Qwen-Image-2.1一键抠图｜电商产品照透明背景自动生成_2105114072894238722.json、图片生成/图生图/Qwen-image2.1万能局部重绘｜图生图精准修改神器_2108390020116729858.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `PreviewImage` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `InpaintModelConditioning` —— 3/10 个有
- `Mask Fill Holes` —— 3/10 个有
- `Int` —— 2/10 个有
- `QwenImage21Cache` —— 2/10 个有
- `ColorMatchV2` —— 1/10 个有
- `DapaoImagePadDirectionNode` —— 1/10 个有
- `InpaintCropImproved` —— 1/10 个有
- `InpaintStitchImproved` —— 1/10 个有
- `KSamplerSelect` —— 1/10 个有
- `ManualSigmas` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `SamplerCustom` —— 1/10 个有
- `YYZZipImageSave` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

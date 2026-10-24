---
name: text_to_image_upscale_lora_sampler_64
type: Text To Image
frequency: 4
level: strong
coverage: 0.85625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SeedVR2 高清修复放大｜精修老片画质复活_2112485526564597762.json, 图片生成/图生图/seedvr2图像高清放大｜图生图画质增强一键直出_2091296292063506433.json, 图片生成/图生图/seedvr2图像高清放大｜图生图画质增强直出_2091005891771461634.json, 图片生成/图生图/九宫格分镜图切割高清放大图生图处理工作流工具_2101039744347099138.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SeedVR2 高清修复放大｜精修老片画质复活_2112485526564597762.json、图片生成/图生图/seedvr2图像高清放大｜图生图画质增强一键直出_2091296292063506433.json、图片生成/图生图/seedvr2图像高清放大｜图生图画质增强直出_2091005891771461634.json、图片生成/图生图/九宫格分镜图切割高清放大图生图处理工作流工具_2101039744347099138.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/4 个有
- `GuHaiAutoImageSplit` —— 1/4 个有
- `ImpactCompare` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: If ` —— 1/4 个有
- `LayerUtility: Integer` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_video_lora_sampler_174
type: Text To Image
frequency: 3
level: strong
coverage: 0.664333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Bypasser (rgthree), GetImageSizeAndCount, GetNode, ImageScaleToTotalPixels, Int, JjkText, KSampler, LoraLoaderModelOnly, MathExpression_UTK, Mute / Bypass Repeater (rgthree), PreviewImage, RIFE VFI, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/视频高清放大补帧｜视频超分画质提升工作流_2087200008096538626.json, 视频生成/文生视频/SeedVR2视频高清放大补帧 视频超分辨率增强处理_2099570302983430145.json, 视频生成/文生视频/视频高清放大补帧SeedVR2｜高清放大配补帧双修，文生视频成片更丝滑_2100494943390359553.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/视频高清放大补帧｜视频超分画质提升工作流_2087200008096538626.json、视频生成/文生视频/SeedVR2视频高清放大补帧 视频超分辨率增强处理_2099570302983430145.json、视频生成/文生视频/视频高清放大补帧SeedVR2｜高清放大配补帧双修，文生视频成片更丝滑_2100494943390359553.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageScaleToTotalPixels`
- `Int`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MathExpression_UTK`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `RIFE VFI`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

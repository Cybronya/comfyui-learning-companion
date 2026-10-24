---
name: text_to_image_sampler_clip_unet_31
type: Text To Image
frequency: 14
level: strong
coverage: 0.848
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo基础文生图+高清放大_2063174571645296642.json, 图片生成/文生图/Z-image-turbo基础文生图【用于绘世comfyui批量管理系统】_2089190207693344769.json, 图片生成/文生图/Z-image-turbo文生图_2063952781551169537.json, 图片生成/文生图/Z-image真实感文生图急速出图_1993918066069356545.json, 图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070356235764977666.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070398228675252226.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070414848839737345.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070428303873368066.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2078331213101752321.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070353662572060673.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070396975937314818.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070416550108155905.json, 图片生成/文生图/krea2文生图+seedvr2高清放大_2070429404085444609.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo基础文生图+高清放大_2063174571645296642.json、图片生成/文生图/Z-image-turbo基础文生图【用于绘世comfyui批量管理系统】_2089190207693344769.json、图片生成/文生图/Z-image-turbo文生图_2063952781551169537.json、图片生成/文生图/Z-image真实感文生图急速出图_1993918066069356545.json、图片生成/文生图/Zimage-文生图+高清修复_2011971976901955585.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 11/14 个有
- `SeedVR2LoadVAEModel` —— 11/14 个有
- `SeedVR2VideoUpscaler` —— 11/14 个有
- `Image Comparer (rgthree)` —— 9/14 个有
- `PreviewImage` —— 9/14 个有
- `PrimitiveInt` —— 9/14 个有
- `CR Text` —— 8/14 个有
- `ImageScaleBy` —— 1/14 个有
- `ImpactInt` —— 1/14 个有
- `RTXVideoSuperResolution` —— 1/14 个有
- `Resolution` —— 1/14 个有
- `Text` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1080 | 14 | 89% |
| 高度 | 1536 | 1280 - 1920 | 14 | 89% |
| 采样步数 | 8 | 8 - 10 | 14 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 71% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1080，14 个样本，取值集中（一致性 89%）
- 高度 中位数 1536，观测区间 1280 - 1920，14 个样本，取值集中（一致性 89%）
- 采样步数 中位数 8，观测区间 8 - 10，14 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 71%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（12/14 个样本）：Steps较低可能导致细节不足

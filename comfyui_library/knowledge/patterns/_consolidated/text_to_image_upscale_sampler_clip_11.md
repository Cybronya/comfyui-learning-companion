---
name: text_to_image_upscale_sampler_clip_11
type: Text To Image
frequency: 9
level: moderate
coverage: 0.827667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-真人角色4K文生图_2095131210359074818.json, 图片生成/文生图/Krea2_turbo 4K放大_2079597154166988801.json, 图片生成/文生图/Krea2_turbo 4K放大_2080129101544906754.json, 图片生成/文生图/Krea2_turbo_4K放大_2080939525467099137.json, 图片生成/文生图/Krea2_turbo_4K放大_2095797338735468546.json, 图片生成/文生图/Krea2_turbo_4K放大_2096154230204751874.json, 图片生成/文生图/Krea2文生图-天宫中式巨构_2097024511869804546.json, 图片生成/文生图/MOSS Image 文生图（8步加速_50步复杂文字）(带模型和lora下载链接)_2112068613405499394.json, 图片生成/文生图/MOSS Image 文生图｜8步加速+50步复杂文字附模型lora_2112403092594585601.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Krea2-真人角色4K文生图_2095131210359074818.json、图片生成/文生图/Krea2_turbo 4K放大_2079597154166988801.json、图片生成/文生图/Krea2_turbo 4K放大_2080129101544906754.json、图片生成/文生图/Krea2_turbo_4K放大_2080939525467099137.json、图片生成/文生图/Krea2_turbo_4K放大_2095797338735468546.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `TextConcatenate` —— 5/9 个有
- `ImageScaleToTotalPixels` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `Seed (rgthree)` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `QZ_ResolutionPreset` —— 2/9 个有
- `VOSR2ModelLoader` —— 2/9 个有
- `VOSR2Upscale` —— 2/9 个有
- `JjkText` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `solarL_SaveImagesToZip` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 9 | 62% |
| 高度 | 1024 | 80 - 1280 | 9 | 61% |
| 采样步数 | 8 | 4 - 9 | 9 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 22% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，9 个样本
- 高度 中位数 1024，观测区间 80 - 1280，9 个样本
- 采样步数 中位数 8，观测区间 4 - 9，9 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足

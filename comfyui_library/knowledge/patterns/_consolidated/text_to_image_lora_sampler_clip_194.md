---
name: text_to_image_lora_sampler_clip_194
type: Text To Image
frequency: 4
level: strong
coverage: 0.88025
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json, 图片生成/图生图/Qwen Image 2.1生图及编辑工作流，支持12张参考图一致性最强开源方案_2107154350245240833.json, 图片生成/文生图/Qwen 2.1基础工作流i2v t2v，文生视频图生视频双模式入门方案_2103210530956726273.json, 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_194

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json、图片生成/图生图/Qwen Image 2.1生图及编辑工作流，支持12张参考图一致性最强开源方案_2107154350245240833.json、图片生成/文生图/Qwen 2.1基础工作流i2v t2v，文生视频图生视频双模式入门方案_2103210530956726273.json、图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `SaveImageAdvanced` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Change Channel Count` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `QwenPERewriteT8` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `VOSR2ModelLoader` —— 1/4 个有
- `VOSR2Upscale` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足

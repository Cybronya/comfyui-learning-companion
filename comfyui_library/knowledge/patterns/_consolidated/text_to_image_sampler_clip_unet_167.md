---
name: text_to_image_sampler_clip_unet_167
type: Text To Image
frequency: 4
level: weak
coverage: 0.9345
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImpactInt, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Seedance专属三视图！超级角色资产库：简单指令，万象资产_文生图_角色设计_2040049722169233409.json, 图片生成/文生图/Z-image-turbo文生图_2063952781551169537.json, 图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json, 图片生成/文生图/多套文生图横向对比｜Z-Image Krea2 Qwen Klein2谁更强_2112934322469687297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Seedance专属三视图！超级角色资产库：简单指令，万象资产_文生图_角色设计_2040049722169233409.json、图片生成/文生图/Z-image-turbo文生图_2063952781551169537.json、图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json、图片生成/文生图/多套文生图横向对比｜Z-Image Krea2 Qwen Klein2谁更强_2112934322469687297.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactInt`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `PainterFluxImageEdit` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `JjkText` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/4 个有
- `RH_Nano_Banana2_Image2Image` —— 1/4 个有
- `solarL_SaveImagesToZip` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 80 - 864 | 4 | 49% |
| 高度 | 1280 | 80 - 1320 | 4 | 47% |
| 采样步数 | 9.5 | 4 - 10 | 4 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 4 | 19% |
| 采样算法 | res_2s | - | 4 | 25% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 80 - 864，4 个样本，取值分散，一致性仅 49%
- 高度 中位数 1280，观测区间 80 - 1320，4 个样本，取值分散，一致性仅 47%
- 采样步数 中位数 9.5，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 res_2s，4 个样本，一致性 25%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_upscale_sampler_clip_19
type: Text To Image
frequency: 7
level: weak
coverage: 0.885
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2文生图+SeedVR2高清放大_2079590934051901442.json, 图片生成/文生图/Krea2文生图-天宫中式巨构_2097024511869804546.json, 图片生成/文生图/MOSS Image 文生图（8步加速_50步复杂文字）(带模型和lora下载链接)_2112068613405499394.json, 图片生成/文生图/MOSS Image 文生图｜8步加速+50步复杂文字附模型lora_2112403092594585601.json, 图片生成/文生图/中国风玄幻大作｜Krea2玉京仙宫场景文生图_2096621224637063170.json, 图片生成/文生图/玉京仙宫玄幻风场景｜Krea2中国风文生图生成_2096302133913145346.json, 图片生成/文生图/高清放大｜Krea2 lora动漫角色文生图基础工作流_2089832493032763394.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Krea2文生图+SeedVR2高清放大_2079590934051901442.json、图片生成/文生图/Krea2文生图-天宫中式巨构_2097024511869804546.json、图片生成/文生图/MOSS Image 文生图（8步加速_50步复杂文字）(带模型和lora下载链接)_2112068613405499394.json、图片生成/文生图/MOSS Image 文生图｜8步加速+50步复杂文字附模型lora_2112403092594585601.json、图片生成/文生图/中国风玄幻大作｜Krea2玉京仙宫场景文生图_2096621224637063170.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `Seed (rgthree)` —— 5/7 个有
- `JjkText` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `CheckpointLoaderSimple` —— 2/7 个有
- `ResolutionSelector` —— 2/7 个有
- `VOSR2ModelLoader` —— 2/7 个有
- `VOSR2Upscale` —— 2/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `QZ_ResolutionPreset` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 42% |
| 采样算法 | er_sde | - | 7 | 86% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 1024 | 7 | 0% |
| 高度 | 80 | 80 - 1536 | 7 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，7 个样本，取值分散，一致性仅 0%
- 高发问题（12/7 个样本）：Steps较低可能导致细节不足

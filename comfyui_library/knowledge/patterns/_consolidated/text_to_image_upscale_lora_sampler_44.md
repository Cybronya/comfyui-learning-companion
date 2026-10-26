---
name: text_to_image_upscale_lora_sampler_44
type: Text To Image
frequency: 6
level: strong
coverage: 0.909
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyLatentImage, ImageScale, JjkText, KSampler, LoraLoaderModelOnly, PreviewImage, QZ_ResolutionPreset, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMathDual+, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy seed, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105424857071710209.json, 图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105426302470803457.json, 图片生成/文生图/Qwen Image 2.1场景4K文生图，高质量场景生成工作流_2102852270667943937.json, 图片生成/文生图/Qwen-Image-2.1场景4K版｜文生图场景大片轻松出_2105270809030905857.json, 图片生成/文生图/Qwen-Image-2.1场景4K｜文生图高清放大细节拉满_2105269192474841090.json, 图片生成/文生图/Qwen_Image_2.1场景4K文生图，高质量场景生成工作流_2105849610391609345.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105424857071710209.json、图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105426302470803457.json、图片生成/文生图/Qwen Image 2.1场景4K文生图，高质量场景生成工作流_2102852270667943937.json、图片生成/文生图/Qwen-Image-2.1场景4K版｜文生图场景大片轻松出_2105270809030905857.json、图片生成/文生图/Qwen-Image-2.1场景4K｜文生图高清放大细节拉满_2105269192474841090.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `ImageScale`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QZ_ResolutionPreset`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMathDual+`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/6 个有
- `EmptyImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

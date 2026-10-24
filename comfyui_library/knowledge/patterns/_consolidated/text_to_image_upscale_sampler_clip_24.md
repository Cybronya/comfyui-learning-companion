---
name: text_to_image_upscale_sampler_clip_24
type: Text To Image
frequency: 4
level: weak
coverage: 0.90825
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ColorMatchV2, EmptyLatentImage, ExtractBeforeAfter, Image Comparer (rgthree), ImageBatchMulti, ImageScaleToTotalPixelsX, JDCN_StringToList, KSampler, KSamplerSelect, LoadImage, PreviewBridge, PreviewImage, ProcessString, QwenImage21Cache, RandomNoise, ReferenceLatent, ResolutionSelector, SDVN RGBA to RGB, SamplerCustomAdvanced, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAEEncode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy positive, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1万物迁移，几乎可迁移任何产品的商品换背景图生图工具_2103908038183837698.json, 图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json, 图片生成/图生图/qwen-image-2.1-姿态迁移_2103296254561308673.json, 图片生成/图生图/qwen-image-2.1万物迁移｜产品服装任意场景一键换背景_2103694462307364866.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1万物迁移，几乎可迁移任何产品的商品换背景图生图工具_2103908038183837698.json、图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json、图片生成/图生图/qwen-image-2.1-姿态迁移_2103296254561308673.json、图片生成/图生图/qwen-image-2.1万物迁移｜产品服装任意场景一键换背景_2103694462307364866.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `EmptyLatentImage`
- `ExtractBeforeAfter`
- `Image Comparer (rgthree)`
- `ImageBatchMulti`
- `ImageScaleToTotalPixelsX`
- `JDCN_StringToList`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `PreviewBridge`
- `PreviewImage`
- `ProcessString`
- `QwenImage21Cache`
- `RandomNoise`
- `ReferenceLatent`
- `ResolutionSelector`
- `SDVN RGBA to RGB`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy positive`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `BlockifyMask` —— 2/4 个有
- `LayerUtility: ColorImage V2` —— 2/4 个有
- `LayerUtility: ImageBlend` —— 2/4 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 2/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `SDPoseOODLoader` —— 2/4 个有
- `SDPoseOODProcessor` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 4 | 2% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，4 个样本，取值分散，一致性仅 2%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

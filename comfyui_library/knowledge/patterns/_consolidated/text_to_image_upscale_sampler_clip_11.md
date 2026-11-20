---
name: text_to_image_upscale_sampler_clip_11
type: Text To Image
frequency: 9
level: weak
coverage: 0.901444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ColorMatchV2, EmptyLatentImage, ExtractBeforeAfter, ImageScaleToTotalPixelsX, JDCN_StringToList, KSampler, KSamplerSelect, LoadImage, PreviewBridge, PreviewImage, ProcessString, QwenImage21Cache, RandomNoise, ReferenceLatent, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAEEncode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy positive, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1万物迁移，几乎可迁移任何产品的商品换背景图生图工具_2103908038183837698.json, 图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json, 图片生成/图生图/qwen-image-2.1-二次元转真人_2114273703994413058.json, 图片生成/图生图/qwen-image-2.1-二次元转真人_2114518890490458114.json, 图片生成/图生图/qwen-image-2.1-二次元转真人_2115293614724177922.json, 图片生成/图生图/qwen-image-2.1-姿态迁移_2103296254561308673.json, 图片生成/图生图/qwen-image-2.1万物迁移｜产品服装任意场景一键换背景_2103694462307364866.json, 平台全量/qwen-image-2.1-万物迁移_2103416888717045761.json, 平台全量/qwen-image-2.1-二次元转真人_2106208549465583618.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1万物迁移，几乎可迁移任何产品的商品换背景图生图工具_2103908038183837698.json、图片生成/图生图/Qwen Image 2.1姿态迁移工作流，角色一致性图生图姿势参考方案_2103921742514315266.json、图片生成/图生图/qwen-image-2.1-二次元转真人_2114273703994413058.json、图片生成/图生图/qwen-image-2.1-二次元转真人_2114518890490458114.json、图片生成/图生图/qwen-image-2.1-二次元转真人_2115293614724177922.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `EmptyLatentImage`
- `ExtractBeforeAfter`
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
- `BlockifyMask` —— 7/9 个有
- `LayerUtility: ColorImage V2` —— 7/9 个有
- `LayerUtility: ImageBlend` —— 7/9 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 7/9 个有
- `Mask Fill Holes` —— 7/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `ImageBatchMulti` —— 5/9 个有
- `SDVN RGBA to RGB` —— 5/9 个有
- `AIO_Preprocessor` —— 4/9 个有
- `ImageBlend` —— 4/9 个有
- `ImageConcanate` —— 4/9 个有
- `ImageUpscaleWithModel` —— 4/9 个有
- `UpscaleModelLoader` —— 4/9 个有
- `easy imageSizeBySide` —— 4/9 个有
- `JjkText` —— 3/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `solarL_SaveImagesToZip` —— 3/9 个有
- `孤海注释` —— 3/9 个有
- `SDPoseOODLoader` —— 2/9 个有
- `SDPoseOODProcessor` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 25 | 9 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 24% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 80 - 1024 | 9 | 37% |
| 高度 | 1024 | 80 - 1024 | 9 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 25，9 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 37%
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足

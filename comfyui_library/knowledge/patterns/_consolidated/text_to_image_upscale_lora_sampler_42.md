---
name: text_to_image_upscale_lora_sampler_42
type: Text To Image
frequency: 7
level: weak
coverage: 0.874714
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/一句话生成顶级人像大片_2036055062274904066.json, 图片生成/文生图/云信短剧主角-瑶光lora_2086014484270903297.json, 图片生成/文生图/人物资产图_2111020921766109185.json, 图片生成/文生图/人物资产图一键生成 角色设定文生图处理生成工具_2113023431720656897.json, 图片生成/文生图/漫剧海报封面设计（z_image）_2040052372478627842.json, 图片生成/文生图/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json, 图片生成/文生图/短剧最佳拍档画布功能，支持场景角色文生视频_2111550122223038466.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/一句话生成顶级人像大片_2036055062274904066.json、图片生成/文生图/云信短剧主角-瑶光lora_2086014484270903297.json、图片生成/文生图/人物资产图_2111020921766109185.json、图片生成/文生图/人物资产图一键生成 角色设定文生图处理生成工具_2113023431720656897.json、图片生成/文生图/漫剧海报封面设计（z_image）_2040052372478627842.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `JjkText` —— 3/7 个有
- `solarL_SaveImagesToZip` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `FastFilmGrain` —— 2/7 个有
- `LayerColor: BrightnessContrastV2` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有
- `AspectRatio` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 7 | 31% |
| 采样算法 | er_sde | - | 7 | 43% |
| 调度器 | beta | - | 7 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 80 - 1144 | 7 | 24% |
| 高度 | 1472 | 80 - 1920 | 7 | 19% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 er_sde，7 个样本，一致性 43%
- 调度器 最常用 beta，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 80 - 1144，7 个样本，取值分散，一致性仅 24%
- 高度 中位数 1472，观测区间 80 - 1920，7 个样本，取值分散，一致性仅 19%
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足

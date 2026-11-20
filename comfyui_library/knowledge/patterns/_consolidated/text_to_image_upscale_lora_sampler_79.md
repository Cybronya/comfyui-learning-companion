---
name: text_to_image_upscale_lora_sampler_79
type: Text To Image
frequency: 4
level: strong
coverage: 0.8885
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/一句话生成顶级人像大片_2036055062274904066.json, 图片生成/文生图/云信短剧主角-瑶光lora_2086014484270903297.json, 图片生成/文生图/啊癫z-image 角色资产四视图_2091918692912287745.json, 图片生成/文生图/漫剧海报封面设计（z_image）_2040052372478627842.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/一句话生成顶级人像大片_2036055062274904066.json、图片生成/文生图/云信短剧主角-瑶光lora_2086014484270903297.json、图片生成/文生图/啊癫z-image 角色资产四视图_2091918692912287745.json、图片生成/文生图/漫剧海报封面设计（z_image）_2040052372478627842.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
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
- `CR Text` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `FastFilmGrain` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LayerColor: BrightnessContrastV2` —— 2/4 个有
- `AspectRatio` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 50% |
| 调度器 | bong_tangent | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1080 | 1080 - 1144 | 4 | 97% |
| 高度 | 1920 | 1472 - 1920 | 4 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 50%
- 调度器 最常用 bong_tangent，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1144，4 个样本，取值集中（一致性 97%）
- 高度 中位数 1920，观测区间 1472 - 1920，4 个样本，取值集中（一致性 89%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

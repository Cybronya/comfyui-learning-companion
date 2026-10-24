---
name: text_to_image_upscale_lora_sampler_40
type: Text To Image
frequency: 6
level: strong
coverage: 0.872167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/一句话生成顶级人像大片_2036055062274904066.json, 图片生成/文生图/云信短剧主角-瑶光lora_2086014484270903297.json, 图片生成/文生图/人物资产图_2111020921766109185.json, 图片生成/文生图/全能图片B2：生成角色图像三视图工作流_2035677159926276097.json, 图片生成/文生图/啊癫z-image 角色资产四视图_2091918692912287745.json, 图片生成/文生图/漫剧海报封面设计（z_image）_2040052372478627842.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/一句话生成顶级人像大片_2036055062274904066.json、图片生成/文生图/云信短剧主角-瑶光lora_2086014484270903297.json、图片生成/文生图/人物资产图_2111020921766109185.json、图片生成/文生图/全能图片B2：生成角色图像三视图工作流_2035677159926276097.json、图片生成/文生图/啊癫z-image 角色资产四视图_2091918692912287745.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CR Text` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `FastFilmGrain` —— 3/6 个有
- `LayerColor: BrightnessContrastV2` —— 3/6 个有
- `llama_cpp_instruct_adv` —— 3/6 个有
- `llama_cpp_model_loader` —— 3/6 个有
- `llama_cpp_parameters` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `AspectRatio` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_2s | - | 6 | 50% |
| 调度器 | bong_tangent | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 6 | 75% |
| 高度 | 1920 | 1080 - 1920 | 6 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，6 个样本，一致性 50%
- 调度器 最常用 bong_tangent，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，6 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，6 个样本，取值集中（一致性 81%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

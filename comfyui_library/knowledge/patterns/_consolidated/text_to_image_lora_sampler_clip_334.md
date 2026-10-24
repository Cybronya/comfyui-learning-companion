---
name: text_to_image_lora_sampler_clip_334
type: Text To Image
frequency: 5
level: strong
coverage: 0.8226
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), Int, JjkText, KSampler, KuwaharaBlur, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader, easy boolean, easy ifElse, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/通用放大终版改变较大 图片分辨率提升方案_2104996402978975745.json, 图片生成/图生图/去AI感真实感放大 2.0｜Krea 重塑自然美学｜高清放大_2096873297366577154.json, 图片生成/图生图/无损放大海报专用图生图处理生成工作流工具_2102175922328788993.json, 图片生成/图生图/海报专用无损放大｜图生图印刷级清晰｜大尺寸输出不掉链子_2104795629145907201.json, 图片生成/图生图/通用放大终版商业级真实感图生图处理生成工具_2102172784855183362.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_334

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/通用放大终版改变较大 图片分辨率提升方案_2104996402978975745.json、图片生成/图生图/去AI感真实感放大 2.0｜Krea 重塑自然美学｜高清放大_2096873297366577154.json、图片生成/图生图/无损放大海报专用图生图处理生成工作流工具_2102175922328788993.json、图片生成/图生图/海报专用无损放大｜图生图印刷级清晰｜大尺寸输出不掉链子_2104795629145907201.json、图片生成/图生图/通用放大终版商业级真实感图生图处理生成工具_2102172784855183362.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `Int`
- `JjkText`
- `KSampler`
- `KuwaharaBlur`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy boolean`
- `easy ifElse`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 4/5 个有
- `ImageUpscaleWithModel` —— 4/5 个有
- `InvertMask` —— 4/5 个有
- `JoinImageWithAlpha` —— 4/5 个有
- `LayerMask: BiRefNetUltraV2` —— 4/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 4/5 个有
- `Upscale Model Loader` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `ImageResize+` —— 3/5 个有
- `LayerColor: Color of Shadow & Highlight` —— 3/5 个有
- `LayerColor: RGB` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `easy imageColorMatch` —— 3/5 个有
- `DF_Integer` —— 2/5 个有
- `Latent Noise Injection` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `YUAN_TXTConvertAny` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `GroupExecutor` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `UNETLoader_Any` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足

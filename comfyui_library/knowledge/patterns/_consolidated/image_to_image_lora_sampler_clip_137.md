---
name: image_to_image_lora_sampler_clip_137
type: Image To Image
frequency: 3
level: strong
coverage: 0.652
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CM_SDXLResolution, CheckpointLoaderSimple, DownloadAndLoadFlorence2Model, Fast Groups Bypasser (rgthree), Florence2Run, FluxGuidance, Image Comparer (rgthree), ImageScale, KSampler, LayerColor: LUT Apply, LayerFilter: FilmV2, LayerFilter: HDREffects, LayerMask: CreateGradientMask, LayerUtility: ImageBlendAdvance, LoadImage, LoraLoader, MaskToImage, PreviewImage, SaveImage, ShowText|pysssss, Text Multiline, VAEDecode, VAEEncode, easy imageConcat, easy promptConcat, easy seed]
problems: []
missing: []
members: [图片生成/图生图/jojo日本动漫-AI滤镜_1936029144054419458.json, 图片生成/图生图/《JOJO的奇妙冒险》日漫风格｜一键生图系列_1912405716811087873.json, 平台全量/《JOJO》风格海报生成器_1904436075018817537.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_137

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/jojo日本动漫-AI滤镜_1936029144054419458.json、图片生成/图生图/《JOJO的奇妙冒险》日漫风格｜一键生图系列_1912405716811087873.json、平台全量/《JOJO》风格海报生成器_1904436075018817537.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CM_SDXLResolution`
- `CheckpointLoaderSimple`
- `DownloadAndLoadFlorence2Model`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScale`
- `KSampler`
- `LayerColor: LUT Apply`
- `LayerFilter: FilmV2`
- `LayerFilter: HDREffects`
- `LayerMask: CreateGradientMask`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `VAEDecode`
- `VAEEncode`
- `easy imageConcat`
- `easy promptConcat`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| 采样步数 | 36 | 36 - 36 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 36，观测区间 36 - 36，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）

---
name: image_to_image_lora_sampler_clip_119
type: Image To Image
frequency: 4
level: strong
coverage: 0.83
common_nodes: [BasicGuider, BasicScheduler, BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, DeepTranslatorTextNode, DownloadAndLoadSAM2Model, DualCLIPLoader, Florence2ModelLoader, Florence2Run, Florence2toCoordinates, FluxGuidance, Image Comparer (rgthree), ImageCompositeMasked, ImageConcanate, ImageScaleBy, KSampler, KSamplerSelect, LayerMask: MaskGrow, LoadImage, MaskPreview+, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, RandomNoise, ResizeImageMixlab, Sam2Segmentation, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/文生图/万物换背景加速版_1942830610421624833.json, 平台全量/万物换背景加速版-小宣喧_1874478483765415937.json, 平台全量/商品图人物一致性提示词精准换背景_1915063413788049409.json, 平台全量/图片万物皆可换背景加速版_2000540069524107265.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/万物换背景加速版_1942830610421624833.json、平台全量/万物换背景加速版-小宣喧_1874478483765415937.json、平台全量/商品图人物一致性提示词精准换背景_1915063413788049409.json、平台全量/图片万物皆可换背景加速版_2000540069524107265.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `DeepTranslatorTextNode`
- `DownloadAndLoadSAM2Model`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `Florence2toCoordinates`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageScaleBy`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskPreview+`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PreviewImage`
- `RandomNoise`
- `ResizeImageMixlab`
- `Sam2Segmentation`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

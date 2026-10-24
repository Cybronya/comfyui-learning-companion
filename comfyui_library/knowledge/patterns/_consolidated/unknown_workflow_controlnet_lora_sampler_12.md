---
name: unknown_workflow_controlnet_lora_sampler_12
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.86275
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CR Simple Image Compare, ControlNetApplySD3, ControlNetLoader, DepthAnythingV2Preprocessor, DualCLIPLoader, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageScale, Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSamplerSelect, LayerColor: Brightness & Contrast, LayerFilter: FilmV2, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux+ControlNet姿势一致性洗图反推_1946406763995230209.json, 图片生成/图生图/Flux一键生成洗图图生图网红图片洗图工作流_2089679251569201153.json, 图片生成/图生图/Flux洗图 ControlNet_1928825552176627714.json, 图片生成/图生图/Flux洗图图生图网红图片洗图工作流_2089571830314135553.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux+ControlNet姿势一致性洗图反推_1946406763995230209.json、图片生成/图生图/Flux一键生成洗图图生图网红图片洗图工作流_2089679251569201153.json、图片生成/图生图/Flux洗图 ControlNet_1928825552176627714.json、图片生成/图生图/Flux洗图图生图网红图片洗图工作流_2089571830314135553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageScale`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LayerFilter: FilmV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

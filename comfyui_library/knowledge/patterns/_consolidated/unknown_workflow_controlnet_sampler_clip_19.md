---
name: unknown_workflow_controlnet_sampler_clip_19
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.877667
common_nodes: [AIO_Preprocessor, ApplyFluxControlNet, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/一键解锁二次元 你的专属动漫滤镜_1916667244833869826.json, 图片生成/图生图/一键转卡通_1916440283846737922.json, 图片生成/图生图/室内设计毛坯房秒变效果图带lora快速出图Flux版_1899710160435105793.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键解锁二次元 你的专属动漫滤镜_1916667244833869826.json、图片生成/图生图/一键转卡通_1916440283846737922.json、图片生成/图生图/室内设计毛坯房秒变效果图带lora快速出图Flux版_1899710160435105793.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFluxControlNet`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `LoadFluxControlNet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `TeaCache` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）

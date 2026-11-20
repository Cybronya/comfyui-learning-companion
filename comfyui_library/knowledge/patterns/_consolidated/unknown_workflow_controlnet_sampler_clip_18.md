---
name: unknown_workflow_controlnet_sampler_clip_18
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.86975
common_nodes: [AIO_Preprocessor, ApplyFluxControlNet, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/一键解锁二次元 你的专属动漫滤镜_1916667244833869826.json, 图片生成/图生图/一键转卡通_1916440283846737922.json, 图片生成/图生图/室内设计毛坯房秒变效果图带lora快速出图Flux版_1899710160435105793.json, 平台全量/照片转绘豆豆眼简笔画风格_1915592035808509954.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键解锁二次元 你的专属动漫滤镜_1916667244833869826.json、图片生成/图生图/一键转卡通_1916440283846737922.json、图片生成/图生图/室内设计毛坯房秒变效果图带lora快速出图Flux版_1899710160435105793.json、平台全量/照片转绘豆豆眼简笔画风格_1915592035808509954.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFluxControlNet`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `LoadFluxControlNet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelSamplingFlux` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `LayerUtility: TextJoin` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）

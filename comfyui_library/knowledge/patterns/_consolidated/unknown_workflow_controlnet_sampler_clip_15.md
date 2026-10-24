---
name: unknown_workflow_controlnet_sampler_clip_15
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.892667
common_nodes: [AIO_Preprocessor, ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, ControlNetApplySD3, ControlNetLoader, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptySD3LatentImage, Florence2Run, FluxGuidance, ImageScale, KSamplerSelect, LoadImage, ModelSamplingFlux, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/PuLID角色一致性（面部）_1920675244418203649.json, 图片生成/图生图/【面部一致】FLUX PuLID 网红角色面部保持一致性不同姿势生成_1908024842749419521.json, 图片生成/图生图/面部保持一致_1902523531027197954.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/PuLID角色一致性（面部）_1920675244418203649.json、图片生成/图生图/【面部一致】FLUX PuLID 网红角色面部保持一致性不同姿势生成_1908024842749419521.json、图片生成/图生图/面部保持一致_1902523531027197954.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Florence2Run`
- `FluxGuidance`
- `ImageScale`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `FromBasicPipe_v2` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ToBasicPipe` —— 2/3 个有
- `easy imageSplitGrid` —— 2/3 个有
- `easy imagesSplitImage` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.66 | 0.66 - 0.66 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.66，观测区间 0.66 - 0.66，3 个样本，取值集中（一致性 100%）

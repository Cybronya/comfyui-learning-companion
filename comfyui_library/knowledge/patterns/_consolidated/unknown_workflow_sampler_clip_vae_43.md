---
name: unknown_workflow_sampler_clip_vae_43
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9352
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.1-dev洗图工作流，一键生成相似图（防侵权）_2039928937966473218.json, 图片生成/图生图/Flux Redux - generate image variations_1864587893908926465.json, 图片生成/图生图/一键生成相似图（防侵权）_1986087726040698882.json, 图片生成/图生图/通道图 一键直出全模效果图_2035286937296183297.json, 图片生成/图生图/通道图一键直出全模效果图_1890324947364093954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_43

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX.1-dev洗图工作流，一键生成相似图（防侵权）_2039928937966473218.json、图片生成/图生图/Flux Redux - generate image variations_1864587893908926465.json、图片生成/图生图/一键生成相似图（防侵权）_1986087726040698882.json、图片生成/图生图/通道图 一键直出全模效果图_2035286937296183297.json、图片生成/图生图/通道图一键直出全模效果图_1890324947364093954.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 4/5 个有
- `Florence2Run` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `EmptyLatentImage` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageScale` —— 2/5 个有
- `InstructPixToPixConditioning` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RepeatLatentBatch` —— 2/5 个有
- `UltimateSDUpscale` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `easy stylesSelector` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 896 | 3 | 72% |
| 高度 | 512 | 512 - 1152 | 3 | 58% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 896，3 个样本
- 高度 中位数 512，观测区间 512 - 1152，3 个样本

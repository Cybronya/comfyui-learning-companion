---
name: image_to_image_controlnet_upscale_lora_12
type: Image To Image
frequency: 2
level: weak
coverage: 0.8555
common_nodes: [AIO_Preprocessor, ApplyFBCacheOnModel, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ColorMatch, ConditioningZeroOut, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, Fast Groups Muter (rgthree), FluxGuidance, FluxUnionControlNetApply, Get Image Size, Image Comparer (rgthree), ImageConcatMulti, ImageResize+, ImageScaleToTotalPixels, Int, KSampler, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PathchSageAttentionKJ, PreviewImage, RH_LLMAPI_NODE, ReduxAdvanced, SaveImage, SeedVR2, SeedVR2BlockSwap, SetUnionControlNetType, StyleModelLoader, TeaCache, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy compare, easy ifElse, easy imageConcat, easy imageSize, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/室外和室内-素模生成实景展厅效果图工作流-效果很好-已测试_1983711444736909313.json, 图片生成/图生图/建筑+景观+室内AI效果图工作流_1982019743207047169.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/室外和室内-素模生成实景展厅效果图工作流-效果很好-已测试_1983711444736909313.json、图片生成/图生图/建筑+景观+室内AI效果图工作流_1982019743207047169.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFBCacheOnModel`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `FluxUnionControlNetApply`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `ReduxAdvanced`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `TeaCache`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy imageConcat`
- `easy imageSize`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | depth | - | 2 | 100% |
| 采样步数 | 5 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.2 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 最常用 depth，2 个样本，一致性 100%
- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

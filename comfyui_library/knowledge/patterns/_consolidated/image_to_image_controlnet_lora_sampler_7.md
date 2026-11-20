---
name: image_to_image_controlnet_lora_sampler_7
type: Image To Image
frequency: 4
level: strong
coverage: 0.88125
common_nodes: [AIO_Preprocessor, ApplyFBCacheOnModel, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ColorMatch, ConditioningZeroOut, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxUnionControlNetApply, Image Comparer (rgthree), ImageConcatMulti, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PathchSageAttentionKJ, PreviewImage, RH_LLMAPI_NODE, ReduxAdvanced, SaveImage, SetUnionControlNetType, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageConcat, easy imageSize, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/室外和室内-素模生成实景展厅效果图工作流-效果很好-已测试_1983711444736909313.json, 图片生成/图生图/建筑+景观+室内AI效果图工作流_1982019743207047169.json, 平台全量/建筑景观规划室内多合一效果图v2.0_1955473606023286786.json, 平台全量/建筑景观规划室内多合一效果图v3.10_2029018062724276225.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/室外和室内-素模生成实景展厅效果图工作流-效果很好-已测试_1983711444736909313.json、图片生成/图生图/建筑+景观+室内AI效果图工作流_1982019743207047169.json、平台全量/建筑景观规划室内多合一效果图v2.0_1955473606023286786.json、平台全量/建筑景观规划室内多合一效果图v3.10_2029018062724276225.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
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
- `FluxGuidance`
- `FluxUnionControlNetApply`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `ReduxAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageConcat`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `Get Image Size` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerColor: ColorAdapter` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `SeedVR2BlockSwap` —— 2/4 个有
- `TeaCache` —— 2/4 个有
- `UltimateSDUpscale` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `easy compare` —— 2/4 个有
- `easy ifElse` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | depth | - | 4 | 100% |
| 采样步数 | 7.5 | 5 - 10 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | uni_pc | - | 4 | 75% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 0.19 | 0.18 - 0.2 | 4 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 最常用 depth，4 个样本，一致性 100%
- 采样步数 中位数 7.5，观测区间 5 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 0.19，观测区间 0.18 - 0.2，4 个样本，取值集中（一致性 95%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足

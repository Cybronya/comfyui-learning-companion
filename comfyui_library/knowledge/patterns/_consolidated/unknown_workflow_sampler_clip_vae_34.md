---
name: unknown_workflow_sampler_clip_vae_34
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.939
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux超级加速工作流-Nunchaku_1911400407372103681.json, 图片生成/文生图/Nunchaku Flux pulid秒级换脸出图_1925472577286754305.json, 图片生成/文生图/Nunchakuflux文生图极速秒出图带lora_1912452601420677122.json, 图片生成/文生图/Nunchaku加速工作流-文生图_1923752379836264449.json, 图片生成/文生图/Nunchaku双截棍全系工作流运行合集_1932623266177556482.json, 图片生成/文生图/nunchaku0.3.0.dev2新版换脸_1925107417154318337.json, 图片生成/文生图/双截棍0.3-Flux全生态支持_1931572247486771202.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_34

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Flux超级加速工作流-Nunchaku_1911400407372103681.json、图片生成/文生图/Nunchaku Flux pulid秒级换脸出图_1925472577286754305.json、图片生成/文生图/Nunchakuflux文生图极速秒出图带lora_1912452601420677122.json、图片生成/文生图/Nunchaku加速工作流-文生图_1923752379836264449.json、图片生成/文生图/Nunchaku双截棍全系工作流运行合集_1932623266177556482.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxGuidance`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 6/7 个有
- `EmptySD3LatentImage` —— 5/7 个有
- `NunchakuFluxLoraLoader` —— 5/7 个有
- `LoadImage` —— 4/7 个有
- `NunchakuPulidApply` —— 4/7 个有
- `NunchakuPulidLoader` —— 4/7 个有
- `ControlNetApplyAdvanced` —— 3/7 个有
- `ControlNetLoader` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `SetUnionControlNetType` —— 3/7 个有
- `AIO_Preprocessor` —— 2/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `DualCLIPLoader` —— 2/7 个有
- `InpaintModelConditioning` —— 2/7 个有
- `KSampler` —— 2/7 个有
- `CLIPVisionEncode` —— 1/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `EmptyLatentImage` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `ImageAndMaskResizeNode` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `InstructPixToPixConditioning` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `NunchakuTextEncoderLoaderV2` —— 1/7 个有
- `SDXLEmptyLatentSizePicker+` —— 1/7 个有
- `StyleModelApply` —— 1/7 个有
- `StyleModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 512.5 | - | 2 | 0% |
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 高度 中位数 512.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）

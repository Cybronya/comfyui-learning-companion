---
name: unknown_workflow_controlnet_lora_sampler_24
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.871667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, Florence2ModelLoader, Florence2Run, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json, 图片生成/文生图/【阡陌】FLUX Controlnet精准控图工作流_1927245978720698369.json, 平台全量/CG迷-Flux Upscaler老照片修复，高清放大洗图_1927269466948927490.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json、图片生成/文生图/【阡陌】FLUX Controlnet精准控图工作流_1927245978720698369.json、平台全量/CG迷-Flux Upscaler老照片修复，高清放大洗图_1927269466948927490.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCompositeMasked` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `LayerMask: MaskEdgeShrink` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.65 | 0.65 - 1 | 3 | 78% |
| 宽度 | 1200 | - | 1 | 100% |
| 高度 | 1600 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.65，观测区间 0.65 - 1，3 个样本

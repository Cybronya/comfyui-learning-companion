---
name: unknown_workflow_controlnet_lora_sampler_25
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.87
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, Florence2ModelLoader, Florence2Run, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json, 图片生成/文生图/【阡陌】FLUX Controlnet精准控图工作流_1927245978720698369.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux.1 dev 背景高清（噪点去除）_2043925009676115969.json、图片生成/文生图/【阡陌】FLUX Controlnet精准控图工作流_1927245978720698369.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
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
- `AIO_Preprocessor` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `LayerMask: MaskEdgeShrink` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.825 | - | 2 | 79% |
| 宽度 | 1200 | - | 1 | 100% |
| 高度 | 1600 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.825，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

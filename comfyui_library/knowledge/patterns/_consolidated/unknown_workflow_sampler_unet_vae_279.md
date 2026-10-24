---
name: unknown_workflow_sampler_unet_vae_279
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.887
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RHMiniMaxH3DecodeAV, RHMiniMaxH3DirectModelLoader, RHMiniMaxH3DirectTextEncoderLoader, RHMiniMaxH3DirectVAELoader, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3T2VATarget, RHMiniMaxH3T2VATextEncode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 合集 多参视频加速版本  文生视频  首位帧视频_2085757259535175682.json, 视频生成/图生视频/MiniMax H3 图生视频_2084120970457079810.json, 视频生成/图生视频/MiniMax H3开源版  多参 图生视频  文生视频 首尾帧 视频合集_2084290396510838785.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_279

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 合集 多参视频加速版本  文生视频  首位帧视频_2085757259535175682.json、视频生成/图生视频/MiniMax H3 图生视频_2084120970457079810.json、视频生成/图生视频/MiniMax H3开源版  多参 图生视频  文生视频 首尾帧 视频合集_2084290396510838785.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DirectModelLoader`
- `RHMiniMaxH3DirectTextEncoderLoader`
- `RHMiniMaxH3DirectVAELoader`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3T2VATarget`
- `RHMiniMaxH3T2VATextEncode`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `RHMiniMaxH3FL2VAEncode` —— 2/3 个有
- `RHMiniMaxH3FL2VAFirstFrameCondition` —— 2/3 个有
- `RHMiniMaxH3FL2VAModelLoader` —— 2/3 个有
- `RHMiniMaxH3FL2VATarget` —— 2/3 个有
- `RHMiniMaxH3FL2VATextEncoderLoader` —— 2/3 个有
- `RHMiniMaxH3FL2VAVAELoader` —— 2/3 个有
- `JjkText` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxH3BlockCacheT8` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

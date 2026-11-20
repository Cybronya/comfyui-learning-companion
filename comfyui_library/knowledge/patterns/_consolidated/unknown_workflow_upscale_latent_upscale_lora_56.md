---
name: unknown_workflow_upscale_latent_upscale_lora_56
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.874333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/h3-二阶+sigma+latent_2096577454994448385.json, 视频生成/图生视频/minimaxh3-多参+latent二采_2098875416437157889.json, 视频生成/图生视频/【合理动态版】Hybrid_4+5步双采样_2096530913504088066.json, 视频生成/图生视频/【疯了的动态】Dasiwa_4+5步双采样_2096866880698015746.json, 视频生成/图生视频/黄色的大宝剑武打流放大二采_2109571702479998978.json, 视频生成/文生视频/h3-二阶采样（sigma插值+latent放大）_2090487702180417538.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_56

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/h3-二阶+sigma+latent_2096577454994448385.json、视频生成/图生视频/minimaxh3-多参+latent二采_2098875416437157889.json、视频生成/图生视频/【合理动态版】Hybrid_4+5步双采样_2096530913504088066.json、视频生成/图生视频/【疯了的动态】Dasiwa_4+5步双采样_2096866880698015746.json、视频生成/图生视频/黄色的大宝剑武打流放大二采_2109571702479998978.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 5/6 个有
- `SplitSigmas` —— 5/6 个有
- `ExtendIntermediateSigmas` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `CR Text` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `LoraLoaderBypassModelOnly` —— 2/6 个有
- `ManualSigmas` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `SolAttnMiniMax` —— 2/6 个有
- `TextOverlay` —— 2/6 个有
- `BlockSparseAttention` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `MiniMaxH3HybridLoader` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

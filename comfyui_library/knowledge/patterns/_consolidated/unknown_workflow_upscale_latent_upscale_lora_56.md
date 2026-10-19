---
name: unknown_workflow_upscale_latent_upscale_lora_56
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.893
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json, 视频生成/图生视频/iniMax H3 六图可选图生视频｜混合模型 潜空间高清直出_2095018141456879618.json, 视频生成/图生视频/minimaxh3-多参+latent二采_2098875416437157889.json, 视频生成/图生视频/黄色的大宝剑武打流放大二采_2109571702479998978.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_56

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json、视频生成/图生视频/iniMax H3 六图可选图生视频｜混合模型 潜空间高清直出_2095018141456879618.json、视频生成/图生视频/minimaxh3-多参+latent二采_2098875416437157889.json、视频生成/图生视频/黄色的大宝剑武打流放大二采_2109571702479998978.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 3/4 个有
- `MiniMaxH3SigmaShift` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `SplitSigmas` —— 3/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `MiniMaxLowVRAMAttention` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `BlockSparseAttention` —— 1/4 个有
- `CFGGuider` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `VRAM_Debug` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

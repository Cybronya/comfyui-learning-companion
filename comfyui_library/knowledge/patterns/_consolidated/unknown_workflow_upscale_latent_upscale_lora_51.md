---
name: unknown_workflow_upscale_latent_upscale_lora_51
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.759143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3-turbo-I2V_2094678182095052802.json, 视频生成/图生视频/MinimaxH3-turbo-R2V_2096133628672696321.json, 视频生成/图生视频/双彩去油优化版_2094596803365793793.json, 视频生成/图生视频/双彩去油优化版_2105703775204896770.json, 视频生成/图生视频/双彩去油优化版_2106240702928736257.json, 视频生成/文生视频/MiniMax H3 latent放大模型双采加速 高动态不糊 去油腻 修音频 全能工作流_2090423453655588865.json, 视频生成/文生视频/MinimaxH3-turbo-T2V_2094630845184299009.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_51

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3-turbo-I2V_2094678182095052802.json、视频生成/图生视频/MinimaxH3-turbo-R2V_2096133628672696321.json、视频生成/图生视频/双彩去油优化版_2094596803365793793.json、视频生成/图生视频/双彩去油优化版_2105703775204896770.json、视频生成/图生视频/双彩去油优化版_2106240702928736257.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `ExtendIntermediateSigmas` —— 4/7 个有
- `H3LatentUpscaleByJingchen573` —— 4/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `MiniMaxLowVRAMAttention` —— 4/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `SolAttnMiniMax` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `SolAttnPatch` —— 3/7 个有
- `easy mathInt` —— 3/7 个有
- `MiniMaxH3ImageToVideo` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `WujiAudioLoader` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

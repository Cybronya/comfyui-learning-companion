---
name: unknown_workflow_sampler_unet_vae_54
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084195676602331137.json, 视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084745751497895937.json, 视频生成/图生视频/(量化加速版)Minimax多参生视频V1_2084238539549663234.json, 视频生成/图生视频/0812日Minimax H3 ref2va加速工作流_2087422773068128257.json, 视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json, 视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2107413322575470593.json, 视频生成/图生视频/FastVideo-FastH3-8-Step-V2 图生视频_2101581826061062145.json, 视频生成/图生视频/MiniMax-H3-超自然服装细节展示-自动优化提示词-.json, 视频生成/图生视频/minimax_h3变装秀_2097724749970493442.json, 视频生成/图生视频/minimax_h3复刻短视频爆款_2096558185426546690.json, 视频生成/图生视频/超自然超细节-H3的服装展示(singularity)_2101287029765136386.json, 视频生成/文生视频/video_minimax_h3_t2v_i2v_r2v_rv2v_2091314256494022658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_54

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084195676602331137.json、视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084745751497895937.json、视频生成/图生视频/(量化加速版)Minimax多参生视频V1_2084238539549663234.json、视频生成/图生视频/0812日Minimax H3 ref2va加速工作流_2087422773068128257.json、视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/14 个有
- `SaveVideo` —— 12/14 个有
- `ResolutionSelector` —— 11/14 个有
- `MiniMaxH3SigmaShift` —— 10/14 个有
- `ModelAttentionBackend` —— 10/14 个有
- `PrimitiveFloat` —— 10/14 个有
- `PrimitiveStringMultiline` —— 10/14 个有
- `MiniMaxH3ReferenceToVideo` —— 9/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `BlockSparseAttention` —— 6/14 个有
- `MiniMaxH3ImageToVideo` —— 6/14 个有
- `GetImageSize` —— 5/14 个有
- `ImageScaleToTotalPixels` —— 5/14 个有
- `ModelPreviewOverrideKJ` —— 5/14 个有
- `ShowText|pysssss` —— 5/14 个有
- `MiniMaxH3PromptEnhancerT8` —— 4/14 个有
- `easy seed` —— 4/14 个有
- `MiniMaxChunkFeedForward` —— 3/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 2/14 个有
- `HAIGC_SaveImagesToZip` —— 2/14 个有
- `INTConstant` —— 2/14 个有
- `LoraLoaderBypassModelOnly` —— 2/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `VHS_LoadVideo` —— 2/14 个有
- `VHS_VideoCombine` —— 2/14 个有
- `easy int` —— 2/14 个有
- `MiniMaxH3ContextIR` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有
- `easy clearCacheAll` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_118
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.788
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json, 视频生成/文生视频/Minimxa-lightx2v-SLA加速文生图_2091334717189746689.json, 视频生成/文生视频/VividMuse_MiniMax_H3_文生视频_2084269402014437378.json, 视频生成/文生视频/[Minimax H3]9图片+3音频全能参考_2084583737949511681.json, 视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json, 视频生成/文生视频/fastvideo_fasth3_文生视频-9：16口播5秒_2101846484743450626.json, 视频生成/文生视频/fastvideo_fasth3_文生视频_2101835354880962561.json, 视频生成/文生视频/minimax-h3单采-v2_2093197455679643650.json, 视频生成/文生视频/minimax-h3双采_2103278801034760193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_118

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json、视频生成/文生视频/Minimxa-lightx2v-SLA加速文生图_2091334717189746689.json、视频生成/文生视频/VividMuse_MiniMax_H3_文生视频_2084269402014437378.json、视频生成/文生视频/[Minimax H3]9图片+3音频全能参考_2084583737949511681.json、视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 8/9 个有
- `CreateVideo` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `MiniMaxH3ImageToVideo` —— 6/9 个有
- `BlockSparseAttention` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `MiniMaxH3SigmaShift` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `LoadAudio` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/9 个有
- `MiniMaxH3ReferenceToVideo` —— 3/9 个有
- `ModelAttentionBackend` —— 3/9 个有
- `Seed (rgthree)` —— 3/9 个有
- `GetNode` —— 2/9 个有
- `GetVideoComponents` —— 2/9 个有
- `ImageScaleToTotalPixels` —— 2/9 个有
- `LoadVideo` —— 2/9 个有
- `ModelPreviewOverrideKJ` —— 2/9 个有
- `PreviewAudio` —— 2/9 个有
- `ResizeImageMaskNode` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `TrimAudioDuration` —— 2/9 个有
- `ExtendIntermediateSigmas` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `LTXVConcatAVLatent` —— 1/9 个有
- `LTXVSeparateAVLatent` —— 1/9 个有
- `ManualSigmas` —— 1/9 个有
- `MinimaxH3LatentUpscaler3D` —— 1/9 个有
- `SplitSigmas` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

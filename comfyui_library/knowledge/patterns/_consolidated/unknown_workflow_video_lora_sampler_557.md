---
name: unknown_workflow_video_lora_sampler_557
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.937
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, Fast Groups Bypasser (rgthree), ImageResizeKJv2, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ImageToVideo, MiniMaxH3MotionContextSaveLatent, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PlaySound|pysssss, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, VRAM_Debug, easy seed]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3单采全功能-细节_残影修复_视频延长_双重去油_远景优化_2102363502223650817.json, 视频生成/文生视频/MiniMax H3双采全功能-细节_残影修复_双重去油_远景优化_2102377997285289985.json, 视频生成/文生视频/MiniMax H3双采全功能-细节_残影修复_双重去油_远景优化_2102400058300911618.json, 视频生成/文生视频/MiniMax H3长视频生成-文生视频_九宫格_四视图生视频_视频全能编辑_2091485099572420610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_557

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3单采全功能-细节_残影修复_视频延长_双重去油_远景优化_2102363502223650817.json、视频生成/文生视频/MiniMax H3双采全功能-细节_残影修复_双重去油_远景优化_2102377997285289985.json、视频生成/文生视频/MiniMax H3双采全功能-细节_残影修复_双重去油_远景优化_2102400058300911618.json、视频生成/文生视频/MiniMax H3长视频生成-文生视频_九宫格_四视图生视频_视频全能编辑_2091485099572420610.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PlaySound|pysssss`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `H3DistanceAttentionPatcher` —— 3/4 个有
- `H3ExactRecover` —— 3/4 个有
- `H3InjectSchedule` —— 3/4 个有
- `H3JerkHeatmap` —— 3/4 个有
- `H3JerkOracle` —— 3/4 个有
- `H3SigmaRefiner` —— 3/4 个有
- `H3TimeSmear` —— 3/4 个有
- `H3V2VInit` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `easy int` —— 3/4 个有
- `AudioConcat` —— 2/4 个有
- `LTXVConcatAVLatent` —— 2/4 个有
- `LTXVSeparateAVLatent` —— 2/4 个有
- `ManualSigmas` —— 2/4 个有
- `MiniMaxH3MotionContext` —— 2/4 个有
- `MiniMaxH3MotionContextLoadLatent` —— 2/4 个有
- `MiniMaxH3MotionContextTrim` —— 2/4 个有
- `MinimaxH3LatentUpscaler3D` —— 2/4 个有
- `SplitSigmas` —— 2/4 个有
- `VHS_MergeImages` —— 2/4 个有
- `easy float` —— 2/4 个有
- `Display Any (rgthree)` —— 1/4 个有
- `ImageScaleToMaxDimension` —— 1/4 个有
- `SpectrumApplyMiniMaxH3` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

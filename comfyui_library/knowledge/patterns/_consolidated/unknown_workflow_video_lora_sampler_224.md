---
name: unknown_workflow_video_lora_sampler_224
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.406182
common_nodes: [BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MediaLoaderFantastic, MiniMaxH3MultimodalChat, MiniMaxH3ReferenceSplitter, MiniMaxH3SigmaShift, MiniMaxH3UnifiedToVideo, ModelPreviewOverrideKJ, ShowText|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, VRAM_Debug]
problems: []
missing: []
members: [图片生成/文生图/4-MiniMax-H3_全能生视频单采高清工作流V5-RH版_2115430428424368129.json, 图片生成/文生图/4-MiniMax-H3_全能生视频单采高清工作流V5-RH版_2115656033900261377.json, 图片生成/文生图/MiniMax-H3_全能生视频二采高清工作流V5-latent分块-RH版_2115435347223072770.json, 图片生成/文生图/MiniMax-H3_全能生视频二采高清工作流V5-latent分块-RH版_2115660624440152065.json, 视频生成/文生视频/4-MiniMax-H3_全能生视频单采高清工作流V5-RH版_2116338324335063042.json, 视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V4-latent分块二采_2087412509618823169.json, 视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V5-latent分块二采_2113454316114759682.json, 视频生成/文生视频/4-MiniMaxh-H3-全能生视频工作流-V5-单采2K直出-RH版_2113465285872275458.json, 视频生成/文生视频/MiniMax-H3_全能生视频二采高清工作流V5-latent分块-RH版_2116322855985172482.json, 视频生成/视频生视频/4-MiniMax-H3 全能生视频单采高清工作流V5-RH版_2098811422074556417.json, 视频生成/视频生视频/MiniMax-H3 全能生视频二采高清工作流V5-latent分块-RH版_2087412509618823169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_224

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/4-MiniMax-H3_全能生视频单采高清工作流V5-RH版_2115430428424368129.json、图片生成/文生图/4-MiniMax-H3_全能生视频单采高清工作流V5-RH版_2115656033900261377.json、图片生成/文生图/MiniMax-H3_全能生视频二采高清工作流V5-latent分块-RH版_2115435347223072770.json、图片生成/文生图/MiniMax-H3_全能生视频二采高清工作流V5-latent分块-RH版_2115660624440152065.json、视频生成/文生视频/4-MiniMax-H3_全能生视频单采高清工作流V5-RH版_2116338324335063042.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MediaLoaderFantastic`
- `MiniMaxH3MultimodalChat`
- `MiniMaxH3ReferenceSplitter`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3UnifiedToVideo`
- `ModelPreviewOverrideKJ`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `VRAM_Debug`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 10/11 个有
- `ComfyMathExpression` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `MiniMaxH3AudioSelect` —— 10/11 个有
- `RTXVideoFrameGeneration` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `BlockSparseAttention` —— 8/11 个有
- `MiniMaxH3SparkAttentionSM89` —— 8/11 个有
- `ModelAttentionBackend` —— 8/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `BasicGuider` —— 6/11 个有
- `GoohaiUniversalSlider` —— 6/11 个有
- `LTXVConcatAVLatent` —— 6/11 个有
- `LTXVSeparateAVLatent` —— 6/11 个有
- `MiniMaxH3TiledSampler` —— 6/11 个有
- `MinimaxH3LatentUpscaler3D` —— 6/11 个有
- `RandomNoise` —— 6/11 个有
- `SamplerCustomAdvanced` —— 6/11 个有
- `忽略多组孤海` —— 6/11 个有
- `ConditioningZeroOut` —— 5/11 个有
- `ManualSigmas` —— 5/11 个有
- `MiniMaxH3SigmaRefiner` —— 5/11 个有
- `SelfLiftAvatarH3Sampler` —— 5/11 个有
- `MiniMaxChunkFeedForward` —— 4/11 个有
- `EmptyImage` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `ComfySwitchNode` —— 1/11 个有
- `LayerUtility: NumberCalculatorV2` —— 1/11 个有
- `MiniMaxH3AudioLock` —— 1/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_upscale_latent_upscale_lora_42
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.874556
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/H3文生视频Tao 3步lora二采RES4LYF_2100959295356628994.json, 视频生成/文生视频/MiniMax H3 FL2VA｜文生+首尾帧全能视频_2090027189914918914.json, 视频生成/文生视频/MiniMax H3 Ref2VA｜多参考全能视频生成_2090060185078419458.json, 视频生成/文生视频/MiniMax-H3 fl2v单模型二采无编解码放大_2093393143118000129.json, 视频生成/文生视频/Minimax H3 多参生视频潜空间放大二采_2093173371193352193.json, 视频生成/文生视频/Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322.json, 视频生成/文生视频/Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730.json, 视频生成/文生视频/minimax h3综合型工作流第一人称，男友视角_2108015047955013633.json, 视频生成/文生视频/海螺H3-高效4步-脸部护持_2091172705780461570.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_42

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/H3文生视频Tao 3步lora二采RES4LYF_2100959295356628994.json、视频生成/文生视频/MiniMax H3 FL2VA｜文生+首尾帧全能视频_2090027189914918914.json、视频生成/文生视频/MiniMax H3 Ref2VA｜多参考全能视频生成_2090060185078419458.json、视频生成/文生视频/MiniMax-H3 fl2v单模型二采无编解码放大_2093393143118000129.json、视频生成/文生视频/Minimax H3 多参生视频潜空间放大二采_2093173371193352193.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `BasicScheduler` —— 7/9 个有
- `SplitSigmas` —— 7/9 个有
- `ModelAttentionBackend` —— 6/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `ManualSigmas` —— 5/9 个有
- `MiniMaxH3ReferenceToVideo` —— 5/9 个有
- `H3SigmaRefiner` —— 4/9 个有
- `MiniMaxH3ImageToVideo` —— 4/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `Text` —— 3/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `AudioCrop` —— 2/9 个有
- `ClownsharKSampler_Beta` —— 2/9 个有
- `ConditioningZeroOut` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `SeedGenerator` —— 2/9 个有
- `StringFunction|pysssss` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `FloatConstant` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `MiniMaxChunkFeedForward` —— 1/9 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/9 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/9 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `SolAttnMiniMax` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | simple | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | 3 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 simple，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）

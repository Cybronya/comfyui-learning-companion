---
name: unknown_workflow_lora_sampler_unet_8
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.736333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json, 视频生成/文生视频/Minimxa-lightx2v-SLA加速文生图_2091334717189746689.json, 视频生成/文生视频/Minmax H3参考加速工作流_2086695240752263170.json, 视频生成/文生视频/minimax h3综合型工作流第一人称，男友视角_2108015047955013633.json, 视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json, 视频生成/文生视频/人物真实低动态H3+sigma强化+潜空间放大工作流 双采_2096114490512330753.json, 视频生成/文生视频/动漫短剧工作流（一键直出1080P竖屏短剧提示词未自动优化）_2093587306430160898.json, 视频生成/文生视频/啊癫 minimaxh3极速版二采潜空间直接放大（去油版）_2093957991434379265.json, 视频生成/文生视频/收藏级！H3 加速+二采+打斗全能工作流拆解系列05集_2092970619469123586.json, 视频生成/文生视频/海螺H3 sigma强化+潜空间放大+高清人脸工作流_2089624110652551169.json, 视频生成/文生视频/海螺二采直出1080P视频H3 sigma强化+潜空间2倍放大（Remix融合模型去油腻）_2091655065831563265.json, 视频生成/文生视频/（0824）万象AI+海螺二采直出1080P（自动提示词）_2091672393700962305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/Minimax_文生视频_8步加速_2077975666892558338.json、视频生成/文生视频/Minimxa-lightx2v-SLA加速文生图_2091334717189746689.json、视频生成/文生视频/Minmax H3参考加速工作流_2086695240752263170.json、视频生成/文生视频/minimax h3综合型工作流第一人称，男友视角_2108015047955013633.json、视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `LoadImage` —— 10/12 个有
- `MiniMaxH3SigmaShift` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `LTXVConcatAVLatent` —— 9/12 个有
- `LTXVSeparateAVLatent` —— 9/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/12 个有
- `MiniMaxH3ReferenceToVideo` —— 9/12 个有
- `PrimitiveStringMultiline` —— 9/12 个有
- `SplitSigmas` —— 9/12 个有
- `H3SigmaRefiner` —— 8/12 个有
- `MinimaxH3LatentUpscaler3D` —— 8/12 个有
- `ModelPreviewOverrideKJ` —— 6/12 个有
- `GetNode` —— 5/12 个有
- `SetNode` —— 5/12 个有
- `LoadAudio` —— 4/12 个有
- `MiniMaxH3ImageToVideo` —— 3/12 个有
- `SolAttnMiniMax` —— 3/12 个有
- `VHS_VideoCombine` —— 3/12 个有
- `ManualSigmas` —— 2/12 个有
- `RHLLMChatNode` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `Int` —— 1/12 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/12 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/12 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/12 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/12 个有
- `SigmasPreview` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

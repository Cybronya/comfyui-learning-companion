---
name: unknown_workflow_video_lora_sampler_336
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.631714
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), KepStringLiteral, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxH3GenerationTailLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3PromptEnhancer, PrimitiveFloat, PrimitiveStringMultiline, RTXVideoSuperResolution, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化 I 超分_2086248471761350657.json, 视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化_2087318804178231297.json, 视频生成/文生视频/MiniMax H3 全功能全模态 I 极致优化 I 提示词强化 I 超分_2085552679165714434.json, 视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091435408507891714.json, 视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2089987121053528066.json, 视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091436941274345473.json, 视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2091439098019016706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_336

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化 I 超分_2086248471761350657.json、视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化_2087318804178231297.json、视频生成/文生视频/MiniMax H3 全功能全模态 I 极致优化 I 提示词强化 I 超分_2085552679165714434.json、视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091435408507891714.json、视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2089987121053528066.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `KepStringLiteral`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3GenerationTailLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3PromptEnhancer`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `SeedVR2` —— 6/7 个有
- `SeedVR2BlockSwap` —— 6/7 个有
- `SeedVR2ExtraArgs` —— 6/7 个有
- `UniBlockSwap` —— 6/7 个有
- `VAEDecode` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `VHS_LoadAudioUpload` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `GetImageSize` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `Int` —— 4/7 个有
- `MiniMaxH3ReferenceToVideo` —— 4/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `easy clearCacheAll` —— 4/7 个有
- `ExtendIntermediateSigmas` —— 2/7 个有
- `Float` —— 2/7 个有
- `LTXVConcatAVLatent` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `MiniMaxH3ImageToVideo` —— 2/7 个有
- `MinimaxH3LatentUpscaler3D` —— 2/7 个有
- `ResizeImageMaskNode` —— 2/7 个有
- `SplitSigmas` —— 2/7 个有
- `FlashVSRInitPipe` —— 1/7 个有
- `FlashVSRNodeAdv` —— 1/7 个有
- `MiniMaxH3AVDecodeT8` —— 1/7 个有
- `MiniMaxH3AudioConditioningT8` —— 1/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/7 个有
- `UnloadAllModels` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

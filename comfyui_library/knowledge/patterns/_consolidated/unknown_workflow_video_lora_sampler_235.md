---
name: unknown_workflow_video_lora_sampler_235
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.869
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/Minimax H3 Selflift 数字人_2101246144524406786.json, 数字人/数字人/Minimax H3 Selflift数字人_2099969302521802753.json, 数字人/数字人/Minimax H3 Selflift数字人_2104042672871796737.json, 数字人/数字人/Minimax H3 数字人_2109243580714938369.json, 数字人/数字人/Minimax H3 数字人唱歌MV_2104387863344410625.json, 数字人/数字人/Selflift数字人_2111026652217176065.json, 视频生成/图生视频/AI音乐MV数字人工作流API_2101970168657309697.json, 视频生成/图生视频/AI音乐MV数字人工作流API_2102304757191888898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_235

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Minimax H3 Selflift 数字人_2101246144524406786.json、数字人/数字人/Minimax H3 Selflift数字人_2099969302521802753.json、数字人/数字人/Minimax H3 Selflift数字人_2104042672871796737.json、数字人/数字人/Minimax H3 数字人_2109243580714938369.json、数字人/数字人/Minimax H3 数字人唱歌MV_2104387863344410625.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `SoundFlow_GetLength` —— 7/8 个有
- `TrimAudioDuration` —— 6/8 个有
- `ModelPreviewOverrideKJ` —— 5/8 个有
- `QwenH3PromptLocal` —— 2/8 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Float` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/8 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy positive` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_597
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91275
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/哆哆无限画布-Minimax+H3+Selflift数字人_2113284997036724225.json, 视频生成/图生视频/哆哆无限画布_Minimax_H3_Selflift数字人_唱歌_带音频参考_2113462291067924481.json, 视频生成/文生视频/10Eros Beta5 SelfLift音频数字人精修流_2101538490512142337.json, 视频生成/文生视频/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2100506281638457345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_597

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/哆哆无限画布-Minimax+H3+Selflift数字人_2113284997036724225.json、视频生成/图生视频/哆哆无限画布_Minimax_H3_Selflift数字人_唱歌_带音频参考_2113462291067924481.json、视频生成/文生视频/10Eros Beta5 SelfLift音频数字人精修流_2101538490512142337.json、视频生成/文生视频/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2100506281638457345.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
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
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `Audio Duration (mtb)` —— 2/4 个有
- `BlockSparseAttention` —— 2/4 个有
- `ComfyNumberConvert` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `SoundFlow_GetLength` —— 2/4 个有
- `easy loraStack` —— 2/4 个有
- `easy loraStackApply` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

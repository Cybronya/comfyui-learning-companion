---
name: unknown_workflow_upscale_latent_upscale_sampler_30
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.82
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, H3ExactRecover, H3InjectSchedule, H3JerkOracle, H3ModeSwitch, H3TimeSmear, H3V2VInit, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AddGuide, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3PDD8StepSetupT8Advanced, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, SolAttnMiniMax, SplitSigmasDenoise, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜FL2VA 首尾帧+关键帧时间线控制｜Motion Lab 动作修复_2094644485325156353.json, 视频生成/文生视频/MiniMax H3｜Ref2VA 多参考+关键帧剧情控制｜Motion Lab 动作_2094644471542673409.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜FL2VA 首尾帧+关键帧时间线控制｜Motion Lab 动作修复_2094644485325156353.json、视频生成/文生视频/MiniMax H3｜Ref2VA 多参考+关键帧剧情控制｜Motion Lab 动作_2094644471542673409.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `H3ExactRecover`
- `H3InjectSchedule`
- `H3JerkOracle`
- `H3ModeSwitch`
- `H3TimeSmear`
- `H3V2VInit`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AddGuide`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3PDD8StepSetupT8Advanced`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SolAttnMiniMax`
- `SplitSigmasDenoise`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有
- `Video Slice` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

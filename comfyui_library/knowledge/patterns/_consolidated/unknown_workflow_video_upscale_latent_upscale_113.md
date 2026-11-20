---
name: unknown_workflow_video_upscale_latent_upscale_113
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.746
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, CS-MultiImageLoader, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudioUI, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PreviewAny, PreviewVideoNode, PrimitiveFloat, PrimitiveStringMultiline, RH_LLMAPI_NODE, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3_数字人演唱_2095220444260556801.json, 视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json, 视频生成/文生视频/MiniMax H3_首段视频生成V4（多参考长视频续接）_2094780637541654529.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_113

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/MiniMax H3_数字人演唱_2095220444260556801.json、视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json、视频生成/文生视频/MiniMax H3_首段视频生成V4（多参考长视频续接）_2094780637541654529.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `CS-MultiImageLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudioUI`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PreviewAny`
- `PreviewVideoNode`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `FlashVSRNode` —— 2/3 个有
- `Int` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `LoadVideoUI` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniMaxH3MotionContext` —— 2/3 个有
- `MiniMaxH3MotionContextTrim` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CR Apply LoRA Stack` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/3 个有
- `easy loraStack` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

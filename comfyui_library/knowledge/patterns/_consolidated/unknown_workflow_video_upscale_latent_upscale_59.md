---
name: unknown_workflow_video_upscale_latent_upscale_59
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.7365
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, CS-MultiImageLoader, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudioUI, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PreviewAny, PreviewVideoNode, PrimitiveFloat, PrimitiveStringMultiline, RH_LLMAPI_NODE, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3_数字人演唱_2095220444260556801.json, 视频生成/图生视频/MiniMax H3_多参极简工作流V4.0_剧本分镜生成_2088176083727376386.json, 视频生成/图生视频/MiniMax_H3_多参极简工作流V4.0_剧本分镜生成_2105589051704299521.json, 视频生成/图生视频/MiniMax_H3_多参极简工作流V4.0_剧本分镜生成_2108376288808497154.json, 视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json, 视频生成/文生视频/MiniMax H3_首段视频生成V4（多参考长视频续接）_2094780637541654529.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_59

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/MiniMax H3_数字人演唱_2095220444260556801.json、视频生成/图生视频/MiniMax H3_多参极简工作流V4.0_剧本分镜生成_2088176083727376386.json、视频生成/图生视频/MiniMax_H3_多参极简工作流V4.0_剧本分镜生成_2105589051704299521.json、视频生成/图生视频/MiniMax_H3_多参极简工作流V4.0_剧本分镜生成_2108376288808497154.json、视频生成/文生视频/MiniMax H3_多参极简工作流V3.0（多参考长视频续接）_2094855892327026689.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 5/6 个有
- `FlashVSRNode` —— 5/6 个有
- `Int` —— 5/6 个有
- `KSampler` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LoadVideo` —— 5/6 个有
- `LoadVideoUI` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3MotionContext` —— 5/6 个有
- `MiniMaxH3MotionContextTrim` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `CR Apply LoRA Stack` —— 4/6 个有
- `ManualSigmas` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `PreviewAudio` —— 4/6 个有
- `Switch any [Crystools]` —— 4/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/6 个有
- `easy loraStack` —— 4/6 个有
- `Float` —— 3/6 个有
- `GetImageSize` —— 3/6 个有
- `ImageFromBatch` —— 3/6 个有
- `LiconMSR` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `SolAttnPatch` —— 3/6 个有
- `SplitSigmas` —— 3/6 个有
- `TTResolutionSelector` —— 3/6 个有
- `Text` —— 3/6 个有
- `VHS_MergeImages` —— 3/6 个有
- `忽略多组孤海` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_multistep | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，5 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足

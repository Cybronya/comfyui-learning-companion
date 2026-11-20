---
name: unknown_workflow_video_lora_sampler_475
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.6805
common_nodes: [BasicScheduler, CLIPLoader, CS-MultiImageLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, GetImageSize, ImageFromBatch, Int, KSamplerSelect, LoadAudioUI, LoadVideoUI, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PreviewAny, PreviewImage, PrimitiveFloat, RH_LLMAPI_NODE, ResolutionSelector, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax_H3_初版多参极简二采工作流（最新版已全面使用三采）_2115628641462874114.json, 视频生成/图生视频/MiniMax H3_多参极简工作流V4.0_剧本分镜生成_2088176083727376386.json, 视频生成/图生视频/MiniMax-H3_角色替换工作流_2114001234343583745.json, 视频生成/图生视频/MiniMax_H3_初版多参极简二采工作流最新版已全面使用三采_2115575128414314498.json, 视频生成/图生视频/MiniMax_H3_多参极简工作流V4.0_剧本分镜生成_2105589051704299521.json, 视频生成/图生视频/MiniMax_H3_多参极简工作流V4.0_剧本分镜生成_2108376288808497154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_475

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/MiniMax_H3_初版多参极简二采工作流（最新版已全面使用三采）_2115628641462874114.json、视频生成/图生视频/MiniMax H3_多参极简工作流V4.0_剧本分镜生成_2088176083727376386.json、视频生成/图生视频/MiniMax-H3_角色替换工作流_2114001234343583745.json、视频生成/图生视频/MiniMax_H3_初版多参极简二采工作流最新版已全面使用三采_2115575128414314498.json、视频生成/图生视频/MiniMax_H3_多参极简工作流V4.0_剧本分镜生成_2105589051704299521.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CS-MultiImageLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `GetImageSize`
- `ImageFromBatch`
- `Int`
- `KSamplerSelect`
- `LoadAudioUI`
- `LoadVideoUI`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_LLMAPI_NODE`
- `ResolutionSelector`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `CR Apply LoRA Stack` —— 5/6 个有
- `CR Text` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `FlashVSRNode` —— 5/6 个有
- `Float` —— 5/6 个有
- `KSampler` —— 5/6 个有
- `LTXVConcatAVLatent` —— 5/6 个有
- `LTXVSeparateAVLatent` —— 5/6 个有
- `LiconMSR` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LoadVideo` —— 5/6 个有
- `ManualSigmas` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `MiniMaxH3MotionContext` —— 5/6 个有
- `MiniMaxH3MotionContextTrim` —— 5/6 个有
- `MinimaxH3LatentUpscaler3D` —— 5/6 个有
- `PreviewAudio` —— 5/6 个有
- `PreviewVideoNode` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `RandomNoise` —— 5/6 个有
- `SamplerCustomAdvanced` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `SolAttnPatch` —— 5/6 个有
- `SplitSigmas` —— 5/6 个有
- `Switch any [Crystools]` —— 5/6 个有
- `TTResolutionSelector` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `VHS_MergeImages` —— 5/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/6 个有
- `easy loraStack` —— 5/6 个有
- `BlockSparseAttention` —— 3/6 个有
- `CLIPTextEncode` —— 3/6 个有
- `CheckpointLoaderSimple` —— 3/6 个有
- `DA3Inference` —— 3/6 个有
- `DA3Render` —— 3/6 个有
- `EmptyImage` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `GoohaiUniversalSlider` —— 3/6 个有
- `INTConstant` —— 3/6 个有
- `ImageCompositeMasked` —— 3/6 个有
- `LoadDA3Model` —— 3/6 个有
- `MaskComposite` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `ModelPreviewOverrideKJ` —— 3/6 个有
- `SAM3_TrackPreview` —— 3/6 个有
- `SAM3_TrackToMask` —— 3/6 个有
- `SAM3_VideoTrack` —— 3/6 个有
- `SCAIL2ColoredMask` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `SelfLiftH3Sampler` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `ShowAnything|Mie` —— 3/6 个有
- `SolidMask` —— 3/6 个有
- `VHS_LoadVideoFFmpeg` —— 3/6 个有
- `VHS_VideoInfo` —— 3/6 个有

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
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，5 个样本，取值集中（一致性 100%）
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足

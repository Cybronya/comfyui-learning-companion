---
name: unknown_workflow_sampler_unet_vae_139
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7678
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ChainAssemble, MiniMaxH3ChainContext, MiniMaxH3ChainCurrent, MiniMaxH3ChainLoopEnd, MiniMaxH3ChainLoopStart, MiniMaxH3ChainPlan, MiniMaxH3ChainSegmentSave, MiniMaxH3LoopTrim, MiniMaxH3SigmaShift, PixaromaSizes, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy mergeVideosFromPaths]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 全能参考无限长视频满血+加速_2094642674493116417.json, 视频生成/图生视频/MiniMax H3 全能参考无限长视频满血+加速v2_2094707715150012419.json, 视频生成/图生视频/MiniMax H3 多图参考无限长视频满血+加速_2096191515784732673.json, 视频生成/图生视频/MiniMax H3 首尾帧无限长视频满血+加速_2095862167072493569.json, 视频生成/图生视频/MiniMax H3 首尾帧无限长视频满血+加速_2096076568014704641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_139

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 全能参考无限长视频满血+加速_2094642674493116417.json、视频生成/图生视频/MiniMax H3 全能参考无限长视频满血+加速v2_2094707715150012419.json、视频生成/图生视频/MiniMax H3 多图参考无限长视频满血+加速_2096191515784732673.json、视频生成/图生视频/MiniMax H3 首尾帧无限长视频满血+加速_2095862167072493569.json、视频生成/图生视频/MiniMax H3 首尾帧无限长视频满血+加速_2096076568014704641.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ChainAssemble`
- `MiniMaxH3ChainContext`
- `MiniMaxH3ChainCurrent`
- `MiniMaxH3ChainLoopEnd`
- `MiniMaxH3ChainLoopStart`
- `MiniMaxH3ChainPlan`
- `MiniMaxH3ChainSegmentSave`
- `MiniMaxH3LoopTrim`
- `MiniMaxH3SigmaShift`
- `PixaromaSizes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy mergeVideosFromPaths`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ChainReview` —— 4/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `MiniMaxH3ChainScenePromptEditor` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `SolAttnPatch` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `Int` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `MiniMaxH3ImageToVideo` —— 2/5 个有
- `MiniMaxH3ScheduledPictureReference` —— 2/5 个有
- `MiniMaxH3ScheduledReferenceToVideo` —— 2/5 个有
- `ModelAttentionBackend` —— 2/5 个有
- `PrimitiveBoolean` —— 2/5 个有
- `LoadVideo` —— 1/5 个有
- `MiniMaxH3ChainPlanStudio` —— 1/5 个有
- `MiniMaxH3ChainRichScenePromptEditor` —— 1/5 个有
- `MiniMaxH3ChainRunManager` —— 1/5 个有
- `MiniMaxH3ReferenceToVideo` —— 1/5 个有
- `MiniMaxH3ReferenceVideoPrepare` —— 1/5 个有
- `MiniMaxH3ScheduledAudioReference` —— 1/5 个有
- `MiniMaxH3ScheduledVideoReference` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_295
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.916667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ChainAssemble, MiniMaxH3ChainContext, MiniMaxH3ChainCurrent, MiniMaxH3ChainLoopEnd, MiniMaxH3ChainLoopStart, MiniMaxH3ChainManifestLoad, MiniMaxH3ChainPlan, MiniMaxH3ChainReview, MiniMaxH3ChainScenePromptEditor, MiniMaxH3ChainSegmentSave, MiniMaxH3LoopTrim, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-多参W版长视频-V2.0_2111463571648499714.json, 视频生成/图生视频/MiniMax-H3-无限时长分镜版_2105836805424762881.json, 视频生成/图生视频/MiniMax-H3-无限时长分镜版_2110656252312383490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_295

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-多参W版长视频-V2.0_2111463571648499714.json、视频生成/图生视频/MiniMax-H3-无限时长分镜版_2105836805424762881.json、视频生成/图生视频/MiniMax-H3-无限时长分镜版_2110656252312383490.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
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
- `MiniMaxH3ChainManifestLoad`
- `MiniMaxH3ChainPlan`
- `MiniMaxH3ChainReview`
- `MiniMaxH3ChainScenePromptEditor`
- `MiniMaxH3ChainSegmentSave`
- `MiniMaxH3LoopTrim`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `JoinStringMulti` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `SomethingToString` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxH3ChainPlanModern` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `easy saveText` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

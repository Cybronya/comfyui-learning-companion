---
name: unknown_workflow_sampler_unet_vae_103
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.758
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, KSamplerSelect, PrimitiveBoolean, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Minimax文生视频T2V_2114255990785921025.json, 图片生成/文生图/Minimax文生视频T2V_2115283752321642498.json, 平台全量/FastH3-Omni_2112900011502686210.json, 视频生成/图生视频/4步MiniMax-H3参考图生视频-LynnReal-Omni_2099804283427446785.json, 视频生成/图生视频/LynnReal-FastH3 pose2v动作迁移_2101573571259752450.json, 视频生成/图生视频/LynnReal-Onmi 多参考+首尾帧满血4步加速音视频_2101265947867828226.json, 视频生成/图生视频/MinimaxH3 FastH3 Trim多参考+首尾帧满血8步加速音视频生成_2105942822275866626.json, 视频生成/图生视频/MinimaxH3 singularity2 高动态全能参考+首尾帧满血turbo加速_2114672376171548673.json, 视频生成/图生视频/MinimaxH3_FastH3_Trim多参考+首尾帧满血8步加速音视频生成_2114189677254242305.json, 视频生成/图生视频/MinimaxH3人物替换character swap_2109965862622031874.json, 视频生成/图生视频/Minmax多参考生成视频R2V_2084668436755599362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_103

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Minimax文生视频T2V_2114255990785921025.json、图片生成/文生图/Minimax文生视频T2V_2115283752321642498.json、平台全量/FastH3-Omni_2112900011502686210.json、视频生成/图生视频/4步MiniMax-H3参考图生视频-LynnReal-Omni_2099804283427446785.json、视频生成/图生视频/LynnReal-FastH3 pose2v动作迁移_2101573571259752450.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `MiniMaxH3ReferenceToVideo` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `AnySwitch` —— 7/11 个有
- `Fast Bypasser (rgthree)` —— 7/11 个有
- `MiniMaxH3ImageToVideo` —— 7/11 个有
- `PrimitiveInt` —— 4/11 个有
- `AudioCrop` —— 3/11 个有
- `GetNode` —— 3/11 个有
- `LoadAudio` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `SDVN Any Show` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `easy minimaxH3AudioLock` —— 3/11 个有
- `LoadVideo` —— 2/11 个有
- `MiniMaxH3SaveLatent` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `Bool` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `FastGroupsBypassSwitch` —— 1/11 个有
- `GetVideoComponents` —— 1/11 个有
- `Int` —— 1/11 个有
- `LynnRealAlignedReference` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `QwenH3PromptLocal` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_88
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.813667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json, 视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json, 视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json, 视频生成/文生视频/4步MiniMax-H3文生视频-LynnReal-Omni_2099804217237135361.json, 视频生成/文生视频/8步加速Mini Max H3图生视频_2084136196300697601.json, 视频生成/文生视频/A-3 MiniMax-H3 文生视频 开源版_2084541355501641730.json, 视频生成/文生视频/H3-多功能工作流_2084183787587596289.json, 视频生成/文生视频/H3-最优官流_2088982134630469634.json, 视频生成/文生视频/MINIMAX-H3 sage+sol att双加速低显存全功能工作流_2084920261798879233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_88

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json、视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json、视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json、视频生成/文生视频/4步MiniMax-H3文生视频-LynnReal-Omni_2099804217237135361.json、视频生成/文生视频/8步加速Mini Max H3图生视频_2084136196300697601.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 8/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `MiniMaxH3ImageToVideo` —— 6/9 个有
- `LoadImage` —— 5/9 个有
- `MiniMaxH3ReferenceToVideo` —— 5/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `easy int` —— 2/9 个有
- `ComfyNumberConvert` —— 1/9 个有
- `ManualSigmas` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `SolAttnPatch` —— 1/9 个有
- `UniBlockSwap` —— 1/9 个有
- `UniBlockSwapTE` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

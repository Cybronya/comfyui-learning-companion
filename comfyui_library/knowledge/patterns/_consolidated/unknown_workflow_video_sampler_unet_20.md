---
name: unknown_workflow_video_sampler_unet_20
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.728786
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimaxh3 数字人_2089195997028249601.json, 视频生成/图生视频/minimax全能参考 8步加速_2088816074463735810.json, 视频生成/图生视频/video_minimax_h3_r2v_2084181079887536129.json, 视频生成/图生视频/【低成本01号】海螺H3全能多参音视频生成（9图3视频3音频）开源版_2085685970485202946.json, 视频生成/图生视频/【开源】minimax_h3 参考生视频加速版_2085966231420628993.json, 视频生成/图生视频/【开源】minimax_h3 图生视频加速版_2085932065148719105.json, 视频生成/图生视频/多参考图双音轨视频工作流_2087092408126369794.json, 视频生成/图生视频/老李多参生视频_2104266943242002434.json, 视频生成/文生视频/MINIMAX-H3 多参工作流_2084509251074093057.json, 视频生成/文生视频/MINIMAX-H3多参_2086757864504385537.json, 视频生成/文生视频/最强开源版minimax海螺H3全能参考视频生成加速优化支持9图3视频3音频_2084244979584684034.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图-动态去高躁_2088657311995879425.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2085050902129504257.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2087936662021173250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_20

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/minimaxh3 数字人_2089195997028249601.json、视频生成/图生视频/minimax全能参考 8步加速_2088816074463735810.json、视频生成/图生视频/video_minimax_h3_r2v_2084181079887536129.json、视频生成/图生视频/【低成本01号】海螺H3全能多参音视频生成（9图3视频3音频）开源版_2085685970485202946.json、视频生成/图生视频/【开源】minimax_h3 参考生视频加速版_2085966231420628993.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 13/14 个有
- `PathchSageAttentionKJ` —— 9/14 个有
- `LoadAudio` —— 8/14 个有
- `PrimitiveStringMultiline` —— 8/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `Text` —— 6/14 个有
- `EasyCache` —— 5/14 个有
- `SolAttnPatch` —— 5/14 个有
- `VHS_LoadVideo` —— 5/14 个有
- `MiniMaxH3BlockCacheT8` —— 4/14 个有
- `GetNode` —— 3/14 个有
- `Int` —— 3/14 个有
- `ModelPatchTorchSettings` —— 3/14 个有
- `PainterVRAM` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `TrimAudioDuration` —— 3/14 个有
- `ExtendIntermediateSigmas` —— 1/14 个有
- `H3SigmaRefiner` —— 1/14 个有
- `SaveAudio` —— 1/14 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

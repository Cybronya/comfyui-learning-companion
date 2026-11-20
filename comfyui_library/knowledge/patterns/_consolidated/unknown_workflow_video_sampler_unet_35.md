---
name: unknown_workflow_video_sampler_unet_35
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.899083
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3_多参_单图版注意力再加速_2105908156558823425.json, 视频生成/图生视频/minimax_h3_多参_短剧批量专用（支持90个角色、场景、道具）_2101317527325470722.json, 视频生成/图生视频/minimax_ref_fl_低显存真实感工作流_2097518131697766402.json, 视频生成/图生视频/多参考生视频_2112177352993230849.json, 视频生成/图生视频/（api强化武打）竖屏640p坤坤H3官流lora加速20步_2114244637195071489.json, 视频生成/图生视频/（api）横屏640p坤坤H3官流无lora12步_2110413455923699713.json, 视频生成/图生视频/（api）竖屏608p坤坤H3官流无lora_2108200300300554241.json, 视频生成/图生视频/（api）竖屏768p坤坤H3官流_2108103067618070530.json, 视频生成/文生视频/H3官流全能参考9图1音频1视频_2105563203647393793.json, 视频生成/文生视频/H3官流（mpov版）-不用加速lora_2107126428574773249.json, 视频生成/文生视频/H3官流（最强武戏）_2108377903393239042.json, 视频生成/文生视频/H3官流（终极版）_2104734128657756162.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_35

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/minimax_h3_多参_单图版注意力再加速_2105908156558823425.json、视频生成/图生视频/minimax_h3_多参_短剧批量专用（支持90个角色、场景、道具）_2101317527325470722.json、视频生成/图生视频/minimax_ref_fl_低显存真实感工作流_2097518131697766402.json、视频生成/图生视频/多参考生视频_2112177352993230849.json、视频生成/图生视频/（api强化武打）竖屏640p坤坤H3官流lora加速20步_2114244637195071489.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 11/12 个有
- `MiniMaxH3ReferenceToVideo` —— 10/12 个有
- `ModelPreviewOverrideKJ` —— 10/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `ManualSigmas` —— 9/12 个有
- `BlockSparseAttention` —— 8/12 个有
- `LoadAudio` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `MiniMaxLowVRAMAttention` —— 3/12 个有
- `LayerUtility: PurgeVRAM V2` —— 2/12 个有
- `MiniMaxChunkFeedForward` —— 2/12 个有
- `SolAttnPatch` —— 2/12 个有
- `ExtendIntermediateSigmas` —— 1/12 个有
- `H3SigmaRefiner` —— 1/12 个有
- `MiniMaxH3AudioConditioningT8` —— 1/12 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_lora_sampler_unet_51
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.854583
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/260813001.Minimax-H3多图参考生视频_2088059548048379905.json, 视频生成/图生视频/2图参考生视频minimax_2110625760905089026.json, 视频生成/图生视频/2张参考图_2110029532303552514.json, 视频生成/图生视频/3图参考空白工作流miniimaxh3_2099113484138143745.json, 视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json, 视频生成/图生视频/MiniMax H3 REF2VA-全能参考生视频-(8步加速-768P)-V1_2085290521219649538.json, 视频生成/图生视频/MiniMax H3 多参输入生视频_2085272663802605570.json, 视频生成/图生视频/MiniMax H3+lightx2v 4步加速全能参考工作流2图_2086437276707545089.json, 视频生成/图生视频/h3  4步多图自用_2088590941430046722.json, 视频生成/图生视频/多图参考生成视频_2093669173456105473.json, 视频生成/文生视频/🍲Minimax-H3多模态参考4步加速极限双优版🍲_2086661468988198913.json, 视频生成/文生视频/🍲Minimax-H3提示词自动优化+4步加速极限双优版🍲_2086652281939914753.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_51

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/260813001.Minimax-H3多图参考生视频_2088059548048379905.json、视频生成/图生视频/2图参考生视频minimax_2110625760905089026.json、视频生成/图生视频/2张参考图_2110029532303552514.json、视频生成/图生视频/3图参考空白工作流miniimaxh3_2099113484138143745.json、视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/12 个有
- `ResolutionSelector` —— 11/12 个有
- `PathchSageAttentionKJ` —— 8/12 个有
- `PrimitiveStringMultiline` —— 8/12 个有
- `孤海注释` —— 5/12 个有
- `easy int` —— 4/12 个有
- `Seed (rgthree)` —— 3/12 个有
- `Text` —— 3/12 个有
- `easy convertAnything` —— 3/12 个有
- `LoadAudio` —— 2/12 个有
- `MiniMaxChunkFeedForward` —— 2/12 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `SpectrumSDXL` —— 2/12 个有
- `DapaoH3PromptBoxNode` —— 1/12 个有
- `DapaoH3VideoPromptNode` —— 1/12 个有
- `H3AdaLNLoRAFix` —— 1/12 个有
- `LoadImageFromUrl` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `PrimitiveString` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

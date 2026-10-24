---
name: unknown_workflow_video_lora_sampler_351
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.859667
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3角色替换（单人_指定角色+视频编辑）_2109856895799480322.json, 视频生成/图生视频/MiniMaxH3参考加速版自用_2092230388805619714.json, 视频生成/图生视频/Minimax H3 高动态打斗模型，优化步数，减少等待时间_2098343857598582785.json, 视频生成/图生视频/Minimax H3 高动态打斗模型，更稳更有冲击力！_2096240918440529922.json, 视频生成/图生视频/Minimax 参考图模式_2109199755543924737.json, 视频生成/图生视频/minimaxH3多参考视频工作流pv（备用方案）_2097327651475247106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_351

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3角色替换（单人_指定角色+视频编辑）_2109856895799480322.json、视频生成/图生视频/MiniMaxH3参考加速版自用_2092230388805619714.json、视频生成/图生视频/Minimax H3 高动态打斗模型，优化步数，减少等待时间_2098343857598582785.json、视频生成/图生视频/Minimax H3 高动态打斗模型，更稳更有冲击力！_2096240918440529922.json、视频生成/图生视频/Minimax 参考图模式_2109199755543924737.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `ModelAttentionBackend` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `VHS_LoadVideo` —— 4/6 个有
- `Label (rgthree)` —— 3/6 个有
- `LoadAudio` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `BlockSparseAttention` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `H3SigmaRefiner` —— 1/6 个有
- `ManualSigmas` —— 1/6 个有
- `MiniMaxH3Unified` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SelfLiftH3Sampler` —— 1/6 个有
- `StringMergeNode` —— 1/6 个有
- `VHS_SelectImages` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

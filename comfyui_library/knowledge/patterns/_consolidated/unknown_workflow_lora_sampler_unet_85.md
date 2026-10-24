---
name: unknown_workflow_lora_sampler_unet_85
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.58775
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, SolAttnMiniMax, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/DG_图生视频（一张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094345515814178817.json, 视频生成/图生视频/DG_图生视频（三张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094347086996271105.json, 视频生成/图生视频/DG_图生视频（两张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094341092257914881.json, 视频生成/图生视频/DG_视频编辑（视频+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094349718418710529.json, 视频生成/图生视频/H3 sigma强化+潜空间放大工作流_2089596339163320321.json, 视频生成/图生视频/H3 sigma强化+潜空间放大工作流_2091173937257472002.json, 视频生成/图生视频/H3 sigma强化_2090416810561728514.json, 视频生成/文生视频/DG_文生视频（提示词生视频）（H3 sigma强化+潜空间放大 参考生视频工作流_2094343576493846530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_85

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/DG_图生视频（一张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094345515814178817.json、视频生成/图生视频/DG_图生视频（三张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094347086996271105.json、视频生成/图生视频/DG_图生视频（两张图+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094341092257914881.json、视频生成/图生视频/DG_视频编辑（视频+提示词）（H3 sigma强化+潜空间放大 参考生视频工作流_2094349718418710529.json、视频生成/图生视频/H3 sigma强化+潜空间放大工作流_2089596339163320321.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SolAttnMiniMax`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Getter` —— 5/8 个有
- `ImageConcanate` —— 5/8 个有
- `LoadAudio` —— 5/8 个有
- `MiniMaxH3AVDecodeT8` —— 5/8 个有
- `MinimaxH3LatentUpscaler3D` —— 5/8 个有
- `PreviewAudio` —— 5/8 个有
- `RH_Translator` —— 5/8 个有
- `Setter` —— 5/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `VHS_LoadVideoPath` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `WooshLoadFlow` —— 5/8 个有
- `WooshSample` —— 5/8 个有
- `WooshTextEncode` —— 5/8 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/8 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

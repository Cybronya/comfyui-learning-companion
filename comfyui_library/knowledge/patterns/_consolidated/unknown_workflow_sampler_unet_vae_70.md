---
name: unknown_workflow_sampler_unet_vae_70
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8354
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json, 视频生成/文生视频/MiniMax H3 全模态多参考视频生成器_2090757184836685826.json, 视频生成/文生视频/MiniMax H3 全能参考 自动提示词工作流_2084174326928076802.json, 视频生成/文生视频/MiniMax H3 全能参考生视频_2085373656615702530.json, 视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json, 视频生成/文生视频/minimaxH3满血版海螺H3_2085024933234692098.json, 视频生成/文生视频/video_minimax_h3_r2v 多素材联合参考_2085213870431490049.json, 视频生成/文生视频/中式天宫，东方神话美学——第一幕_2090917033448927234.json, 视频生成/文生视频/中式天宫，东方神话美学——第二幕_2090890642951073793.json, 视频生成/文生视频/多图参考H3广告_2085248140055236609.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_70

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json、视频生成/文生视频/MiniMax H3 全模态多参考视频生成器_2090757184836685826.json、视频生成/文生视频/MiniMax H3 全能参考 自动提示词工作流_2084174326928076802.json、视频生成/文生视频/MiniMax H3 全能参考生视频_2085373656615702530.json、视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
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
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `SaveVideo` —— 9/10 个有
- `LoadAudio` —— 6/10 个有
- `PreviewAny` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `MiniMaxH3AVDecodeT8` —— 1/10 个有
- `MiniMaxH3AudioConditioningT8` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/10 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `VHS_VideoCombine` —— 1/10 个有
- `llama_cpp_instruct_adv` —— 1/10 个有
- `llama_cpp_model_loader` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

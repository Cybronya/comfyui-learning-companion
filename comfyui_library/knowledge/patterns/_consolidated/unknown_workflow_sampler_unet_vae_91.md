---
name: unknown_workflow_sampler_unet_vae_91
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.855625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json, 视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json, 视频生成/文生视频/minimaxH3满血版海螺H3_2085024933234692098.json, 视频生成/文生视频/minimax_h3 多参考图生视频+sage加速_2084551631911342082.json, 视频生成/文生视频/中式天宫，东方神话美学——第一幕_2090917033448927234.json, 视频生成/文生视频/中式天宫，东方神话美学——第二幕_2090890642951073793.json, 视频生成/文生视频/海螺H3多宫格图生视频场景图生成短视频角色卡片图生成短视频_2086510723475263490.json, 视频生成/文生视频/海螺minimax_h3_多参_中文版，适配comfyui（自用）_2077373534669721601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_91

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Ref2VA 多参考生视频极速超清 2K_2101695103294328834.json、视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json、视频生成/文生视频/minimaxH3满血版海螺H3_2085024933234692098.json、视频生成/文生视频/minimax_h3 多参考图生视频+sage加速_2084551631911342082.json、视频生成/文生视频/中式天宫，东方神话美学——第一幕_2090917033448927234.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 7/8 个有
- `CreateVideo` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `LoadAudio` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `MiniMaxH3AudioConditioningT8` —— 1/8 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/8 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_169
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82825
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/超审！minimax_h3_it2v(参考生视频)  ！_2084667157266391041.json, 图片生成/文生图/超审！minimax_h3_it2v(图_文生视频) ！_2084665406370963457.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频--基础工作流_2084961117960491010.json, 视频生成/文生视频/海螺H3全能多参音视频生成开源版（9图3视频3音频）_2084825306258558977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_169

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/超审！minimax_h3_it2v(参考生视频)  ！_2084667157266391041.json、图片生成/文生图/超审！minimax_h3_it2v(图_文生视频) ！_2084665406370963457.json、视频生成/文生视频/万象AI--MiniMax H3 多参生视频--基础工作流_2084961117960491010.json、视频生成/文生视频/海螺H3全能多参音视频生成开源版（9图3视频3音频）_2084825306258558977.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `LTXVSeparateAVLatent` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SaveLatent` —— 2/4 个有
- `VAEDecode` —— 2/4 个有
- `VAEDecodeAudio` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `LayerMask: RemBgUltra` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `PainterVRAM` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

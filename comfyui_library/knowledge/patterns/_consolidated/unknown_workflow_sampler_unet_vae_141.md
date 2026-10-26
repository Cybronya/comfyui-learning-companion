---
name: unknown_workflow_sampler_unet_vae_141
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.854125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/无限长视频流_2105728965766897665.json, 视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json, 视频生成/图生视频/速度逆天！Minimax多图全能参考T8双采样8步加速版_2085471982044401665.json, 视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json, 视频生成/图生视频/高尚无限长视频流_2098617968786763777.json, 视频生成/文生视频/8步加速Mini Max H3图生视频_2084136196300697601.json, 视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json, 视频生成/文生视频/MiniMax H3超长视频流 一次直出2分15秒视频 （135S）_2101639116063600641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_141

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/无限长视频流_2105728965766897665.json、视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json、视频生成/图生视频/速度逆天！Minimax多图全能参考T8双采样8步加速版_2085471982044401665.json、视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json、视频生成/图生视频/高尚无限长视频流_2098617968786763777.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

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
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `CreateVideo` —— 4/8 个有
- `SaveVideo` —— 4/8 个有
- `VHS_VideoCombine` —— 4/8 个有
- `AudioConcat` —— 3/8 个有
- `GetImageRangeFromBatch` —— 3/8 个有
- `ImageBatchMulti` —— 3/8 个有
- `Label (rgthree)` —— 3/8 个有
- `LayerColor: ColorAdapter` —— 3/8 个有
- `MiniMaxH3AddGuide` —— 3/8 个有
- `SaveAudio` —— 3/8 个有
- `ModelAttentionBackend` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `SolAttnMiniMax` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

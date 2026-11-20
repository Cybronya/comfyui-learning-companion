---
name: unknown_workflow_sampler_unet_vae_174
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.817875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json, 视频生成/文生视频/1-MiniMaxh-H3-文生视频工作流-V2_2084639097741725698.json, 视频生成/文生视频/3-MiniMax-H3-参考生视频工作流-V2_2084639172459065346.json, 视频生成/文生视频/minimax_阿里8步加速_文生视频_图生视频_全能参考三合一_2095489469662187522.json, 视频生成/文生视频/minmaxH3单采+1参考视频_2105350818894536705.json, 视频生成/文生视频/minmaxH3单采加速_2105257162896404482.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频--基础工作流_2084961117960491010.json, 视频生成/视频生视频/FastH3 Ominiref 8步高质量视频_2113137033521754114.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_174

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json、视频生成/文生视频/1-MiniMaxh-H3-文生视频工作流-V2_2084639097741725698.json、视频生成/文生视频/3-MiniMax-H3-参考生视频工作流-V2_2084639172459065346.json、视频生成/文生视频/minimax_阿里8步加速_文生视频_图生视频_全能参考三合一_2095489469662187522.json、视频生成/文生视频/minmaxH3单采+1参考视频_2105350818894536705.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `CreateVideo` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `MiniMaxH3ImageToVideo` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `ExtendIntermediateSigmas` —— 2/8 个有
- `MiniMaxH3ContextIR` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `BlockSparseAttention` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `VHS_LoadAudioUpload` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

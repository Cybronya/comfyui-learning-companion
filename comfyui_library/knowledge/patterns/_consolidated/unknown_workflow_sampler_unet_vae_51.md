---
name: unknown_workflow_sampler_unet_vae_51
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.761643
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/开源版minimax_h3_i2v_fastH3_快速图生视频_2113910481533628418.json, 视频生成/图生视频/最强开源版minimaxH3全能参考视频短剧生成加速优化支持9图3视频3音频_2084579032405991426.json, 视频生成/图生视频/最强开源版minimaxH3全能参考视频短剧生成加速优化支持9图3视频3音频_2084602160666468354.json, 视频生成/图生视频/海螺H3(minimax H3)全能参考生视频加速开源版（9图3视频3音频）_2084186220753678337.json, 视频生成/图生视频/海螺H3全能多参音视频生成开源版（9图3视频3音频）_2089909211806388225.json, 视频生成/文生视频/AITUDOU-MiniMax H3(全能参考)_2084222366611234818.json, 视频生成/文生视频/API专用--MiniMax H3 多参生视频--基础工作流_2084516866738974722.json, 视频生成/文生视频/FS-video_minimax_h3_r2v_2105628001928044546.json, 视频生成/文生视频/FastVideo-FastH3-8-Step-V2 文生视频_2100836004453249025.json, 视频生成/文生视频/MiniMax FastH3 v2首尾帧视频_2100074906296872962.json, 视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）V2_2086281240478576641.json, 视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json, 视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_51

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/开源版minimax_h3_i2v_fastH3_快速图生视频_2113910481533628418.json、视频生成/图生视频/最强开源版minimaxH3全能参考视频短剧生成加速优化支持9图3视频3音频_2084579032405991426.json、视频生成/图生视频/最强开源版minimaxH3全能参考视频短剧生成加速优化支持9图3视频3音频_2084602160666468354.json、视频生成/图生视频/海螺H3(minimax H3)全能参考生视频加速开源版（9图3视频3音频）_2084186220753678337.json、视频生成/图生视频/海螺H3全能多参音视频生成开源版（9图3视频3音频）_2089909211806388225.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 14 个 workflow 都包含：
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
- `LoadImage` —— 13/14 个有
- `PrimitiveStringMultiline` —— 12/14 个有
- `MiniMaxH3ReferenceToVideo` —— 10/14 个有
- `VHS_VideoCombine` —— 10/14 个有
- `MiniMaxH3SigmaShift` —— 7/14 个有
- `PathchSageAttentionKJ` —— 7/14 个有
- `VHS_LoadVideo` —— 7/14 个有
- `GetNode` —— 6/14 个有
- `LoadAudio` —— 6/14 个有
- `SetNode` —— 6/14 个有
- `BlockSparseAttention` —— 4/14 个有
- `CreateVideo` —— 4/14 个有
- `MiniMaxH3ImageToVideo` —— 4/14 个有
- `ModelAttentionBackend` —— 4/14 个有
- `PainterVRAM` —— 4/14 个有
- `SaveVideo` —— 4/14 个有
- `Label (rgthree)` —— 3/14 个有
- `LoraLoaderModelOnly` —— 3/14 个有
- `MiniMaxH3BlockCacheT8` —— 1/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/14 个有
- `Text` —— 1/14 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

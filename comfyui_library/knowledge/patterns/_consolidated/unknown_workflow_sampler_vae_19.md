---
name: unknown_workflow_sampler_vae_19
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.817923
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084195676602331137.json, 视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084745751497895937.json, 视频生成/图生视频/(量化加速版)Minimax多参生视频V1_2084238539549663234.json, 视频生成/图生视频/0812日Minimax H3 ref2va加速工作流_2087422773068128257.json, 视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json, 视频生成/图生视频/1图_multi_ref_minimax_h3_i2v_2094711687055241217.json, 视频生成/图生视频/2图_multi_ref_minimax_h3_i2v_2094710093471375361.json, 视频生成/图生视频/2张参考图_2110029532303552514.json, 视频生成/图生视频/3图_multi_ref_minimax_h3_i2v_2092499319101415426.json, 视频生成/图生视频/单图参考生视频 生产力版 MiniMax+H3+H25+Hybrid_2088526268315820034.json, 视频生成/图生视频/电商4图参考考生视频  minimax h3 加速版_2089612691093676034.json, 视频生成/图生视频/电商双图参考考生视频  minimax h3 加速版_2088445593055219714.json, 视频生成/图生视频/首尾帧参考生视频 无色差版 Minimax H3_2088976531933712385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084195676602331137.json、视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084745751497895937.json、视频生成/图生视频/(量化加速版)Minimax多参生视频V1_2084238539549663234.json、视频生成/图生视频/0812日Minimax H3 ref2va加速工作流_2087422773068128257.json、视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `MiniMaxH3ReferenceToVideo` —— 11/13 个有
- `CreateVideo` —— 9/13 个有
- `PathchSageAttentionKJ` —— 9/13 个有
- `SaveVideo` —— 9/13 个有
- `UNETLoader` —— 9/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `MiniMaxH3SigmaShift` —— 6/13 个有
- `MiniMaxH3HybridLoader` —— 4/13 个有
- `VHS_VideoCombine` —— 4/13 个有
- `PainterVRAM` —— 3/13 个有
- `PreviewAny` —— 3/13 个有
- `YK_LoadImageFromURL` —— 3/13 个有
- `HAIGC_SaveImagesToZip` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `ModelAttentionBackend` —— 2/13 个有
- `BlockSparseAttention` —— 1/13 个有
- `H3AdaLNLoRAFix` —— 1/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `LoadImageFromUrl` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_51
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.848636
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(768P)Minimax多参生视频BF16高质量加速版V3_2102609315793293313.json, 视频生成/图生视频/(768P)Minimax视频参考V1_2106930546961108994.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086148083527798786.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086156036376977410.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085215256233725953.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085648828052631554.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085258096615710722.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085265592797450241.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085286536706351105.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085553480567189505.json, 视频生成/图生视频/minimax_h3 多参考图+视频参考+sage加速_2084192560171536385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_51

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/(768P)Minimax多参生视频BF16高质量加速版V3_2102609315793293313.json、视频生成/图生视频/(768P)Minimax视频参考V1_2106930546961108994.json、视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086148083527798786.json、视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086156036376977410.json、视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085215256233725953.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `CreateVideo` —— 9/11 个有
- `SaveVideo` —— 9/11 个有
- `CR Prompt Text` —— 8/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `easy showAnything` —— 3/11 个有
- `EasyCache` —— 2/11 个有
- `H3SigmaRefiner` —— 2/11 个有
- `RHMiniMaxH3PromptOptimizerCompact` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `SaveVideoRGBA` —— 2/11 个有
- `StringFunction|pysssss` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `Vignette` —— 2/11 个有
- `BatchImagesNode` —— 1/11 个有
- `VHS_VideoCombine` —— 1/11 个有
- `VideoInfoLoaded` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

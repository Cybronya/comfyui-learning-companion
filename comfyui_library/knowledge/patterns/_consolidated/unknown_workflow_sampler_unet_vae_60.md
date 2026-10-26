---
name: unknown_workflow_sampler_unet_vae_60
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.842538
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json, 视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json, 视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json, 视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json, 视频生成/图生视频/minimax多图生视频_2102951424215834626.json, 视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json, 视频生成/图生视频/video_minimax_h3_i2v_2084181095406456833.json, 视频生成/图生视频/video_minimax_h3_i2v_RH_2096548199573049346.json, 视频生成/图生视频/【老金驿站】MinimaxH3超级加速40%i2v工作流_2087177800716476417.json, 视频生成/文生视频/MiniMax H3 图生视频 首尾帧生视频_2085441158259494913.json, 视频生成/文生视频/MiniMax H3 文生视频-comfyui版_2084188214616739841.json, 视频生成/文生视频/Minimax H3 文生视频 8步加速Lora+sage双重加速工作流_2089325283299119105.json, 视频生成/文生视频/video_minimax_h3_t2v_i2v_r2v_rv2v_2091314256494022658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_60

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json、视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json、视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json、视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json、视频生成/图生视频/minimax多图生视频_2102951424215834626.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `MiniMaxH3ImageToVideo` —— 12/13 个有
- `PrimitiveFloat` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `CreateVideo` —— 9/13 个有
- `SaveVideo` —— 9/13 个有
- `GetImageSize` —— 6/13 个有
- `ImageScaleToTotalPixels` —— 6/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `VHS_VideoCombine` —— 5/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/13 个有
- `easy int` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `MiniMaxH3ReferenceToVideo` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `ImageScale` —— 1/13 个有
- `MiniMaxChunkFeedForward` —— 1/13 个有
- `MiniMaxH3TurboLoRA` —— 1/13 个有
- `ModelAttentionBackend` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有
- `VHS_LoadVideo` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

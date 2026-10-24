---
name: unknown_workflow_sampler_unet_vae_199
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7348
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/VividMuse_MiniMax_H3_多参生视频_2084280381586628609.json, 图片生成/图生图/fastH3_ref2va_2112720537771397122.json, 图片生成/图生图/trim fast minimax_2107875369050267650.json, 图片生成/文生图/H3fast-v2全参加速_2110710299581046785.json, 数字人/数字人/7度工作流改版1_2098964914600763393.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_199

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/VividMuse_MiniMax_H3_多参生视频_2084280381586628609.json、图片生成/图生图/fastH3_ref2va_2112720537771397122.json、图片生成/图生图/trim fast minimax_2107875369050267650.json、图片生成/文生图/H3fast-v2全参加速_2110710299581046785.json、数字人/数字人/7度工作流改版1_2098964914600763393.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SaveVideo` —— 4/5 个有
- `BlockSparseAttention` —— 3/5 个有
- `MiniMaxH3SigmaShift` —— 3/5 个有
- `ModelAttentionBackend` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MiniMaxH3ImageToVideo` —— 1/5 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 1/5 个有
- `PainterVRAM` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `easy positive` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

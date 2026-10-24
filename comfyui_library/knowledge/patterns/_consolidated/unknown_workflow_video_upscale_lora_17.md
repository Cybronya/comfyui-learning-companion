---
name: unknown_workflow_video_upscale_lora_17
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8135
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetImageSizeAndCount, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, Yuan_RTXVideoUpscaleH3, easy int]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 FL2VA 三阶极致放大｜2K生成式精修_2088625693134512130.json, 视频生成/文生视频/MiniMax H3 Ref2VA 二阶超清重绘｜多参考精修_2088888730617729025.json, 视频生成/文生视频/MiniMax+H3+FL2VA+二阶超清放大｜首尾帧精修_2089240886684250114.json, 视频生成/文生视频/MiniMax+H3+Ref2VA+三阶极致重绘｜2K多参考精修_2089240711672713217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 FL2VA 三阶极致放大｜2K生成式精修_2088625693134512130.json、视频生成/文生视频/MiniMax H3 Ref2VA 二阶超清重绘｜多参考精修_2088888730617729025.json、视频生成/文生视频/MiniMax+H3+FL2VA+二阶超清放大｜首尾帧精修_2089240886684250114.json、视频生成/文生视频/MiniMax+H3+Ref2VA+三阶极致重绘｜2K多参考精修_2089240711672713217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetImageSizeAndCount`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `Yuan_RTXVideoUpscaleH3`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3HybridLoader` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `ImagePadForOutpaint` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

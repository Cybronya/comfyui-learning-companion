---
name: unknown_workflow_lora_sampler_unet_198
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.905
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ColorTransfer, DepthAnythingPreprocessor, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ImageToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3图生图！2K加速版！_2114579063401697281.json, 图片生成/图生图/MiniMaxH3图生图！2K加速版！_2115015849433198594.json, 图片生成/图生图/MiniMaxH3图生图！2K加速版！_2115059679905804289.json, 图片生成/图生图/MiniMaxH3图生图！2K加速版！_2116388573745336321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_198

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3图生图！2K加速版！_2114579063401697281.json、图片生成/图生图/MiniMaxH3图生图！2K加速版！_2115015849433198594.json、图片生成/图生图/MiniMaxH3图生图！2K加速版！_2115059679905804289.json、图片生成/图生图/MiniMaxH3图生图！2K加速版！_2116388573745336321.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ColorTransfer`
- `DepthAnythingPreprocessor`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ImageToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

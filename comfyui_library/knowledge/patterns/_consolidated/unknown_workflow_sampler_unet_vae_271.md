---
name: unknown_workflow_sampler_unet_vae_271
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8498
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MImaxH3工作流超强开源视频加速ENGENG_2087086399177707522.json, 视频生成/图生视频/Mini Max H3-9图参考生音视频-高质量加速版_2095466875982536706.json, 视频生成/图生视频/MiniMax_H3_00325_唱歌_2086448635486760962.json, 视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json, 视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_271

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MImaxH3工作流超强开源视频加速ENGENG_2087086399177707522.json、视频生成/图生视频/Mini Max H3-9图参考生音视频-高质量加速版_2095466875982536706.json、视频生成/图生视频/MiniMax_H3_00325_唱歌_2086448635486760962.json、视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json、视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 3/5 个有
- `ResizeImagesByLongerEdge` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `EasyCache` —— 2/5 个有
- `RTXVideoSuperResolution` —— 2/5 个有
- `ApplyFaceProcessor` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CompressImages` —— 1/5 个有
- `FaceProcessorLoader` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SaveMP4` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

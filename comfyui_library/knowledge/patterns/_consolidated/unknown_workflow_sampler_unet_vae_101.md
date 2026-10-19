---
name: unknown_workflow_sampler_unet_vae_101
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.840714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MImaxH3工作流超强开源视频加速ENGENG_2087086399177707522.json, 视频生成/图生视频/MiniMax H3 4图生视频+音频接入_2090184072877395969.json, 视频生成/图生视频/MiniMax H3 8步加速 智能参考娃娃穿搭视频生成_2085536956800397314.json, 视频生成/图生视频/MiniMax H3 【参考图+参考音频】4步生视频_2090646084061323265.json, 视频生成/图生视频/MiniMax H3 多参输入生视频_2085272663802605570.json, 视频生成/图生视频/MiniMax H3 多图生视频+音频接入_2090182586948734978.json, 视频生成/图生视频/MiniMax H3 音频驱动（数字人）唱歌视频_2084544809620041730.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_101

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MImaxH3工作流超强开源视频加速ENGENG_2087086399177707522.json、视频生成/图生视频/MiniMax H3 4图生视频+音频接入_2090184072877395969.json、视频生成/图生视频/MiniMax H3 8步加速 智能参考娃娃穿搭视频生成_2085536956800397314.json、视频生成/图生视频/MiniMax H3 【参考图+参考音频】4步生视频_2090646084061323265.json、视频生成/图生视频/MiniMax H3 多参输入生视频_2085272663802605570.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `MiniMaxH3SigmaShift` —— 2/7 个有
- `ApplyFaceProcessor` —— 1/7 个有
- `CompressImages` —— 1/7 个有
- `FaceProcessorLoader` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SaveMP4` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SeedVR2BlockSwap` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有
- `TrimAudioDuration` —— 1/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

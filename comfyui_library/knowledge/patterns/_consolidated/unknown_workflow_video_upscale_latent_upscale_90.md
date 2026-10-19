---
name: unknown_workflow_video_upscale_latent_upscale_90
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.45225
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, GetNode, JWFloat, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVLatentSeparateT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, VRAM_Debug]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3-多参生视频_2099054818437459969.json, 视频生成/图生视频/MiniMaxH3-多参生视频_2099773384988127233.json, 视频生成/图生视频/MiniMaxH3-多参生视频_2100033508268920833.json, 视频生成/图生视频/【AI影视剧制作】MiniMaxH3-多参视频生成发布版_2109119782388846593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_90

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3-多参生视频_2099054818437459969.json、视频生成/图生视频/MiniMaxH3-多参生视频_2099773384988127233.json、视频生成/图生视频/MiniMaxH3-多参生视频_2100033508268920833.json、视频生成/图生视频/【AI影视剧制作】MiniMaxH3-多参视频生成发布版_2109119782388846593.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `GetNode`
- `JWFloat`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVLatentSeparateT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRAM_Debug`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 3/4 个有
- `MiniMaxLowVRAMAttention` —— 3/4 个有
- `PreviewImage` —— 3/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

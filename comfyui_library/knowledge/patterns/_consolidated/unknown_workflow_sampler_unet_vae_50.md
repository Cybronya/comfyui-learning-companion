---
name: unknown_workflow_sampler_unet_vae_50
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.809182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2102924951413153793.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2103672100170067969.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2104844242353999874.json, 视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 参考生视频_2108491242530234370.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 首尾帧_2108488300557328386.json, 视频生成/图生视频/Minimax H3 参考图和参考视音频生成视频满血版_2105625287546462210.json, 视频生成/图生视频/Minimax3-参考生视频-8月8日版_2086541785450500098.json, 视频生成/图生视频/R2V-参考生视频-5060Ti16G-极速加速版_2102730812373422081.json, 视频生成/文生视频/MiniMax H3 文图生视频、参考生视频多合一工作流-B站UP主@好奇漫步_2086134141166383105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_50

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json、视频生成/图生视频/MiniMax_H3_参考生视频_2102924951413153793.json、视频生成/图生视频/MiniMax_H3_参考生视频_2103672100170067969.json、视频生成/图生视频/MiniMax_H3_参考生视频_2104844242353999874.json、视频生成/图生视频/Minimax H3 - 多参视频生成_2086482284911357953.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `ComfySwitchNode` —— 8/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `PrimitiveInt` —— 8/11 个有
- `LoadAudio` —— 7/11 个有
- `PrimitiveBoolean` —— 7/11 个有
- `GetVideoComponents` —— 3/11 个有
- `LoadVideo` —— 3/11 个有
- `MiniMaxH3ImageToVideo` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `VedaSparseAttention` —— 2/11 个有
- `ImageUpscaleWithModel` —— 1/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/11 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/11 个有
- `ModelAttentionBackend` —— 1/11 个有
- `SpectrumApplyMiniMaxH3` —— 1/11 个有
- `UpscaleModelLoader` —— 1/11 个有
- `XB_ReferenceAny` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

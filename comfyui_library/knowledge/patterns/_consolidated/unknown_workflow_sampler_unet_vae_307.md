---
name: unknown_workflow_sampler_unet_vae_307
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.746
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, LoadAudio, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/58.MiniMax H3 全能参考加速极简_2087136892977504257.json, 视频生成/文生视频/MiniMax H3+lightx2v 4步加速全能参考工作流_2086324132442107906.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）V2_2086281240478576641.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_307

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/58.MiniMax H3 全能参考加速极简_2087136892977504257.json、视频生成/文生视频/MiniMax H3+lightx2v 4步加速全能参考工作流_2086324132442107906.json、视频生成/文生视频/MiniMax H3多参2倍速（开源版）V2_2086281240478576641.json、视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `LoadAudio`
- `LoadImage`
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
- `BasicScheduler` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `SpectrumSDXL` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MiniMaxH3BlockCacheT8` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `TextInput` —— 1/4 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

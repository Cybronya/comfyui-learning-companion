---
name: unknown_workflow_sampler_unet_vae_118
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.780571
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/58.MiniMax H3 全能参考加速极简_2087136892977504257.json, 视频生成/文生视频/MiniMax H3+lightx2v 4步加速全能参考工作流_2086324132442107906.json, 视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json, 视频生成/文生视频/Minimax_h3官方多参视频生成工作流_2084688064726781954.json, 视频生成/文生视频/minimaxH3多参考视频工作流（超级加速版）_2080928622717784066.json, 视频生成/文生视频/minimaxH3数字人唱歌_2095054420571676674.json, 视频生成/文生视频/minimaxH3数字人工作流（音频驱动）_2094755368487444482.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_118

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/58.MiniMax H3 全能参考加速极简_2087136892977504257.json、视频生成/文生视频/MiniMax H3+lightx2v 4步加速全能参考工作流_2086324132442107906.json、视频生成/文生视频/MiniMax H3多参2倍速（开源版）_2084599726879629314.json、视频生成/文生视频/Minimax_h3官方多参视频生成工作流_2084688064726781954.json、视频生成/文生视频/minimaxH3多参考视频工作流（超级加速版）_2080928622717784066.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `VAEDecodeAudio` —— 5/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `AudioCrop` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `Label (rgthree)` —— 3/7 个有
- `ModelPreviewOverrideKJ` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/7 个有
- `SoundFlow_GetLength` —— 2/7 个有
- `SpectrumSDXL` —— 2/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `TextInput` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

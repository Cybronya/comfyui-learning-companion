---
name: unknown_workflow_sampler_unet_vae_169
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.817429
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/（2320）H3-最优官流_2089001915131711490.json, 视频生成/文生视频/260818002. MiniMax-H3 全能参考速生视频_2089370236645634050.json, 视频生成/文生视频/A-5 MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2084649315783503873.json, 视频生成/文生视频/H3-最优官流_2088982134630469634.json, 视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json, 视频生成/文生视频/MiniMax H3+lightx2v 4步加速全能参考工作流_2086324132442107906.json, 视频生成/文生视频/minimaxH3多参考视频工作流（超级加速版）_2080928622717784066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_169

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/（2320）H3-最优官流_2089001915131711490.json、视频生成/文生视频/260818002. MiniMax-H3 全能参考速生视频_2089370236645634050.json、视频生成/文生视频/A-5 MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2084649315783503873.json、视频生成/文生视频/H3-最优官流_2088982134630469634.json、视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `BasicScheduler` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `ModelPreviewOverrideKJ` —— 3/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `ManualSigmas` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/7 个有
- `SpectrumSDXL` —— 1/7 个有
- `VHS_LoadAudioUpload` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

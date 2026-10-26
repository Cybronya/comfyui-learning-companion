---
name: unknown_workflow_sampler_unet_vae_143
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.82875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json, 视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json, 视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json, 视频生成/文生视频/4步MiniMax-H3文生视频-LynnReal-Omni_2099804217237135361.json, 视频生成/文生视频/A-3 MiniMax-H3 文生视频 开源版_2084541355501641730.json, 视频生成/文生视频/A-3_MiniMax-H3_文生视频_开源版_2100205096012443649.json, 视频生成/文生视频/MINIMAX-H3工作流_2091759961062862849.json, 视频生成/文生视频/[Minimax H3]9图片+3音频全能参考_2084583737949511681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_143

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json、视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json、视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json、视频生成/文生视频/4步MiniMax-H3文生视频-LynnReal-Omni_2099804217237135361.json、视频生成/文生视频/A-3 MiniMax-H3 文生视频 开源版_2084541355501641730.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 7/8 个有
- `MiniMaxH3ImageToVideo` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `LoadImage` —— 3/8 个有
- `MiniMaxH3ReferenceToVideo` —— 3/8 个有
- `LoadAudio` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `ComfyNumberConvert` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetVideoComponents` —— 1/8 个有
- `Image Compare (mtb)` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

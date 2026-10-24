---
name: unknown_workflow_sampler_unet_vae_286
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.768333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/高质量MINIMAX-H3文生视频-短剧漫剧生成_2084320532614443010.json, 音频生成/音频生成/minimax-H3-单音频-声音克隆_2099008776971051009.json, 音频生成/音频生成/minimax-H3-单音频-声音克隆_2109827821043535873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_286

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/高质量MINIMAX-H3文生视频-短剧漫剧生成_2084320532614443010.json、音频生成/音频生成/minimax-H3-单音频-声音克隆_2099008776971051009.json、音频生成/音频生成/minimax-H3-单音频-声音克隆_2109827821043535873.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 2/3 个有
- `SaveAudioAdvanced` —— 2/3 个有
- `StringFormat` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `VAEDecode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

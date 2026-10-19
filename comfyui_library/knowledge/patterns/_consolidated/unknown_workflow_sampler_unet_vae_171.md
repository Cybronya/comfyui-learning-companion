---
name: unknown_workflow_sampler_unet_vae_171
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/时尚穿搭视频Lookbook Minimax H3_2108419577200861186.json, 视频生成/文生视频/Minimax参考生视频 高质量 加速版_2086430508090744833.json, 视频生成/文生视频/Minimax图生视频高质量加速版_2087062490541813762.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_171

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/时尚穿搭视频Lookbook Minimax H3_2108419577200861186.json、视频生成/文生视频/Minimax参考生视频 高质量 加速版_2086430508090744833.json、视频生成/文生视频/Minimax图生视频高质量加速版_2087062490541813762.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `MiniMaxH3BlockCacheT8` —— 2/3 个有
- `MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `ConcatenateVideo` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `MiniMaxH3AddGuide` —— 1/3 个有
- `MiniMaxH3ImageToVideo` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `ResizeAndPadImage` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

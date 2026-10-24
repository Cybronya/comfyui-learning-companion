---
name: unknown_workflow_sampler_unet_vae_281
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, MiniMaxH3SigmaShift, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json, 视频生成/图生视频/Minimax-H3 360°环绕与卡片旋转视频_2109661372345831426.json, 视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_281

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json、视频生成/图生视频/Minimax-H3 360°环绕与卡片旋转视频_2109661372345831426.json、视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniMaxH3ImageToVideo` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DF_Integer` —— 1/3 个有
- `Int` —— 1/3 个有
- `MiniMaxChunkFeedForward` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

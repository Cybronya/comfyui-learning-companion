---
name: unknown_workflow_sampler_unet_vae_190
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.907
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3SigmaShift, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json, 视频生成/图生视频/Minimax-H3 360°环绕与卡片旋转视频_2109661372345831426.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜参考生视频_2098326332844363777.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜首尾帧视频_2098317959839174657.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜参考生视频_2098326323948244994.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜首尾帧视频_2098326342881333250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_190

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json、视频生成/图生视频/Minimax-H3 360°环绕与卡片旋转视频_2109661372345831426.json、视频生成/文生视频/MiniMax H3｜LightX2V 4步｜参考生视频_2098326332844363777.json、视频生成/文生视频/MiniMax H3｜LightX2V 4步｜首尾帧视频_2098317959839174657.json、视频生成/文生视频/MiniMax H3｜LightX2V 8步｜参考生视频_2098326323948244994.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3AudioConditioningT8` —— 4/6 个有
- `CR Text` —— 1/6 个有
- `DF_Integer` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3ImageToVideo` —— 1/6 个有
- `MiniMaxH3ReferenceToVideo` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

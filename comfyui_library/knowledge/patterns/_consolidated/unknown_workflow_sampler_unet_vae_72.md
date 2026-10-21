---
name: unknown_workflow_sampler_unet_vae_72
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8958
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, LoadImage, MiniMaxH3AudioConditioningT8, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜Larry 4步｜参考生视频_2098331637259001857.json, 视频生成/文生视频/MiniMax H3｜Larry 4步｜首尾帧_2098334091904118785.json, 视频生成/文生视频/MiniMax H3｜Larry 8步｜参考生视频_2098334052255363074.json, 视频生成/文生视频/MiniMax H3｜Larry 8步｜首尾帧_2098334066805395458.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜参考生视频_2098326332844363777.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜首尾帧视频_2098317959839174657.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜参考生视频_2098326323948244994.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜首尾帧视频_2098326342881333250.json, 视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json, 视频生成/文生视频/MiniMax H3｜Sol Attention｜首尾帧+参考生视频_2098331649598640129.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_72

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜Larry 4步｜参考生视频_2098331637259001857.json、视频生成/文生视频/MiniMax H3｜Larry 4步｜首尾帧_2098334091904118785.json、视频生成/文生视频/MiniMax H3｜Larry 8步｜参考生视频_2098334052255363074.json、视频生成/文生视频/MiniMax H3｜Larry 8步｜首尾帧_2098334066805395458.json、视频生成/文生视频/MiniMax H3｜LightX2V 4步｜参考生视频_2098326332844363777.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 6/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `MiniMaxH3SigmaShift` —— 4/10 个有
- `MiniMaxH3TurboLoRA` —— 4/10 个有
- `MiniMaxH3TurboSampler` —— 4/10 个有
- `MiniMaxH3MemoryEfficientSolAttentionPatch` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

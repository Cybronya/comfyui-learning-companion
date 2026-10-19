---
name: unknown_workflow_sampler_unet_vae_175
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.558333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, CreateVideo, GetNode, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3文生视频、图生视频、参考生视频、动作迁移、人物替换自由切换，双重加速版_2086132690054639617.json, 视频生成/文生视频/MinimaxH3首尾帧2倍速V2_2086280974836527106.json, 视频生成/文生视频/乡野爬山好风光_2087832652211638274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Minimax H3文生视频、图生视频、参考生视频、动作迁移、人物替换自由切换，双重加速版_2086132690054639617.json、视频生成/文生视频/MinimaxH3首尾帧2倍速V2_2086280974836527106.json、视频生成/文生视频/乡野爬山好风光_2087832652211638274.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `MiniMaxH3BlockCacheT8` —— 2/3 个有
- `MiniMaxH3ImageToVideo` —— 2/3 个有
- `MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `EasyCache` —— 1/3 个有
- `Int` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

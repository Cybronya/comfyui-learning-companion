---
name: unknown_workflow_sampler_unet_vae_174
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96325
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json, 视频生成/图生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json, 视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json, 视频生成/文生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_174

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax H3首尾帧视频生成_2085198810418077698.json、视频生成/图生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json、视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json、视频生成/文生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `LTXVSeparateAVLatent` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `Int` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

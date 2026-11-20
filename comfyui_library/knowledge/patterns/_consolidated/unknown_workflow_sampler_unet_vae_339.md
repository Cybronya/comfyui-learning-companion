---
name: unknown_workflow_sampler_unet_vae_339
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.962
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, Int, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json, 视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json, 视频生成/文生视频/minimax 首尾帧加速版_2084471697830404098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_339

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json、视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json、视频生成/文生视频/minimax 首尾帧加速版_2084471697830404098.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `Int`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

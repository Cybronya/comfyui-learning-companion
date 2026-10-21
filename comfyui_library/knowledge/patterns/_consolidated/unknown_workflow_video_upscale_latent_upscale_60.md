---
name: unknown_workflow_video_upscale_latent_upscale_60
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.4665
common_nodes: [BasicGuider, BasicScheduler, FeiHouEasyH3RH, FeiHouEasyH3RHLoader, FeiHouEasyH3RHLoraStack, FeiHouEasyH3RHOutput, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, RandomSeedNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, easy cleanGpuUsed, easy float, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/文生图/minimax_h3_极简画布模式多参工作流_2098939356470931457.json, 图片生成/文生图/minimax_h3_极简画布模式多参工作流_2099674240306995201.json, 视频生成/图生视频/Minimax_H3_全能参考漫剧工作流_2099768671395733506.json, 视频生成/图生视频/Minimax_H3_全能参考漫剧工作流_2100029946231083009.json, 视频生成/图生视频/minimax_h3_极简画布模式多参工作流_2099788558071582722.json, 视频生成/图生视频/minimax_h3_极简画布模式多参工作流_2100044087197003778.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_60

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/minimax_h3_极简画布模式多参工作流_2098939356470931457.json、图片生成/文生图/minimax_h3_极简画布模式多参工作流_2099674240306995201.json、视频生成/图生视频/Minimax_H3_全能参考漫剧工作流_2099768671395733506.json、视频生成/图生视频/Minimax_H3_全能参考漫剧工作流_2100029946231083009.json、视频生成/图生视频/minimax_h3_极简画布模式多参工作流_2099788558071582722.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `FeiHouEasyH3RH`
- `FeiHouEasyH3RHLoader`
- `FeiHouEasyH3RHLoraStack`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `RandomSeedNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy float`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

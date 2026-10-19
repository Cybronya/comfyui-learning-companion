---
name: unknown_workflow_video_sampler_unet_60
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6828
common_nodes: [BasicGuider, MiniMaxH3AVDecodeT8GH, MiniMaxH3DualClockT8GH, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-H3图生视频工作流.json, 视频生成/文生视频/minimax-h3-全能参考一体化_2093965123072380929.json, 视频生成/文生视频/【傲雪AIGC】MiniMax - H3 短剧+漫剧+真人剧 - 多参视频输出_2092871905568182273.json, 视频生成/文生视频/全自动智能MiniMax - H3 全自动提示词智能视频创作平台_2090358016645357569.json, 视频生成/文生视频/图+音+MiniMaxH3_2093570622650667014.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3图生视频工作流.json、视频生成/文生视频/minimax-h3-全能参考一体化_2093965123072380929.json、视频生成/文生视频/【傲雪AIGC】MiniMax - H3 短剧+漫剧+真人剧 - 多参视频输出_2092871905568182273.json、视频生成/文生视频/全自动智能MiniMax - H3 全自动提示词智能视频创作平台_2090358016645357569.json、视频生成/文生视频/图+音+MiniMaxH3_2093570622650667014.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `MiniMaxH3AVDecodeT8GH`
- `MiniMaxH3DualClockT8GH`
- `MiniMaxH3IntegrationAdapterGH`
- `MiniMaxH3IntegrationGH`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `easy ifElse` —— 4/5 个有
- `easy anythingIndexSwitch` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `SaveAudioAdvanced` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/5 个有
- `RH_RhartImageG2OfficialTextToImage` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

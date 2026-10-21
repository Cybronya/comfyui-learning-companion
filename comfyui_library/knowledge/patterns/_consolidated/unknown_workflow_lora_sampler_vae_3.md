---
name: unknown_workflow_lora_sampler_vae_3
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9788
common_nodes: [BasicGuider, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio]
problems: []
missing: []
members: [视频生成/文生视频/Minimax-H3加速一站式工作流_2086720729625743361.json, 视频生成/文生视频/MinimaxH3工作流多合一极简版_2088792747246444545.json, 视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧全能参考加速lora）_2086651785254621186.json, 视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧全能参考加速lora）_2086696294881513474.json, 视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧多图参考加速lora）_2088157268767494145.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3加速一站式工作流_2086720729625743361.json、视频生成/文生视频/MinimaxH3工作流多合一极简版_2088792747246444545.json、视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧全能参考加速lora）_2086651785254621186.json、视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧全能参考加速lora）_2086696294881513474.json、视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧多图参考加速lora）_2088157268767494145.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `SpectrumSDXL` —— 3/5 个有
- `BasicScheduler` —— 1/5 个有
- `KSamplerSelect` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `SpectrumApplyMiniMaxH3` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

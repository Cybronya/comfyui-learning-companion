---
name: unknown_workflow_lora_sampler_vae_4
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.98915
common_nodes: [BasicGuider, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio]
problems: []
missing: []
members: [平台全量/MiniMax_H3_Easy_hybrid_2117587641150562306.json, 平台全量/minimax加速一站式工作流文生视频图生视频首尾帧多图参考加速lora_2117753467589709825.json, 视频生成/图生视频/MiniMax H3 真人娃娃换装_2088546321346162689.json, 视频生成/图生视频/Minimax H3加速Lora6步直出1080P_2085682508917727234.json, 视频生成/文生视频/H3 六步文生视频｜短片预检版_2098739088026329089.json, 视频生成/文生视频/MiniMax_H3_Easy_hybrid全能参考极简多合一工作流_2105216168821878786.json, 视频生成/文生视频/Minimax H3开源加速版 Lora6步直出1080P文生视频_2086042110033219586.json, 视频生成/文生视频/Minimax H3开源加速版 Lora6步直出1080P文生视频_2086051839778316289.json, 视频生成/文生视频/Minimax H3开源加速版 Lora6步直出1080P文生视频_2087868991841849345.json, 视频生成/文生视频/Minimax H3开源加速版 Lora6步直出1080P文生视频_2087890006252806145.json, 视频生成/文生视频/Minimax H3开源加速版 Lora6步直出1080P文生视频短剧神器_2086795901573619713.json, 视频生成/文生视频/Minimax H3开源加速版文生视频 Lora6步直出1080P短剧广告片视频生成_2087140452066746369.json, 视频生成/文生视频/Minimax H3开源加速版文生视频 Lora6步直出1080P短剧广告片视频生成_2087145404403109889.json, 视频生成/文生视频/Minimax H3开源加速版文生视频 Lora6步直出1080P短剧广告片视频生成_2089298256638603266.json, 视频生成/文生视频/Minimax H3开源加速版文生视频 Lora6步直出1080P短剧广告片视频生成_2089314898022068226.json, 视频生成/文生视频/Minimax-H3加速一站式工作流_2086720729625743361.json, 视频生成/文生视频/MinimaxH3Lora6步直出1080P文生视频短剧神器ENG开源加速版ENGENG_2087096703185936385.json, 视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧全能参考加速lora）_2086651785254621186.json, 视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧全能参考加速lora）_2086696294881513474.json, 视频生成/文生视频/minimax加速一站式工作流（文生视频图生视频首尾帧多图参考加速lora）_2088157268767494145.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（平台全量/MiniMax_H3_Easy_hybrid_2117587641150562306.json、平台全量/minimax加速一站式工作流文生视频图生视频首尾帧多图参考加速lora_2117753467589709825.json、视频生成/图生视频/MiniMax H3 真人娃娃换装_2088546321346162689.json、视频生成/图生视频/Minimax H3加速Lora6步直出1080P_2085682508917727234.json、视频生成/文生视频/H3 六步文生视频｜短片预检版_2098739088026329089.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 14/20 个有
- `KSamplerSelect` —— 14/20 个有
- `ImageResizeKJv2` —— 12/20 个有
- `MiniMaxH3SigmaShift` —— 12/20 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 6/20 个有
- `SpectrumSDXL` —— 5/20 个有
- `LoadImage` —— 4/20 个有
- `MiniMaxH3EasyMediaLoader` —— 2/20 个有
- `PrimitiveStringMultiline` —— 1/20 个有
- `SpectrumApplyMiniMaxH3` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_267
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9085
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, H3ExactRecover, H3InjectSchedule, H3JerkHeatmap, H3JerkOracle, H3TimeSmear, H3V2VInit, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3战斗专用视频工作流Supermate_2088565137006481410.json, 视频生成/图生视频/Minimax-H3-图生视频-拖影修复_2088984353446653953.json, 视频生成/图生视频/MinimaxH3-参考生视频-残影优化工作流_2089951187620683778.json, 视频生成/图生视频/MinimaxH3拖影强化参考生视频工作流_2088291115316371458.json, 视频生成/文生视频/Minimax H3-文生视频-残影优化工作流_2089951230276751361.json, 视频生成/文生视频/Minimax H3开源版 拖影强化版文生视频工作流_2088568398233038849.json, 视频生成/文生视频/Minimax H3开源版 拖影强化版文生视频工作流_2088607540094521346.json, 视频生成/文生视频/Minimax H3拖影强化文生视频工作流_2088291098631434242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_267

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3战斗专用视频工作流Supermate_2088565137006481410.json、视频生成/图生视频/Minimax-H3-图生视频-拖影修复_2088984353446653953.json、视频生成/图生视频/MinimaxH3-参考生视频-残影优化工作流_2089951187620683778.json、视频生成/图生视频/MinimaxH3拖影强化参考生视频工作流_2088291115316371458.json、视频生成/文生视频/Minimax H3-文生视频-残影优化工作流_2089951230276751361.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `H3ExactRecover`
- `H3InjectSchedule`
- `H3JerkHeatmap`
- `H3JerkOracle`
- `H3TimeSmear`
- `H3V2VInit`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 6/8 个有
- `SaveVideo` —— 6/8 个有
- `H3AudioRecover` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `MiniMaxH3ImageToVideo` —— 4/8 个有
- `MiniMaxH3ReferenceToVideo` —— 4/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `孤海注释` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

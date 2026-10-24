---
name: unknown_workflow_video_sampler_vae_46
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8197
common_nodes: [BasicGuider, CLIPLoader, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, RandomNoise, SamplerCustomAdvanced, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/H3_Turbo_Stable_4V4A_2087928785877430274.json, 视频生成/文生视频/MiniMax H3 动作自然度增强工作流-AI人物动作流畅不僵硬_2097931937448022018.json, 视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json, 视频生成/文生视频/MiniMax_H3_动作自然度增强工作流-AI人物动作流畅不僵硬_2100061739890069505.json, 视频生成/文生视频/MiniMax_H3_动作自然度增强工作流-AI人物动作流畅不僵硬_2100140680126492673.json, 视频生成/文生视频/MinimaxH3 全功能加速工作流_2086320789044944897.json, 视频生成/文生视频/Minimax参考生视频(最新插件双时钟+4步lora8步高质量极速)_2085606301979209730.json, 视频生成/文生视频/Minimax双时钟图生视频加速版_2087634755666931713.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V1_2085629759433822210.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V2_2093869475740344321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_46

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/H3_Turbo_Stable_4V4A_2087928785877430274.json、视频生成/文生视频/MiniMax H3 动作自然度增强工作流-AI人物动作流畅不僵硬_2097931937448022018.json、视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json、视频生成/文生视频/MiniMax_H3_动作自然度增强工作流-AI人物动作流畅不僵硬_2100061739890069505.json、视频生成/文生视频/MiniMax_H3_动作自然度增强工作流-AI人物动作流畅不僵硬_2100140680126492673.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DualClockSamplerT8` —— 8/10 个有
- `LoraLoaderBypassModelOnly` —— 7/10 个有
- `UNETLoader` —— 7/10 个有
- `LoadImage` —— 6/10 个有
- `PrimitiveFloat` —— 6/10 个有
- `ComfyMathExpression` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `ResolutionSelector` —— 5/10 个有
- `CR Prompt Text` —— 4/10 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 4/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 3/10 个有
- `GetNode` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `MiniMaxH3FastH34StepSetupT8Advanced` —— 1/10 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

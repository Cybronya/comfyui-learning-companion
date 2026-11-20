---
name: unknown_workflow_video_lora_sampler_134
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.838929
common_nodes: [BasicGuider, CLIPLoader, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json, 视频生成/文生视频/Minimax参考生视频(最新插件双时钟+4步lora8步高质量极速)_2085606301979209730.json, 视频生成/文生视频/Minimax双时钟图生视频加速版_2087634755666931713.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V1_2085629759433822210.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V2_2093869475740344321.json, 视频生成/文生视频/Minimax文生视频（Lightx2v正式版8步lora+双时钟）_2087718430937014273.json, 视频生成/文生视频/minimaxH3文生视频（light2v8步lora+双时钟）_2087529767288524801.json, 视频生成/文生视频/minimax三图工作流_2090738092591378434.json, 视频生成/文生视频/minimax三图工作流_2091847130888630274.json, 视频生成/文生视频/minimax九图工作流_2091582636920758274.json, 视频生成/文生视频/minimax九图工作流_2092593622448427010.json, 视频生成/文生视频/minimax九图工作流_2102148767163183105.json, 视频生成/文生视频/双时钟采样6步极速图文生视频_2085767587174113281.json, 视频生成/文生视频/极速版 MinimaxH3 文生视频 图生视频  T8版_2085912109149417474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_134

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json、视频生成/文生视频/Minimax参考生视频(最新插件双时钟+4步lora8步高质量极速)_2085606301979209730.json、视频生成/文生视频/Minimax双时钟图生视频加速版_2087634755666931713.json、视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V1_2085629759433822210.json、视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V2_2093869475740344321.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 13/14 个有
- `MiniMaxH3DualClockSamplerT8` —— 13/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/14 个有
- `ResolutionSelector` —— 13/14 个有
- `CR Prompt Text` —— 12/14 个有
- `LoadImage` —— 12/14 个有
- `ModelAttentionBackend` —— 4/14 个有
- `VHS_LoadVideo` —— 3/14 个有
- `GetNode` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `LoadAudio` —— 1/14 个有
- `MiniMaxH3FastH34StepSetupT8Advanced` —— 1/14 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 1/14 个有
- `MiniMaxH3SigmaShift` —— 1/14 个有
- `ModelPreviewOverrideKJ` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

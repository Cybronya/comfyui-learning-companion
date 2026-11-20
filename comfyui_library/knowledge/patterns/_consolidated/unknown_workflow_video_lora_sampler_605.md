---
name: unknown_workflow_video_lora_sampler_605
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6656
common_nodes: [BasicGuider, BasicScheduler, JWImageResizeToMegapixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, ViggleAnimateConditioning, ViggleTextCondLoader]
problems: []
missing: []
members: [视频生成/图生视频/H3動作遷移_目前支持10秒_2099764920819732482.json, 视频生成/图生视频/minimax-H3+Viggle  动作迁移强化版 免提示词_2109956166884356097.json, 视频生成/图生视频/minimax-H3+Viggle  动作迁移强化版 免提示词_2109987503527784449.json, 视频生成/图生视频/动作迁移美女跳舞minimax-H3+Viggle （ 免提示词 超级简化版）_2110005406293643265.json, 视频生成/文生视频/Viggle-animate-h3视频角色替换_2097851117714632705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_605

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/H3動作遷移_目前支持10秒_2099764920819732482.json、视频生成/图生视频/minimax-H3+Viggle  动作迁移强化版 免提示词_2109956166884356097.json、视频生成/图生视频/minimax-H3+Viggle  动作迁移强化版 免提示词_2109987503527784449.json、视频生成/图生视频/动作迁移美女跳舞minimax-H3+Viggle （ 免提示词 超级简化版）_2110005406293643265.json、视频生成/文生视频/Viggle-animate-h3视频角色替换_2097851117714632705.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `JWImageResizeToMegapixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ViggleAnimateConditioning`
- `ViggleTextCondLoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/5 个有
- `CR Value` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `BlockSparseAttention` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `CustomSigmas` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

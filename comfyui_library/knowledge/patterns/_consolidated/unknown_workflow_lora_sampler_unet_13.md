---
name: unknown_workflow_lora_sampler_unet_13
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.865125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/10Eros-Max 8步极速4视图生视频 v2.0_2087352692522962945.json, 视频生成/图生视频/260813001.Minimax-H3多图参考生视频_2088059548048379905.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json, 视频生成/图生视频/Minimax H3参考生视频-电商带货-8步加速版_2107686836549279745.json, 视频生成/图生视频/Minimax H3参考生视频-电商带货-8步加速版_2109966408665878530.json, 视频生成/图生视频/Minimax-H3-8步加速-多参考生视频（平均3.5分钟出5秒）_2085387387793928194.json, 视频生成/文生视频/🍲Minimax-H3多模态参考4步加速极限双优版🍲_2086661468988198913.json, 视频生成/文生视频/🍲Minimax-H3提示词自动优化+4步加速极限双优版🍲_2086652281939914753.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/10Eros-Max 8步极速4视图生视频 v2.0_2087352692522962945.json、视频生成/图生视频/260813001.Minimax-H3多图参考生视频_2088059548048379905.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json、视频生成/图生视频/Minimax H3参考生视频-电商带货-8步加速版_2107686836549279745.json、视频生成/图生视频/Minimax H3参考生视频-电商带货-8步加速版_2109966408665878530.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `孤海注释` —— 4/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `easy convertAnything` —— 3/8 个有
- `easy int` —— 3/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `Text` —— 2/8 个有
- `DapaoH3PromptBoxNode` —— 1/8 个有
- `DapaoH3VideoPromptNode` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `MmuuaiGroupBypass` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `SaveLatent` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

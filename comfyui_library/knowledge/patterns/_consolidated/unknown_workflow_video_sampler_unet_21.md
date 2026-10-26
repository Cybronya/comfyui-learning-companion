---
name: unknown_workflow_video_sampler_unet_21
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.875643
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/单人换视频中的单人（简单提示词)_2113259206127210498.json, 视频生成/图生视频/单图Minimax H3_2084901814679461889.json, 视频生成/图生视频/单图Minimax H3_2085688315197616129.json, 视频生成/图生视频/多参生成视频_2110673932587200514.json, 视频生成/图生视频/润哥教育IP数字人_H3_R2V_2111327138715623425.json, 视频生成/图生视频/自用H3官流（终极版）_2108147321883152385.json, 视频生成/图生视频/街舞表演视频制作_2106024930591731713.json, 视频生成/图生视频/（api强化武打）竖屏640p坤坤H3官流lora加速20步_2114244637195071489.json, 视频生成/图生视频/（api）横屏640p坤坤H3官流无lora12步_2110413455923699713.json, 视频生成/图生视频/（api）竖屏608p坤坤H3官流无lora_2108200300300554241.json, 视频生成/图生视频/（api）竖屏768p坤坤H3官流_2108103067618070530.json, 视频生成/文生视频/H3官流全能参考9图1音频1视频_2105563203647393793.json, 视频生成/文生视频/H3官流（mpov版）-不用加速lora_2107126428574773249.json, 视频生成/文生视频/H3官流（单采极速文戏）_2106642679642812418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/单人换视频中的单人（简单提示词)_2113259206127210498.json、视频生成/图生视频/单图Minimax H3_2084901814679461889.json、视频生成/图生视频/单图Minimax H3_2085688315197616129.json、视频生成/图生视频/多参生成视频_2110673932587200514.json、视频生成/图生视频/润哥教育IP数字人_H3_R2V_2111327138715623425.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 13/14 个有
- `ModelAttentionBackend` —— 13/14 个有
- `VAEDecodeAudio` —— 13/14 个有
- `BlockSparseAttention` —— 11/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `ModelPreviewOverrideKJ` —— 10/14 个有
- `ManualSigmas` —— 9/14 个有
- `LoadAudio` —— 8/14 个有
- `VHS_LoadVideo` —— 5/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/14 个有
- `MiniMaxH3SigmaShift` —— 2/14 个有
- `SolAttnMiniMax` —— 2/14 个有
- `ExtendIntermediateSigmas` —— 1/14 个有
- `GetVideoComponents` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `LoadVideo` —— 1/14 个有
- `LoraLoaderBypassModelOnly` —— 1/14 个有
- `PreviewAny` —— 1/14 个有
- `忽略多组孤海` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

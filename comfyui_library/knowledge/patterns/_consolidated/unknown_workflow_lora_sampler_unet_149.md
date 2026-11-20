---
name: unknown_workflow_lora_sampler_unet_149
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.882333
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/人物替换工作流1_2115370839989383170.json, 视频生成/图生视频/润哥教育IP数字人_H3_R2V_2111327138715623425.json, 视频生成/图生视频/自用H3官流（单采极速文戏）_2108455375656804353.json, 视频生成/图生视频/自用H3官流（终极版）_2108147321883152385.json, 视频生成/图生视频/街舞表演视频制作_2106024930591731713.json, 视频生成/图生视频/黄色的大宝剑打斗流_2109476674894131202.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_149

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/人物替换工作流1_2115370839989383170.json、视频生成/图生视频/润哥教育IP数字人_H3_R2V_2111327138715623425.json、视频生成/图生视频/自用H3官流（单采极速文戏）_2108455375656804353.json、视频生成/图生视频/自用H3官流（终极版）_2108147321883152385.json、视频生成/图生视频/街舞表演视频制作_2106024930591731713.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `VAEDecodeAudio` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `BasicScheduler` —— 4/6 个有
- `ManualSigmas` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `VHS_LoadVideo` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `ExtendIntermediateSigmas` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `DisableNoise` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `MiniMaxH3Unified` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `SoundFlow_GetLength` —— 1/6 个有
- `SplitSigmasDenoise` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_sampler_unet_69
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.845667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3-多图参考生视频_2092494833108733954.json, 视频生成/图生视频/MiniMaxH3参考加速版自用_2092230388805619714.json, 视频生成/图生视频/MiniMaxH3多参MV生成工作流 By 像素幻想Lab_2087128116820013058.json, 视频生成/图生视频/MiniMax_H3_I2V_lora加速_2090796314308202498.json, 视频生成/图生视频/Minimax H3 高动态打斗模型，更稳更有冲击力！_2096240918440529922.json, 视频生成/图生视频/minimaxh3人物替换多人版工作流_2114864168745652226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_69

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3-多图参考生视频_2092494833108733954.json、视频生成/图生视频/MiniMaxH3参考加速版自用_2092230388805619714.json、视频生成/图生视频/MiniMaxH3多参MV生成工作流 By 像素幻想Lab_2087128116820013058.json、视频生成/图生视频/MiniMax_H3_I2V_lora加速_2090796314308202498.json、视频生成/图生视频/Minimax H3 高动态打斗模型，更稳更有冲击力！_2096240918440529922.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `LoadAudio` —— 3/6 个有
- `ModelPreviewOverrideKJ` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `MiniMaxLowVRAMAttention` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `BlockSparseAttention` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `MiniMaxH3ImageToVideo` —— 1/6 个有
- `SolAttnPatch` —— 1/6 个有
- `StringMergeNode` —— 1/6 个有
- `ZNGB_ResizeImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

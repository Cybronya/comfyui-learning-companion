---
name: unknown_workflow_video_sampler_unet_39
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5496
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda_2110543734483013634.json, 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json, 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json, 视频生成/图生视频/minimax_h3多图快速参考生视频_2110577324570796034.json, 视频生成/图生视频/minimax_ref_fl_低显存真实感工作流_2097518131697766402.json, 视频生成/图生视频/poster animation_2094321304538279938.json, 视频生成/图生视频/【傲雪AIGC】MiniMax+H3首尾帧生视频版_2093696527855341570.json, 视频生成/文生视频/MiniMax+H3文生视频_2089205361046810625.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094359561212882945.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094381288823287810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_39

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/minimax_h3_i2v_fastH3_v2_veda_2110543734483013634.json、视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json、视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json、视频生成/图生视频/minimax_h3多图快速参考生视频_2110577324570796034.json、视频生成/图生视频/minimax_ref_fl_低显存真实感工作流_2097518131697766402.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `ModelAttentionBackend` —— 7/10 个有
- `MiniMaxH3ImageToVideo` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `Text` —— 5/10 个有
- `BlockSparseAttention` —— 4/10 个有
- `VHS_LoadVideoFFmpeg` —— 4/10 个有
- `VedaSparseAttention` —— 4/10 个有
- `孤海注释` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `QwenH3PromptLocal` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `LayerUtility: TextJoin` —— 1/10 个有
- `MiniMaxChunkFeedForward` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `MiniMaxLowVRAMAttention` —— 1/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

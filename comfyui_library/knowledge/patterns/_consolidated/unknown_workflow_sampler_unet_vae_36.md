---
name: unknown_workflow_sampler_unet_vae_36
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.846143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json, 视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json, 视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json, 视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json, 视频生成/图生视频/minMax+H3+二采放大_2091513919167885314.json, 视频生成/图生视频/minimax h3_fi2va-dasiwa-zs05可选单图双采_2092267502540779521.json, 视频生成/图生视频/minimax h3_ref2va-dasiwa-zs05可选双采_2092257046572920834.json, 视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json, 视频生成/图生视频/【合理动态版】Hybrid_4+5步双采样_2096530913504088066.json, 视频生成/图生视频/【疯了的动态】Dasiwa_4+5步双采样_2096866880698015746.json, 视频生成/文生视频/MiniMax H3 FL2VA｜文生+首尾帧全能视频_2090027189914918914.json, 视频生成/文生视频/MiniMax H3 Ref2VA｜多参考全能视频生成_2090060185078419458.json, 视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json, 视频生成/文生视频/海螺H3-高效4步-脸部护持_2091172705780461570.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_36

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全能参考高清放大工作流_2110689506868424706.json、视频生成/图生视频/Minimax_H3_首帧锁定_固定全景_音色配对修正版_2108927308747857922.json、视频生成/图生视频/Minimax_h3_超级加速多图参考生视频_2084162807137918977.json、视频生成/图生视频/Singularity真实人物高质量双采工作流_2098389525570613249.json、视频生成/图生视频/minMax+H3+二采放大_2091513919167885314.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `PrimitiveFloat` —— 13/14 个有
- `PrimitiveStringMultiline` —— 13/14 个有
- `LTXVConcatAVLatent` —— 12/14 个有
- `LTXVSeparateAVLatent` —— 12/14 个有
- `MinimaxH3LatentUpscaler3D` —— 12/14 个有
- `VHS_VideoCombine` —— 12/14 个有
- `MiniMaxH3ReferenceToVideo` —— 10/14 个有
- `MiniMaxH3SigmaShift` —— 10/14 个有
- `ModelPreviewOverrideKJ` —— 10/14 个有
- `SplitSigmas` —— 10/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/14 个有
- `ModelAttentionBackend` —— 7/14 个有
- `ManualSigmas` —— 6/14 个有
- `CreateVideo` —— 5/14 个有
- `H3SigmaRefiner` —— 5/14 个有
- `LoadAudio` —— 5/14 个有
- `Label (rgthree)` —— 4/14 个有
- `MiniMaxH3ImageToVideo` —— 4/14 个有
- `SaveVideo` —— 4/14 个有
- `ImageResizeKJv2` —— 3/14 个有
- `LoraLoaderBypassModelOnly` —— 3/14 个有
- `easy showAnything` —— 3/14 个有
- `AudioCrop` —— 2/14 个有
- `StringFunction|pysssss` —— 2/14 个有
- `VHS_LoadVideo` —— 2/14 个有
- `FloatConstant` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `Int` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `MiniMaxChunkFeedForward` —— 1/14 个有
- `PainterVRAM` —— 1/14 个有
- `PathchSageAttentionKJ` —— 1/14 个有
- `RHLLMChatNode` —— 1/14 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/14 个有
- `easy int` —— 1/14 个有
- `忽略多组孤海` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

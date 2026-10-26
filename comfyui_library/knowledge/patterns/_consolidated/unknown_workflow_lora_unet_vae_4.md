---
name: unknown_workflow_lora_unet_vae_4
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.604333
common_nodes: [CLIPLoader, CreateVideo, GetNode, LoraLoaderModelOnly, ResolutionSelector, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采武戏直出_2101160593582546945.json, 视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采直出_2099477874922315778.json, 视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大1080P直出_2101166794710011905.json, 视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大武戏1080P直出_2101178415406731265.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大文戏工作流_2096179690426949633.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武器对决工作流_2096593027769913345.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武戏工作流_2096227914462355458.json, 视频生成/图生视频/Minimax H3双模双采工作流-小脸不崩-脸不油，高动态不崩脸_2093185884203085826.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3双模双采工作流_2091613369202724865.json, 视频生成/图生视频/小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091830576230780930.json, 视频生成/图生视频/海螺H3 小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091875924642975746.json, 视频生成/图生视频/短剧助手：MiniMax H3 双模双采资源面板加载生成视频_2093912808089014274.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采武戏直出_2101160593582546945.json、视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采直出_2099477874922315778.json、视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大1080P直出_2101166794710011905.json、视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大武戏1080P直出_2101178415406731265.json、视频生成/图生视频/MiniMax_H3_二次采样+放大文戏工作流_2096179690426949633.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `GetNode`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `BasicScheduler` —— 10/12 个有
- `LTXVConcatAVLatent` —— 10/12 个有
- `LTXVSeparateAVLatent` —— 10/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/12 个有
- `MinimaxH3LatentUpscaler3D` —— 10/12 个有
- `MiniMaxLowVRAMAttention` —— 9/12 个有
- `BasicGuider` —— 8/12 个有
- `CR Prompt Text` —— 8/12 个有
- `ComfyMathExpression` —— 8/12 个有
- `H3SigmaRefiner` —— 8/12 个有
- `KSamplerSelect` —— 8/12 个有
- `MiniMaxH3ReferenceToVideo` —— 8/12 个有
- `MiniMaxH3SigmaShift` —— 8/12 个有
- `ModelAttentionBackend` —— 8/12 个有
- `PrimitiveFloat` —— 8/12 个有
- `RandomNoise` —— 8/12 个有
- `SamplerCustomAdvanced` —— 8/12 个有
- `SplitSigmas` —— 8/12 个有
- `easy cleanGpuUsed` —— 7/12 个有
- `孤海注释` —— 7/12 个有
- `ModelPreviewOverrideKJ` —— 5/12 个有
- `H3AutoContextSampler` —— 4/12 个有
- `H3Parameter` —— 4/12 个有
- `H3SeamCorrection` —— 4/12 个有
- `ImageResizeKJv2` —— 4/12 个有
- `PrimitiveStringMultiline` —— 4/12 个有
- `ExtendIntermediateSigmas` —— 2/12 个有
- `PathchSageAttentionKJ` —— 2/12 个有
- `SolAttnPatch` —— 2/12 个有
- `SplitSigmasDenoise` —— 2/12 个有
- `Anything Everywhere` —— 1/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `DF_Integer` —— 1/12 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/12 个有
- `MiniMaxH3ReferenceSplitter` —— 1/12 个有
- `StringConcatenate` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

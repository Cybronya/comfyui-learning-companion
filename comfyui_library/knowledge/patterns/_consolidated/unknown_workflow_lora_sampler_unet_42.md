---
name: unknown_workflow_lora_sampler_unet_42
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.534
common_nodes: [CLIPLoader, CR Prompt Text, CreateVideo, GetNode, H3AutoContextSampler, H3Parameter, H3SeamCorrection, ImageResizeKJv2, LoadImage, LoraLoaderModelOnly, MiniMaxLowVRAMAttention, ResolutionSelector, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采武戏直出_2101160593582546945.json, 视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采直出_2099477874922315778.json, 视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大1080P直出_2101166794710011905.json, 视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大武戏1080P直出_2101178415406731265.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采武戏直出_2101160593582546945.json、视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频单采直出_2099477874922315778.json、视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大1080P直出_2101166794710011905.json、视频生成/图生视频/MiniMax_H3_AutoContext_无限时长视频双采放大武戏1080P直出_2101178415406731265.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `CreateVideo`
- `GetNode`
- `H3AutoContextSampler`
- `H3Parameter`
- `H3SeamCorrection`
- `ImageResizeKJv2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxLowVRAMAttention`
- `ResolutionSelector`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/4 个有
- `H3SigmaRefiner` —— 2/4 个有
- `LTXVConcatAVLatent` —— 2/4 个有
- `LTXVSeparateAVLatent` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `MinimaxH3LatentUpscaler3D` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `SolAttnPatch` —— 2/4 个有
- `SplitSigmas` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

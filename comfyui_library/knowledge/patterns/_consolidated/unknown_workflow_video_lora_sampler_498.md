---
name: unknown_workflow_video_lora_sampler_498
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9145
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyMiniMaxH3LatentAV, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AddGuide, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3高清质感修复_2099337648761565185.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098937759426760705.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098995425230540801.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2099670789904748546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_498

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax H3高清质感修复_2099337648761565185.json、视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098937759426760705.json、视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098995425230540801.json、视频生成/文生视频/MiniMax_H3_LMS视频高清化_2099670789904748546.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyMiniMaxH3LatentAV`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AddGuide`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SolAttnMiniMax` —— 3/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `ComfyNumberConvert` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

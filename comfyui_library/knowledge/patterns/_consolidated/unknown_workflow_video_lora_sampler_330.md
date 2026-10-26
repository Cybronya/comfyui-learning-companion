---
name: unknown_workflow_video_lora_sampler_330
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.861143
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyMiniMaxH3LatentAV, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [图片生成/图生图/Qwen2511-多角度_2099391040628281345.json, 图片生成/文生图/Minimax_H3去模糊+纹理增强_2098941039192137730.json, 图片生成/文生图/Minimax_H3去模糊+纹理增强_2099053048344694785.json, 视频生成/图生视频/Minimax H3高清质感修复_2099337648761565185.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098937759426760705.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098995425230540801.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2099670789904748546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_330

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen2511-多角度_2099391040628281345.json、图片生成/文生图/Minimax_H3去模糊+纹理增强_2098941039192137730.json、图片生成/文生图/Minimax_H3去模糊+纹理增强_2099053048344694785.json、视频生成/图生视频/Minimax H3高清质感修复_2099337648761565185.json、视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098937759426760705.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `MiniMaxH3AddGuide`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 6/7 个有
- `MiniMaxLowVRAMAttention` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `EmptyImage` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `ResolutionSelector` —— 4/7 个有
- `ComfyMathExpression` —— 3/7 个有
- `ComfyNumberConvert` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/7 个有
- `ModelPreviewOverrideKJ` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `SolAttnMiniMax` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `GetNode` —— 1/7 个有
- `Int` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

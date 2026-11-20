---
name: unknown_workflow_video_lora_sampler_114
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.8985
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyMiniMaxH3LatentAV, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [图片生成/图生图/Qwen2511-多角度_2099391040628281345.json, 图片生成/文生图/Minimax_H3去模糊+纹理增强_2098941039192137730.json, 图片生成/文生图/Minimax_H3去模糊+纹理增强_2099053048344694785.json, 平台全量/MiniMax H3 LMS 视频高清修复_2099341401883500545.json, 平台全量/MiniMax H3 LMS视频高清修复_2098073937149259778.json, 平台全量/MiniMax H3 LMS视频高清修复_2100229192171479041.json, 平台全量/MiniMax H3 LMS视频高清化_2097922828384428034.json, 平台全量/MiniMax_H3_LMS视频高清化_2100395231102459905.json, 平台全量/MiniMax_H3_LMS视频高清化_2100426441103077378.json, 平台全量/Minimax H3去模糊+纹理增强_2097625225021181953.json, 平台全量/Minimax H3去模糊+纹理增强_2098316377571553281.json, 平台全量/MinimaxH3纹理增强_2099037514819530754.json, 视频生成/图生视频/Minimax H3高清质感修复_2099337648761565185.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098937759426760705.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2098995425230540801.json, 视频生成/文生视频/MiniMax_H3_LMS视频高清化_2099670789904748546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_114

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen2511-多角度_2099391040628281345.json、图片生成/文生图/Minimax_H3去模糊+纹理增强_2098941039192137730.json、图片生成/文生图/Minimax_H3去模糊+纹理增强_2099053048344694785.json、平台全量/MiniMax H3 LMS 视频高清修复_2099341401883500545.json、平台全量/MiniMax H3 LMS视频高清修复_2098073937149259778.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
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
- `MiniMaxChunkFeedForward` —— 15/16 个有
- `MiniMaxLowVRAMAttention` —— 15/16 个有
- `PrimitiveStringMultiline` —— 15/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/16 个有
- `SolAttnMiniMax` —— 9/16 个有
- `ResolutionSelector` —— 7/16 个有
- `ComfyMathExpression` —— 6/16 个有
- `ComfyNumberConvert` —— 6/16 个有
- `ModelPreviewOverrideKJ` —— 6/16 个有
- `PrimitiveInt` —— 6/16 个有
- `easy showAnything` —— 5/16 个有
- `EmptyImage` —— 4/16 个有
- `PreviewImage` —— 4/16 个有
- `PreviewAny` —— 2/16 个有
- `GetNode` —— 1/16 个有
- `Int` —— 1/16 个有
- `MathExpression|pysssss` —— 1/16 个有
- `SetNode` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

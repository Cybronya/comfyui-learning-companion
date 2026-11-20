---
name: unknown_workflow_video_upscale_latent_upscale_43
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.442778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy float, 忽略多组孤海]
problems: []
missing: []
members: [平台全量/视频动作迁移_自动横竖屏_720p480p_24fps_2106556243405004802.json, 数字人/数字人/H3二采_2111323289078550530.json, 数字人/数字人/MiniMax H3-多参考生视频-优化版_2111992528827412482.json, 数字人/数字人/视频编辑-替换视频中的元素_2114576787442327553.json, 视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！_2107500379746430977.json, 视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！_2113553458224783362.json, 视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！加放大_2110238781872889857.json, 视频生成/图生视频/视频动作迁移_自动横竖屏_720p480p_24fps_2114902280364449794.json, 视频生成/图生视频/视频动作迁移_自动横竖屏_720p480p_24fps_2115222225719742466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_43

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/视频动作迁移_自动横竖屏_720p480p_24fps_2106556243405004802.json、数字人/数字人/H3二采_2111323289078550530.json、数字人/数字人/MiniMax H3-多参考生视频-优化版_2111992528827412482.json、数字人/数字人/视频编辑-替换视频中的元素_2114576787442327553.json、视频生成/图生视频/H3动作迁移2.0！进阶版，史诗强化！_2107500379746430977.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy float`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `PrimitiveFloat` —— 5/9 个有
- `ImageScale` —— 3/9 个有
- `PrimitiveBoolean` —— 3/9 个有
- `VHS_VideoInfo` —— 3/9 个有
- `PreviewImage` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `GH_AudioVideoMerger` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `ImageBatch` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `LoadImageFromUrl` —— 1/9 个有
- `ModelAttentionBackend` —— 1/9 个有
- `RepeatImageBatch` —— 1/9 个有
- `SeedVR2LoadDiTModel` —— 1/9 个有
- `SeedVR2LoadVAEModel` —— 1/9 个有
- `SeedVR2VideoUpscaler` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

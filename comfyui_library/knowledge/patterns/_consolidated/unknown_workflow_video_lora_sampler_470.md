---
name: unknown_workflow_video_lora_sampler_470
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91925
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, H3InjectVideoLatent, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3NativeAudioLock, MiniMaxH3SigmaShift, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/无限长视频生成 3 高清f放大 1080P MiniMax H3_2090714008914587649.json, 视频生成/图生视频/MiniMax H3｜通用视频二阶高清重绘_2090290098544930818.json, 视频生成/文生视频/MiniMax H3｜通用视频二阶高清重绘_2089986546912030722.json, 视频生成/文生视频/MiniMax+H3+万能视频高清重绘｜一键生成式放大_2088992117300482049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_470

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/无限长视频生成 3 高清f放大 1080P MiniMax H3_2090714008914587649.json、视频生成/图生视频/MiniMax H3｜通用视频二阶高清重绘_2090290098544930818.json、视频生成/文生视频/MiniMax H3｜通用视频二阶高清重绘_2089986546912030722.json、视频生成/文生视频/MiniMax+H3+万能视频高清重绘｜一键生成式放大_2088992117300482049.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `H3InjectVideoLatent`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3NativeAudioLock`
- `MiniMaxH3SigmaShift`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 3/4 个有
- `LTXVConcatAVLatent` —— 3/4 个有
- `LTXVSeparateAVLatent` —— 3/4 个有
- `LoadVideoUI` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `MinimaxH3LatentUpscaler3D` —— 2/4 个有
- `DiffusionModelLoaderKJ` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有
- `Yuan_RTXVideoUpscaleH3` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_419
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.938429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, H3InjectVideoLatent, H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3NativeAudioLock, MiniMaxH3SigmaShift, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MiniMax H3｜通用视频二阶高清重绘（不用传提示词和素材）_2103366092113670145.json, 平台全量/MiniMax_H3｜通用视频二阶高清重绘不用传提示词和素材_2105588554083684353.json, 平台全量/MiniMax_H3｜通用视频二阶高清重绘不用传提示词和素材_2108375850503729154.json, 数字人/数字人/无限长视频生成 3 高清f放大 1080P MiniMax H3_2090714008914587649.json, 视频生成/图生视频/MiniMax H3｜通用视频二阶高清重绘_2090290098544930818.json, 视频生成/文生视频/MiniMax H3｜通用视频二阶高清重绘_2089986546912030722.json, 视频生成/文生视频/MiniMax+H3+万能视频高清重绘｜一键生成式放大_2088992117300482049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_419

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/MiniMax H3｜通用视频二阶高清重绘（不用传提示词和素材）_2103366092113670145.json、平台全量/MiniMax_H3｜通用视频二阶高清重绘不用传提示词和素材_2105588554083684353.json、平台全量/MiniMax_H3｜通用视频二阶高清重绘不用传提示词和素材_2108375850503729154.json、数字人/数字人/无限长视频生成 3 高清f放大 1080P MiniMax H3_2090714008914587649.json、视频生成/图生视频/MiniMax H3｜通用视频二阶高清重绘_2090290098544930818.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
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
- `GetImageSizeAndCount` —— 6/7 个有
- `LTXVConcatAVLatent` —— 6/7 个有
- `LTXVSeparateAVLatent` —— 6/7 个有
- `LoadVideoUI` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `MinimaxH3LatentUpscaler3D` —— 5/7 个有
- `DiffusionModelLoaderKJ` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `Yuan_RTXVideoUpscaleH3` —— 1/7 个有
- `easy imageSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_upscale_latent_upscale_98
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.5215
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【Minimax H3】人物替换，_2112811927469641730.json, 视频生成/文生视频/0905万象+动漫短剧文戏（12秒横屏）_2096159965277933569.json, 视频生成/文生视频/0905万象+动漫短剧文戏（12秒竖屏）_2096418321116786689.json, 视频生成/文生视频/1-Aiden-MiniMax-H3-疯狂测试工作流！！！！_2093054855547015170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_98

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/【Minimax H3】人物替换，_2112811927469641730.json、视频生成/文生视频/0905万象+动漫短剧文戏（12秒横屏）_2096159965277933569.json、视频生成/文生视频/0905万象+动漫短剧文戏（12秒竖屏）_2096418321116786689.json、视频生成/文生视频/1-Aiden-MiniMax-H3-疯狂测试工作流！！！！_2093054855547015170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `easy float` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `MiniMaxChunkFeedForward` —— 2/4 个有
- `MiniMaxLowVRAMAttention` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `忽略多组孤海` —— 2/4 个有
- `AudioCrop` —— 1/4 个有
- `BlockSparseAttention` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `InversionDemoLazyIndexSwitch` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有
- `easy indexTTSForceCleanup` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy positive` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

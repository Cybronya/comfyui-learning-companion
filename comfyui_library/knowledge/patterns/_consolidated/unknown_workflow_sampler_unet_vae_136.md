---
name: unknown_workflow_sampler_unet_vae_136
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.839625
common_nodes: [BasicGuider, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2097993945132388353.json, 视频生成/图生视频/4-9宫图+Minimaxh3导演台（批量短剧专用）_2099703771608735745.json, 视频生成/图生视频/AI短剧制作全流程_2111223881188077570.json, 视频生成/图生视频/BUNNY_H3_单采_er_sde_手动Sigma_2109936169202049026.json, 视频生成/图生视频/H3_打斗工作流_2102828840786681857.json, 视频生成/图生视频/H3_打斗工作流_2105855489631408129.json, 视频生成/图生视频/MiniMax+H3-9.2_2095010503541215234.json, 视频生成/图生视频/黄色的大宝剑打斗流_2109476674894131202.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_136

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2097993945132388353.json、视频生成/图生视频/4-9宫图+Minimaxh3导演台（批量短剧专用）_2099703771608735745.json、视频生成/图生视频/AI短剧制作全流程_2111223881188077570.json、视频生成/图生视频/BUNNY_H3_单采_er_sde_手动Sigma_2109936169202049026.json、视频生成/图生视频/H3_打斗工作流_2102828840786681857.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `ComfyMathExpression` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `CreateVideo` —— 5/8 个有
- `ModelAttentionBackend` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `DisableNoise` —— 4/8 个有
- `ExtendIntermediateSigmas` —— 4/8 个有
- `SplitSigmasDenoise` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `INTConstant` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `LoraLoaderBypassModelOnly` —— 3/8 个有
- `MiniMaxH3SigmaShift` —— 3/8 个有
- `SolAttnMiniMax` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `ResizeShortestToNode` —— 2/8 个有
- `SFH3MultimodalDirector` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `BlockSparseAttention` —— 1/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `ManualSigmas` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

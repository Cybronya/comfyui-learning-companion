---
name: unknown_workflow_lora_sampler_unet_28
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.813
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3_打斗工作流_2102828840786681857.json, 视频生成/图生视频/H3_打斗工作流_2105855489631408129.json, 视频生成/图生视频/MiniMax+H3-9.2_2095010503541215234.json, 视频生成/图生视频/Minimax H3-最佳动态战斗版V2_2096214859611467777.json, 视频生成/图生视频/minimax   h3 最强动作迁移_2089285244263424001.json, 视频生成/图生视频/黄色的大宝剑打斗流_2109476674894131202.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_28

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3_打斗工作流_2102828840786681857.json、视频生成/图生视频/H3_打斗工作流_2105855489631408129.json、视频生成/图生视频/MiniMax+H3-9.2_2095010503541215234.json、视频生成/图生视频/Minimax H3-最佳动态战斗版V2_2096214859611467777.json、视频生成/图生视频/minimax   h3 最强动作迁移_2089285244263424001.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisableNoise` —— 5/6 个有
- `ExtendIntermediateSigmas` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `ModelAttentionBackend` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `SplitSigmasDenoise` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `ModelPreviewOverrideKJ` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `SolAttnMiniMax` —— 3/6 个有
- `INTConstant` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `ResizeShortestToNode` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `BlockSparseAttention` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `MiniMaxH3AddGuide` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `UniBlockSwapTE` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_sampler_unet_23
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.466538
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/8步加速官流_2108935132144037890.json, 视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)_2084210400207396866.json, 视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)真人短剧加速版_2084291490649567233.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+图生视频+1280分辨率加速流_2085330041017298945.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+（首帧）_2084283095339065346.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085589980080070658.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考+数字人+人物音频一致性_2086164860592807937.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+全能参考（1280分辨率）加速流_2085330061422579714.json, 视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json, 视频生成/图生视频/H3极速测试工作流_2109473161694760961.json, 视频生成/图生视频/MiniMax H3-单采_2102816230406189058.json, 视频生成/图生视频/MiniMax-H3-FastVideo多参极速版_2108479598177636354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/8步加速官流_2108935132144037890.json、视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)_2084210400207396866.json、视频生成/图生视频/AITUDOU-MiniMax H3(全能参考)真人短剧加速版_2084291490649567233.json、视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+图生视频+1280分辨率加速流_2085330041017298945.json、视频生成/图生视频/AITUDOU-MiniMax+H3+I2V+（首帧）_2084283095339065346.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 12/13 个有
- `GetNode` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `MiniMaxH3ReferenceToVideo` —— 11/13 个有
- `Label (rgthree)` —— 10/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/13 个有
- `Text` —— 9/13 个有
- `LoraLoaderModelOnly` —— 7/13 个有
- `PrimitiveFloat` —— 7/13 个有
- `ModelAttentionBackend` —— 5/13 个有
- `BlockSparseAttention` —— 4/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `Float` —— 3/13 个有
- `SigmasGraph` —— 3/13 个有
- `easy float` —— 3/13 个有
- `LoadAudio` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `EasyCache` —— 1/13 个有
- `ExtendIntermediateSigmas` —— 1/13 个有
- `H3SigmaRefiner` —— 1/13 个有
- `ManualSigmas` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `ZNGB_AudioCrop` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

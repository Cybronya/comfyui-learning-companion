---
name: unknown_workflow_video_sampler_unet_44
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7124
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/minimax_h3_i2v_fastH3_v2_veda_2117793830861885441.json, 平台全量/minimax_h3_rawmodel_veta_attention_ref2va_2117791616260988929.json, 平台全量/minimax多参生视频加速版_2117539612058017794.json, 平台全量/minimax长视频工作流_2117531904999256065.json, 平台全量/单人口播_2119742441938055169.json, 视频生成/图生视频/H3 超级打戏无损工作流_2110310649992663042.json, 视频生成/图生视频/H3_单采极速文戏_2106860537857527810.json, 视频生成/图生视频/H3_单采极速文戏_2109821779844886530.json, 视频生成/图生视频/H3无损融合单采-8参考图+视频尾帧（保持视频连贯）_2109104328920354818.json, 视频生成/图生视频/MiniMax_H3双采全能工作流V3-语义桥-文戏不油，武戏动态强-参考生视频-长视频-视频复刻-高清直出_2113557786440327170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_44

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/minimax_h3_i2v_fastH3_v2_veda_2117793830861885441.json、平台全量/minimax_h3_rawmodel_veta_attention_ref2va_2117791616260988929.json、平台全量/minimax多参生视频加速版_2117539612058017794.json、平台全量/minimax长视频工作流_2117531904999256065.json、平台全量/单人口播_2119742441938055169.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `ModelAttentionBackend` —— 9/10 个有
- `BlockSparseAttention` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `LoadAudio` —— 6/10 个有
- `MiniMaxH3SigmaShift` —— 6/10 个有
- `ModelPreviewOverrideKJ` —— 6/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `ExtendIntermediateSigmas` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `ManualSigmas` —— 3/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `忽略多组孤海` —— 3/10 个有
- `EmptyImage` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `Text Multiline` —— 2/10 个有
- `VedaSparseAttention` —— 2/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `GetLastFrameNode` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MiniMaxH3AddGuide` —— 1/10 个有
- `MiniMaxH3ImageToVideo` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

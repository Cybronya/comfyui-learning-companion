---
name: unknown_workflow_video_sampler_vae_30
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.944083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, Text, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497.json, 视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json, 视频生成/图生视频/MinimaxH3八步加速极速版T1_2088232222376681473.json, 视频生成/图生视频/minimaxH3先锋艺术_2088544149321633794.json, 视频生成/图生视频/minimaxH3多参提示词优化_2086425483746566146.json, 视频生成/图生视频/minimaxh3-三图参考生视频-15秒动作科幻题材_2097201624564457473.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词T10_2085752202936803329.json, 视频生成/图生视频/创意广告_2087007696313733122.json, 视频生成/图生视频/图生视频提示词自动填充_2086756092205428737.json, 视频生成/图生视频/图生视频提示词运镜_2086862647512879105.json, 视频生成/图生视频/图生视频电影质感_2087837157028352001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497.json、视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530.json、视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json、视频生成/图生视频/MinimaxH3八步加速极速版T1_2088232222376681473.json、视频生成/图生视频/minimaxH3先锋艺术_2088544149321633794.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/12 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 10/12 个有
- `ImageConcatenateMulti_UTK` —— 9/12 个有
- `ComfyMathExpression` —— 8/12 个有
- `PreviewImage` —— 8/12 个有
- `PrimitiveFloat` —— 8/12 个有
- `UNETLoader` —— 7/12 个有
- `EnhancedLoadDiffusionModel` —— 5/12 个有
- `LoraLoaderBypassModelOnly` —— 5/12 个有
- `CreateVideo` —— 2/12 个有
- `Int` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `LoraLoaderModelOnly` —— 2/12 个有
- `MiniMaxH3ImageToVideo` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `Images to RGB` —— 1/12 个有
- `InspyrenetRembg` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_102
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.626
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3-「电商」-多参生视频_2091522221620686850.json, 视频生成/图生视频/MinimaxH3参考生成视频工作流_2084154580937564162.json, 视频生成/图生视频/miniMAXH3全能参考_2084803672076279809.json, 视频生成/图生视频/minimax_h3_lightx2v正式版 参考模式_2085761824204607490.json, 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json, 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json, 视频生成/图生视频/minimax_h3多图快速参考生视频_2110577324570796034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_102

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3-「电商」-多参生视频_2091522221620686850.json、视频生成/图生视频/MinimaxH3参考生成视频工作流_2084154580937564162.json、视频生成/图生视频/miniMAXH3全能参考_2084803672076279809.json、视频生成/图生视频/minimax_h3_lightx2v正式版 参考模式_2085761824204607490.json、视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `CreateVideo` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `BlockSparseAttention` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `VedaSparseAttention` —— 3/7 个有
- `QwenH3PromptLocal` —— 2/7 个有
- `LazySwitch1way` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy boolean` —— 1/7 个有
- `easy saveText` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

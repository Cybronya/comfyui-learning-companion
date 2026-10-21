---
name: unknown_workflow_sampler_unet_vae_53
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.835818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086413769206489090.json, 视频生成/文生视频/MiniMax H3 文生视频（开源版）_2084993426063450113.json, 视频生成/文生视频/MiniMax H3_fl2v_lightx2v_turbo_4step_v0.1_2085726831755481090.json, 视频生成/文生视频/MiniMax H3_文生视频工作流_2084504955460866050.json, 视频生成/文生视频/MiniMax H3图生视频（支持文生视频，首_尾帧生成）_2084161667742654466.json, 视频生成/文生视频/MiniMax H3多图参考生视频（速度提升2倍+提示词自动优化）_2086492553964253185.json, 视频生成/文生视频/多图参考生视频（速度提升2倍+提示词自动优化）_2086268908348207105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_53

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086413769206489090.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
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
- `MiniMaxH3ImageToVideo` —— 9/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/11 个有
- `LoadImage` —— 5/11 个有
- `LoraLoaderBypassModelOnly` —— 3/11 个有
- `MiniMaxH3BlockCacheT8` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `MiniMaxH3ReferenceToVideo` —— 2/11 个有
- `RHLLMChatNode` —— 2/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `Text Multiline` —— 2/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `PlaySound|pysssss` —— 1/11 个有
- `ResizeImagesByLongerEdge` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `VHS_VideoCombine` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

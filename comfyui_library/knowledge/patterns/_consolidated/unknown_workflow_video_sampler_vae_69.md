---
name: unknown_workflow_video_sampler_vae_69
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.848
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_I2V_lora加速_2090796314308202498.json, 视频生成/图生视频/MiniMax_H3图生视频V1_2087430143055847430.json, 视频生成/图生视频/Minimax H3 - 图生视频-首尾帧视频_2095067656989798402.json, 视频生成/图生视频/Minimax H3 图生视频_2084264368950304769.json, 视频生成/图生视频/Minimax H3 首尾帧_2089249903888392193.json, 视频生成/图生视频/minimax_ref_fl_低显存真实感工作流_2097518131697766402.json, 视频生成/图生视频/角色PV动画制作_2096613890909102081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_69

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_I2V_lora加速_2090796314308202498.json、视频生成/图生视频/MiniMax_H3图生视频V1_2087430143055847430.json、视频生成/图生视频/Minimax H3 - 图生视频-首尾帧视频_2095067656989798402.json、视频生成/图生视频/Minimax H3 图生视频_2084264368950304769.json、视频生成/图生视频/Minimax H3 首尾帧_2089249903888392193.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `MiniMaxH3ImageToVideo` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `ResolutionSelector` —— 4/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `H3SigmaRefiner` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `MiniMaxChunkFeedForward` —— 2/7 个有
- `MiniMaxH3ReferenceToVideo` —— 2/7 个有
- `MiniMaxLowVRAMAttention` —— 2/7 个有
- `SolAttnPatch` —— 2/7 个有
- `DiffusionModelLoaderKJ` —— 1/7 个有
- `JsonExtractString` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `RegexReplace` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `StringConcatenate` —— 1/7 个有
- `TextGenerate` —— 1/7 个有
- `ZNGB_ResizeImage` —— 1/7 个有
- `easy convertAnything` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

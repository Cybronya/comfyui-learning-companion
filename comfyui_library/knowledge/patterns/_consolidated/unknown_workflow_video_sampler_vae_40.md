---
name: unknown_workflow_video_sampler_vae_40
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8039
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_I2V_lora加速_2090796314308202498.json, 视频生成/图生视频/MiniMax_H3图生视频V1_2087430143055847430.json, 视频生成/图生视频/Minimax H3 - 图生视频-首尾帧视频_2095067656989798402.json, 视频生成/图生视频/Minimax H3 图生视频_2084264368950304769.json, 视频生成/图生视频/Minimax H3 图生视频｜冻结时间 360 环绕、首尾画面循环闭环｜+ HyperFlow 8 步 LoRA_2104492606691569665.json, 视频生成/图生视频/minimax_ref_fl_低显存真实感工作流_2097518131697766402.json, 视频生成/文生视频/MiniMax H3 FL2VA 三阶极致放大｜2K生成式精修_2088625693134512130.json, 视频生成/文生视频/MiniMax H3 Ref2VA 二阶超清重绘｜多参考精修_2088888730617729025.json, 视频生成/文生视频/MiniMax+H3+FL2VA+二阶超清放大｜首尾帧精修_2089240886684250114.json, 视频生成/文生视频/MiniMax+H3+Ref2VA+三阶极致重绘｜2K多参考精修_2089240711672713217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_40

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_I2V_lora加速_2090796314308202498.json、视频生成/图生视频/MiniMax_H3图生视频V1_2087430143055847430.json、视频生成/图生视频/Minimax H3 - 图生视频-首尾帧视频_2095067656989798402.json、视频生成/图生视频/Minimax H3 图生视频_2084264368950304769.json、视频生成/图生视频/Minimax H3 图生视频｜冻结时间 360 环绕、首尾画面循环闭环｜+ HyperFlow 8 步 LoRA_2104492606691569665.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `ResolutionSelector` —— 8/10 个有
- `MiniMaxH3ImageToVideo` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `MiniMaxChunkFeedForward` —— 6/10 个有
- `MiniMaxLowVRAMAttention` —— 6/10 个有
- `ModelAttentionBackend` —— 6/10 个有
- `H3SigmaRefiner` —— 5/10 个有
- `MiniMaxH3SigmaShift` —— 5/10 个有
- `GetImageSizeAndCount` —— 4/10 个有
- `LTXVConcatAVLatent` —— 4/10 个有
- `LTXVSeparateAVLatent` —— 4/10 个有
- `Yuan_RTXVideoUpscaleH3` —— 4/10 个有
- `easy int` —— 4/10 个有
- `MiniMaxH3ReferenceToVideo` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `MiniMaxH3HybridLoader` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `VAEEncode` —— 2/10 个有
- `DiffusionModelLoaderKJ` —— 1/10 个有
- `ImagePadForOutpaint` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有
- `ZNGB_ResizeImage` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

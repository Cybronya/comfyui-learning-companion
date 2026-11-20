---
name: unknown_workflow_sampler_unet_vae_45
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.832176
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/自动视频参考_2086895012629016578.json, 平台全量/视频人物替换 视频参考生视频 minimax h3_2086293360792399874.json, 视频生成/图生视频/MINIMAX-H3 多参工作流 4步加速 官方Skills提示词模板_2086360900784709633.json, 视频生成/图生视频/MINIMAX-H3 多参工作流包含加速流程和完美克隆音频最终版_2087190952204132354.json, 视频生成/图生视频/MINIMAX-H3 多图生成视频_2085523161088610305.json, 视频生成/图生视频/MINIMAX-H3-图片加音频参考生视频-有提示词模板-int8和fp8_2084515925415522306.json, 视频生成/图生视频/MINIMAX-H3_2084691718737317889.json, 视频生成/图生视频/MINIMAX-H3_多图参考生视频_2084844223446208514.json, 视频生成/图生视频/MINIMAX-H3_多图参考生视频_2115633910469189633.json, 视频生成/图生视频/MiniMax H3 4图生视频+音频接入_2090184072877395969.json, 视频生成/图生视频/MiniMax H3 R2V comfyorg_2085736828308643841.json, 视频生成/图生视频/MiniMax H3 R2V-8步 comfyorg_2087532854384349186.json, 视频生成/图生视频/MiniMax H3 Ref2VA多图参考生视频_2053733634456207362.json, 视频生成/图生视频/MiniMax H3 【参考图+参考音频】4步生视频_2090646084061323265.json, 视频生成/图生视频/MiniMax H3 多参考生视频 8步加速版_2084190473446580225.json, 视频生成/图生视频/MiniMax H3 音频驱动（数字人）唱歌视频_2084544809620041730.json, 视频生成/文生视频/【Gensor-AI】MINIMAX-H3工作流合集【加速版】_2085550246054162433.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_45

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（平台全量/自动视频参考_2086895012629016578.json、平台全量/视频人物替换 视频参考生视频 minimax h3_2086293360792399874.json、视频生成/图生视频/MINIMAX-H3 多参工作流 4步加速 官方Skills提示词模板_2086360900784709633.json、视频生成/图生视频/MINIMAX-H3 多参工作流包含加速流程和完美克隆音频最终版_2087190952204132354.json、视频生成/图生视频/MINIMAX-H3 多图生成视频_2085523161088610305.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 16/17 个有
- `VAEDecodeAudio` —— 16/17 个有
- `PrimitiveFloat` —— 15/17 个有
- `LoadAudio` —— 14/17 个有
- `PrimitiveStringMultiline` —— 14/17 个有
- `CreateVideo` —— 13/17 个有
- `SaveVideo` —— 13/17 个有
- `LoraLoaderModelOnly` —— 10/17 个有
- `JjkText` —— 8/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/17 个有
- `VHS_LoadVideo` —— 7/17 个有
- `VHS_VideoCombine` —— 5/17 个有
- `Fast Groups Bypasser (rgthree)` —— 3/17 个有
- `MiniMaxH3SigmaShift` —— 3/17 个有
- `PreviewAny` —— 3/17 个有
- `VHS_VideoInfo` —— 2/17 个有
- `ImageScaleToTotalPixels` —— 1/17 个有
- `PathchSageAttentionKJ` —— 1/17 个有
- `PrimitiveInt` —— 1/17 个有
- `RHLLMChatNode` —— 1/17 个有
- `SolAttnPatch` —— 1/17 个有
- `TrimAudioDuration` —— 1/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_lora_sampler_vae_12
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.686
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧参考生成视频_MiniMax H3 FL2VA_2084119812443299842.json, 视频生成/图生视频/首尾帧参考生视频 无色差版 Minimax H3_2088976531933712385.json, 视频生成/文生视频/10ErosMax test4 对比测试_2087783168324759554.json, 视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json, 视频生成/文生视频/全能参考二次采样_MInimaxH3_2090972732266733570.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频工作流_2086348400169148418.json, 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/首尾帧参考生成视频_MiniMax H3 FL2VA_2084119812443299842.json、视频生成/图生视频/首尾帧参考生视频 无色差版 Minimax H3_2088976531933712385.json、视频生成/文生视频/10ErosMax test4 对比测试_2087783168324759554.json、视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json、视频生成/文生视频/全能参考二次采样_MInimaxH3_2090972732266733570.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 6/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `MiniMaxH3SigmaShift` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `UNETLoader` —— 4/7 个有
- `MiniMaxH3HybridLoader` —— 3/7 个有
- `MiniMaxH3ReferenceToVideo` —— 3/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 2/7 个有
- `H3SigmaRefiner` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `LTXVConcatAVLatent` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `孤海注释` —— 2/7 个有
- `忽略多组孤海` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `H3LatentUpscaleByJingchen573` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/7 个有
- `MinimaxH3LatentUpscaler3D` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有
- `SplitSigmas` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

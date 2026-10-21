---
name: unknown_workflow_sampler_unet_vae_67
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7674
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧参考生成视频_MiniMax H3 FL2VA_2084119812443299842.json, 视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json, 视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V3_2086292004803276802.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V4_2084169977384497154.json, 视频生成/文生视频/MiniMax H3 Ref2VA 剧本直出｜六段式自动生成+自动校验 · 9图参考成片 · H3原生音画同步版_2088206128625840130.json, 视频生成/文生视频/Minimax H3 多参生视频_2087727061006901250.json, 视频生成/文生视频/Minimax h3 4 步 lora2 加速版_2092076952441151490.json, 视频生成/文生视频/Minimax-h3-文生视频_2084913245437128706.json, 视频生成/文生视频/迄今超强MiniMax-H3文生视频！2倍速！量化加速官方8步Lora再提速50%_1926516021497335809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_67

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/首尾帧参考生成视频_MiniMax H3 FL2VA_2084119812443299842.json、视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json、视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json、视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V3_2086292004803276802.json、视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V4_2084169977384497154.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo` —— 7/10 个有
- `LoadImage` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `MiniMaxH3BlockCacheT8` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `GetNode` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `MiniMaxH3ReferenceToVideo` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

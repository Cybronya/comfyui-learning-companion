---
name: unknown_workflow_sampler_unet_vae_184
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.71
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json, 视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json, 视频生成/文生视频/H3-文生视频_2088176717721591810.json, 视频生成/文生视频/H3_海螺_官方-文生API反推_2086103276034027521.json, 视频生成/文生视频/Minimax-h3-文生视频_2084913245437128706.json, 视频生成/文生视频/MinimaxH3-文生视频（高质量）_2085617922352963586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_184

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json、视频生成/文生视频/H3+Krea2-H3-Style-LoRA对比测试_2087900017330843650.json、视频生成/文生视频/H3-文生视频_2088176717721591810.json、视频生成/文生视频/H3_海螺_官方-文生API反推_2086103276034027521.json、视频生成/文生视频/Minimax-h3-文生视频_2084913245437128706.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `EasyCache` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `RHLLMChatNode` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `StringFunction|pysssss` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

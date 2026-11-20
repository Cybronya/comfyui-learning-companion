---
name: unknown_workflow_lora_sampler_unet_238
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85025
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json, 视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json, 视频生成/文生视频/Minimax_h3_超级加速文生视频_2084160987023896578.json, 视频生成/文生视频/海螺H3 文生视频-提示词自动优化扩写_2086430630488924162.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_238

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json、视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json、视频生成/文生视频/Minimax_h3_超级加速文生视频_2084160987023896578.json、视频生成/文生视频/海螺H3 文生视频-提示词自动优化扩写_2086430630488924162.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
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
- `CR Text` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `EasyCache` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `PainterVRAM` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `Text Find and Replace` —— 1/4 个有
- `TextOverlay` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

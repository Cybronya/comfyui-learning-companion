---
name: unknown_workflow_lora_sampler_unet_123
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.851833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json, 视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json, 视频生成/文生视频/Minimax H3 文生视频 8步加速Lora+sage双重加速工作流_2089325283299119105.json, 视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速工作流_2084217093255421954.json, 视频生成/文生视频/海螺H3 文生视频-提示词自动优化扩写_2086430630488924162.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_123

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json、视频生成/文生视频/Minimax H3 -  文生视频工作流_2095019707211542530.json、视频生成/文生视频/Minimax H3 文生视频 8步加速Lora+sage双重加速工作流_2089325283299119105.json、视频生成/文生视频/MinimaxH3LORA加速工作流ENG文生视频4步ENG_2087097542533279745.json、视频生成/文生视频/MinimaxH3文生视频4步LORA加速工作流_2084217093255421954.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `easy int` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `MuyeTextEditOutput` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `EasyCache` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `Text Find and Replace` —— 1/6 个有
- `TextOverlay` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

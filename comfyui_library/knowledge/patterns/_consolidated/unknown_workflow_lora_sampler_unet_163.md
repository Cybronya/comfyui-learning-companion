---
name: unknown_workflow_lora_sampler_unet_163
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9172
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2099770316435316738.json, 视频生成/文生视频/MiniMax_H3_文生视频加速_2100031727967232001.json, 视频生成/文生视频/Minimax_h3_超级加速文生视频_2084160987023896578.json, 视频生成/文生视频/文生视频-MiniMaxH3-BV1-模板_2090725747148288002.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_163

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json、视频生成/文生视频/MiniMax_H3_文生视频加速_2099770316435316738.json、视频生成/文生视频/MiniMax_H3_文生视频加速_2100031727967232001.json、视频生成/文生视频/Minimax_h3_超级加速文生视频_2084160987023896578.json、视频生成/文生视频/文生视频-MiniMaxH3-BV1-模板_2090725747148288002.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SaveVideo` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `Label (rgthree)` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `PainterVRAM` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `Text Find and Replace` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `TextOverlay` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

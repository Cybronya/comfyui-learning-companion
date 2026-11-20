---
name: unknown_workflow_lora_sampler_unet_185
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7732
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/▶▷MiniMaxH3-加速视频流整合_2119219971925569537.json, 视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json, 视频生成/图生视频/▶▷MiniMaxH3-加速图生视频流_2089600631442067458.json, 视频生成/图生视频/▶▷MiniMaxH3-图生视频_2093020292909195265.json, 视频生成/文生视频/MiniMax H3全能参考生视频（动作迁移）_2084473001717878785.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_185

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/▶▷MiniMaxH3-加速视频流整合_2119219971925569537.json、视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json、视频生成/图生视频/▶▷MiniMaxH3-加速图生视频流_2089600631442067458.json、视频生成/图生视频/▶▷MiniMaxH3-图生视频_2093020292909195265.json、视频生成/文生视频/MiniMax H3全能参考生视频（动作迁移）_2084473001717878785.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `Label (rgthree)` —— 4/5 个有
- `MiniMaxH3ImageToVideo` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `MiniMaxH3ReferenceToVideo` —— 3/5 个有
- `Seed (rgthree)` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `LoadAudio` —— 1/5 个有
- `QwenTE_ImageInfer` —— 1/5 个有
- `QwenTE_ModelLoader` —— 1/5 个有
- `TE_H3_Prompt_Enhancer` —— 1/5 个有
- `TE_prompt_text` —— 1/5 个有
- `TE_text_display` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

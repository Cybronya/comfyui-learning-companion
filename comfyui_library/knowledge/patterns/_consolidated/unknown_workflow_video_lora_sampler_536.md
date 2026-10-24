---
name: unknown_workflow_video_lora_sampler_536
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8405
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/无限长视频流_2105728965766897665.json, 视频生成/图生视频/高尚无限长视频流_2098617968786763777.json, 视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json, 视频生成/文生视频/MiniMax H3超长视频流 一次直出2分15秒视频 （135S）_2101639116063600641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_536

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/无限长视频流_2105728965766897665.json、视频生成/图生视频/高尚无限长视频流_2098617968786763777.json、视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json、视频生成/文生视频/MiniMax H3超长视频流 一次直出2分15秒视频 （135S）_2101639116063600641.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 3/4 个有
- `GetImageRangeFromBatch` —— 3/4 个有
- `ImageBatchMulti` —— 3/4 个有
- `LayerColor: ColorAdapter` —— 3/4 个有
- `MiniMaxH3AddGuide` —— 3/4 个有
- `SaveAudio` —— 3/4 个有
- `Label (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `QwenH3PromptLocal` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

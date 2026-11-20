---
name: unknown_workflow_video_lora_sampler_285
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8773
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 动作、镜头参考(洗稿)_2093254936120348674.json, 视频生成/图生视频/Minimax H3 双时钟参考图生视频（4步极速）_2111092460335226882.json, 视频生成/图生视频/Minimax H3 图生视频 V1_2086828683976855553.json, 视频生成/图生视频/Minimax H3 数字人 - 音频驱动生视频_2085651236589756417.json, 视频生成/图生视频/Minimax H3音频研究_2087749629055164418.json, 视频生成/图生视频/Minimax-H3极速15秒 优化版-图生_多参生视频(双时钟-8步lora)_2086204757458374658.json, 视频生成/图生视频/minimax_h3官方高清加速竖版~横版_2084250037944668161.json, 视频生成/图生视频/加速版-MiniMax H3｜图文一键生视频_2108505916688654337.json, 视频生成/文生视频/(双时钟-8步高质量极速)Minimax图生视频V1_2085634625891815425.json, 视频生成/文生视频/DG_H3 双时钟 图生视频V1 bf16_2087807546869501953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_285

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 动作、镜头参考(洗稿)_2093254936120348674.json、视频生成/图生视频/Minimax H3 双时钟参考图生视频（4步极速）_2111092460335226882.json、视频生成/图生视频/Minimax H3 图生视频 V1_2086828683976855553.json、视频生成/图生视频/Minimax H3 数字人 - 音频驱动生视频_2085651236589756417.json、视频生成/图生视频/Minimax H3音频研究_2087749629055164418.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 8/10 个有
- `CR Prompt Text` —— 7/10 个有
- `LoadAudio` —— 4/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `VHS_LoadVideo` —— 4/10 个有
- `MiniMaxH3BlockCacheT8` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `easy int` —— 2/10 个有
- `AudioInfo` —— 1/10 个有
- `Getter` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `LoadVideoNode` —— 1/10 个有
- `Setter` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

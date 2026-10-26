---
name: unknown_workflow_video_lora_sampler_325
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.734375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json, 视频生成/文生视频/H3-氛围感短视频_2096431562895220737.json, 视频生成/文生视频/H3-氛围感网红打卡点短视频制作_2096832540542857218.json, 视频生成/文生视频/H3官流（最强武戏）_2108377903393239042.json, 视频生成/文生视频/H3官流（终极版）_2104734128657756162.json, 视频生成/文生视频/H3无损融合单采【官方满血API画布级本地流】_2108739345095155713.json, 视频生成/文生视频/minimaxH3+访谈类数字人_2097651536854863873.json, 视频生成/文生视频/minimaxH3数字人工作流（音色参考）_2094688876832055298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_325

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json、视频生成/文生视频/H3-氛围感短视频_2096431562895220737.json、视频生成/文生视频/H3-氛围感网红打卡点短视频制作_2096832540542857218.json、视频生成/文生视频/H3官流（最强武戏）_2108377903393239042.json、视频生成/文生视频/H3官流（终极版）_2104734128657756162.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
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
- `LoadAudio` —— 5/8 个有
- `ManualSigmas` —— 5/8 个有
- `ModelAttentionBackend` —— 5/8 个有
- `BlockSparseAttention` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `AudioCrop` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `QwenH3PromptLocal` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

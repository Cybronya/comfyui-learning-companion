---
name: unknown_workflow_video_lora_sampler_722
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.66575
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 mask替换人物_2099484034475847682.json, 视频生成/图生视频/MiniMax H3 超燃角色PV制作_2113688173112020993.json, 视频生成/图生视频/Minimax H3 高动态打斗模型，优化步数，减少等待时间_2098343857598582785.json, 视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_722

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/H3 mask替换人物_2099484034475847682.json、视频生成/图生视频/MiniMax H3 超燃角色PV制作_2113688173112020993.json、视频生成/图生视频/Minimax H3 高动态打斗模型，优化步数，减少等待时间_2098343857598582785.json、视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

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
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ImageAndMaskPreview` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `SAM3_TrackPreview` —— 1/4 个有
- `SAM3_TrackToMask` —— 1/4 个有
- `SAM3_VideoTrack` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `取色器_孤海` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

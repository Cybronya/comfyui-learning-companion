---
name: unknown_workflow_video_lora_sampler_577
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.852667
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/新4步lora三阶加速不降质音频驱动数字人-口播视频工作流 开源MiniMax H3 FL2VA_2090451028880748546.json, 视频生成/图生视频/新4步加速图生视频MiniMax H3_2090573463361773570.json, 视频生成/图生视频/超级提速不降质音频驱动数字人MV视频工作流开源MiniMax H3 Ref2VA_2086777029281796098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_577

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/新4步lora三阶加速不降质音频驱动数字人-口播视频工作流 开源MiniMax H3 FL2VA_2090451028880748546.json、视频生成/图生视频/新4步加速图生视频MiniMax H3_2090573463361773570.json、视频生成/图生视频/超级提速不降质音频驱动数字人MV视频工作流开源MiniMax H3 Ref2VA_2086777029281796098.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `MelBandRoFormerModelLoader` —— 2/3 个有
- `MelBandRoFormerSampler` —— 2/3 个有
- `MiniMaxH3AVDecodeT8` —— 2/3 个有
- `MiniMaxH3AudioConditioningT8` —— 2/3 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `SolAttnMiniMax` —— 2/3 个有
- `SoundFlow_GetLength` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/3 个有
- `BasicScheduler` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEDecodeAudio` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_544
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8005
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, EasyCache, Label (rgthree), LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnPatch, SpectrumApplyMiniMaxH3, UNETLoader, UniBlockSwap, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/新4步lora三阶加速不降质多参条件生视频工作流 开源MiniMax H3 FL2VA_2092519340435402753.json, 视频生成/图生视频/新4步lora三阶加速不降质尾帧生视频工作流 开源MiniMax H3 FL2VA_2089808482114560002.json, 视频生成/图生视频/新4步加速lora提速不降质图生视频工作流 开源MiniMax H3 FL2VA_2086037089392619521.json, 视频生成/图生视频/新4步加速lora提速不降质多条件参考视频工作流 开源MiniMax H3 FL2VA_2086043448649539585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_544

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/新4步lora三阶加速不降质多参条件生视频工作流 开源MiniMax H3 FL2VA_2092519340435402753.json、视频生成/图生视频/新4步lora三阶加速不降质尾帧生视频工作流 开源MiniMax H3 FL2VA_2089808482114560002.json、视频生成/图生视频/新4步加速lora提速不降质图生视频工作流 开源MiniMax H3 FL2VA_2086037089392619521.json、视频生成/图生视频/新4步加速lora提速不降质多条件参考视频工作流 开源MiniMax H3 FL2VA_2086043448649539585.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EasyCache`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnPatch`
- `SpectrumApplyMiniMaxH3`
- `UNETLoader`
- `UniBlockSwap`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SolAttnMiniMax` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `BasicScheduler` —— 1/4 个有
- `CS-MultiImageLoader` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MiniMaxH3ReferenceToVideo` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `VHS_LoadAudioUpload` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

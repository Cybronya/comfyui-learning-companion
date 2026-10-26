---
name: text_to_image_video_upscale_latent_upscale_8
type: Text To Image
frequency: 8
level: strong
coverage: 0.76775
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, Float, GetNode, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/绘影MiniMax H3文武均衡720P V2 视频生成方案_2105058333806907393.json, 视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强_2099911788254027778.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强宫格图生视频_2099910070346801153.json, 视频生成/文生视频/H3双采全能工作流V2 音频驱动数字人参考生视频_2099905442196574210.json, 视频生成/文生视频/H3双采全能工作流V2文戏不油武戏动态强宫格图生视频_2100639256866811906.json, 视频生成/文生视频/H3双采多参考生视频文武双全全能版10eros Beta5_2100681746168762369.json, 视频生成/文生视频/文武全能图音参考MiniMax H3双采视频生成处理工具_2101038033029124097.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_8

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/绘影MiniMax H3文武均衡720P V2 视频生成方案_2105058333806907393.json、视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json、视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强_2099911788254027778.json、视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强宫格图生视频_2099910070346801153.json、视频生成/文生视频/H3双采全能工作流V2 音频驱动数字人参考生视频_2099905442196574210.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Float`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `Int` —— 4/8 个有
- `LoadAudio` —— 4/8 个有
- `ComfyNumberConvert` —— 2/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `Compare` —— 2/8 个有
- `ConcatTextOfUtils` —— 2/8 个有
- `MiniMaxChunkFeedForward` —— 2/8 个有
- `MiniMaxH3ReferenceToVideo` —— 2/8 个有
- `MiniMaxLowVRAMAttention` —— 2/8 个有
- `SplitStringByDelimiter` —— 2/8 个有
- `easy anythingIndexSwitch` —— 2/8 个有
- `easy ifElse` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `ratio_selector` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

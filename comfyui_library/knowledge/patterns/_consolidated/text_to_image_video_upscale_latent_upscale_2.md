---
name: text_to_image_video_upscale_latent_upscale_2
type: Text To Image
frequency: 24
level: strong
coverage: 0.699417
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/绘影MiniMax H3文武均衡720P V2 视频生成方案_2105058333806907393.json, 视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强_2099911788254027778.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强宫格图生视频_2099910070346801153.json, 视频生成/文生视频/H3双采全能工作流V2 音频驱动数字人参考生视频_2099905442196574210.json, 视频生成/文生视频/H3双采全能工作流V2文戏不油武戏动态强宫格图生视频_2100639256866811906.json, 视频生成/文生视频/H3双采多参考生视频文武双全全能版10eros Beta5_2100681746168762369.json, 视频生成/文生视频/MINIMAX-H3多参二采新玩法｜9图3音混合参考生成视频_2106930396553367553.json, 视频生成/文生视频/MiniMax H3 双采V2｜音频驱动数字人 参考生视频全能流_2097541384940118017.json, 视频生成/文生视频/MiniMax H3 双采全能 V2 参考生视频｜文戏不油腻武戏动态强_2096828255583166466.json, 视频生成/文生视频/MiniMax H3 双采全能 V2 文生视频｜文戏不油武戏动感十足_2096831559121850370.json, 视频生成/文生视频/MiniMax H3 双采多参V2均衡版｜文生图生视频画质速度兼得_2097554449018478593.json, 视频生成/文生视频/MiniMax H3动态最强文生视频｜高质量动作生成V1_2094868618122186753.json, 视频生成/文生视频/MiniMax H3双采V2｜参考生视频，文戏清爽武戏动态拉满_2099867081805221890.json, 视频生成/文生视频/MiniMax H3双采全能V2工作流｜音频驱动数字人参考生视频_2097420200982433794.json, 视频生成/文生视频/MiniMax H3双采全能V2文戏武戏文生视频处理工作流_2101737492507619329.json, 视频生成/文生视频/MiniMax H3双采全能V2版｜文戏不油武戏动态强文生视频_2101569247532113922.json, 视频生成/文生视频/MiniMax H3双采全能V2｜宫格图生视频，文戏不油武戏更带感_2099852923181293569.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2｜文戏不油武戏动态强，宫格图生视频一步成片_2100446257608216578.json, 视频生成/文生视频/MiniMax H3双采全能文戏武戏参考视频生成处理工具包V2_2100995467332116481.json, 视频生成/文生视频/MiniMax H3双采全能音频驱动数字人多人对话处理工具V2_2101355992037548034.json, 视频生成/文生视频/MiniMax H3双采多参均衡版｜文生图生视频多模式生成工作流_2097398089035378689.json, 视频生成/文生视频/MiniMax H3音频驱动数字人文生视频｜双采全能V2工作流_2097517539004866562.json, 视频生成/文生视频/文武全能图音参考MiniMax H3双采视频生成处理工具_2101038033029124097.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_2

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/绘影MiniMax H3文武均衡720P V2 视频生成方案_2105058333806907393.json、视频生成/图生视频/绘影MiniMax H3文武均衡720P图生视频处理工具V1.4_2101359993487446017.json、视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强_2099911788254027778.json、视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强宫格图生视频_2099910070346801153.json、视频生成/文生视频/H3双采全能工作流V2 音频驱动数字人参考生视频_2099905442196574210.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
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
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 22/24 个有
- `ResolutionSelector` —— 22/24 个有
- `Float` —— 21/24 个有
- `Fast Groups Bypasser (rgthree)` —— 14/24 个有
- `SaveImage` —— 14/24 个有
- `LoadAudio` —— 11/24 个有
- `Int` —— 4/24 个有
- `AudioCrop` —— 3/24 个有
- `VHS_LoadVideo` —— 3/24 个有
- `ComfyNumberConvert` —— 2/24 个有
- `ComfySwitchNode` —— 2/24 个有
- `Compare` —— 2/24 个有
- `ConcatTextOfUtils` —— 2/24 个有
- `MiniMaxChunkFeedForward` —— 2/24 个有
- `MiniMaxH3ReferenceToVideo` —— 2/24 个有
- `MiniMaxLowVRAMAttention` —— 2/24 个有
- `ModelPreviewOverrideKJ` —— 2/24 个有
- `SplitStringByDelimiter` —— 2/24 个有
- `easy anythingIndexSwitch` —— 2/24 个有
- `easy ifElse` —— 2/24 个有
- `easy showAnything` —— 2/24 个有
- `ratio_selector` —— 2/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高发问题（24/24 个样本）：Steps较低可能导致细节不足

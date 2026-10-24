---
name: text_to_image_video_lora_sampler_20
type: Text To Image
frequency: 27
level: strong
coverage: 0.693074
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3-最优加速工作流文生视频图生视频_2085853717911400449.json, 视频生成/文生视频/H3全能参考工作流-文生视频生视频图生视频_2087365023227277313.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强_2099911788254027778.json, 视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强宫格图生视频_2099910070346801153.json, 视频生成/文生视频/H3双采全能工作流V2 音频驱动数字人参考生视频_2099905442196574210.json, 视频生成/文生视频/H3双采全能工作流V2文戏不油武戏动态强宫格图生视频_2100639256866811906.json, 视频生成/文生视频/H3双采多参考生视频文武双全全能版10eros Beta5_2100681746168762369.json, 视频生成/文生视频/MINIMAX-H3多参二采新玩法｜9图3音混合参考生成视频_2106930396553367553.json, 视频生成/文生视频/MiniMax H3 双采V2｜音频驱动数字人 参考生视频全能流_2097541384940118017.json, 视频生成/文生视频/MiniMax H3 双采全能 V2 参考生视频｜文戏不油腻武戏动态强_2096828255583166466.json, 视频生成/文生视频/MiniMax H3 双采全能 V2 文生视频｜文戏不油武戏动感十足_2096831559121850370.json, 视频生成/文生视频/MiniMax H3 双采多参V2均衡版｜文生图生视频画质速度兼得_2097554449018478593.json, 视频生成/文生视频/MiniMax H3九图三音多参二采工作流，文生视频图生视频多参考方案_2107232675256950785.json, 视频生成/文生视频/MiniMax H3全能参考生视频 最佳动态V3极速高清版_2098706745035149314.json, 视频生成/文生视频/MiniMax H3动态最强文生视频｜高质量动作生成V1_2094868618122186753.json, 视频生成/文生视频/MiniMax H3双采V2｜参考生视频，文戏清爽武戏动态拉满_2099867081805221890.json, 视频生成/文生视频/MiniMax H3双采全能V2工作流｜音频驱动数字人参考生视频_2097420200982433794.json, 视频生成/文生视频/MiniMax H3双采全能V2文戏武戏文生视频处理工作流_2101737492507619329.json, 视频生成/文生视频/MiniMax H3双采全能V2版｜文戏不油武戏动态强文生视频_2101569247532113922.json, 视频生成/文生视频/MiniMax H3双采全能V2｜宫格图生视频，文戏不油武戏更带感_2099852923181293569.json, 视频生成/文生视频/MiniMax H3双采全能工作流V2｜文戏不油武戏动态强，宫格图生视频一步成片_2100446257608216578.json, 视频生成/文生视频/MiniMax H3双采全能文戏武戏参考视频生成处理工具包V2_2100995467332116481.json, 视频生成/文生视频/MiniMax H3双采全能音频驱动数字人多人对话处理工具V2_2101355992037548034.json, 视频生成/文生视频/MiniMax H3双采多参均衡版｜文生图生视频多模式生成工作流_2097398089035378689.json, 视频生成/文生视频/MiniMax H3音频驱动数字人文生视频｜双采全能V2工作流_2097517539004866562.json, 视频生成/文生视频/xinlingjitang文生视频｜灵感创作直出_2097953578789982209.json, 视频生成/文生视频/文武全能图音参考MiniMax H3双采视频生成处理工具_2101038033029124097.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/文生视频/H3-最优加速工作流文生视频图生视频_2085853717911400449.json、视频生成/文生视频/H3全能参考工作流-文生视频生视频图生视频_2087365023227277313.json、视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强_2099911788254027778.json、视频生成/文生视频/H3双采全能工作流V2 文戏不油武戏动态强宫格图生视频_2099910070346801153.json、视频生成/文生视频/H3双采全能工作流V2 音频驱动数字人参考生视频_2099905442196574210.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 26/27 个有
- `LoadImage` —— 26/27 个有
- `LoraLoaderBypassModelOnly` —— 26/27 个有
- `MiniMaxH3AudioConditioningT8` —— 26/27 个有
- `MiniMaxH3DualClockSamplerT8` —— 26/27 个有
- `SetNode` —— 26/27 个有
- `CR Prompt Text` —— 25/27 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 25/27 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 25/27 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 25/27 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 25/27 个有
- `ModelAttentionBackend` —— 25/27 个有
- `SolAttnMiniMax` —— 25/27 个有
- `Float` —— 20/27 个有
- `Fast Groups Bypasser (rgthree)` —— 16/27 个有
- `SaveImage` —— 14/27 个有
- `LoadAudio` —— 13/27 个有
- `AudioCrop` —— 3/27 个有
- `ConcatTextOfUtils` —— 3/27 个有
- `VHS_LoadVideo` —— 3/27 个有
- `Int` —— 2/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/27 个有
- `ModelPreviewOverrideKJ` —— 2/27 个有
- `PrimitiveStringMultiline` —— 2/27 个有
- `easy anythingIndexSwitch` —— 2/27 个有
- `1hew_AudioDuration` —— 1/27 个有
- `LayerUtility: TextJoin` —— 1/27 个有
- `MathExpression|pysssss` —— 1/27 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/27 个有
- `MiniMaxH3ReferenceToVideo` —— 1/27 个有
- `SaveVideoNode` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（27/27 个样本）：Steps较低可能导致细节不足

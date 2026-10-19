---
name: text_to_image_video_lora_sampler_33
type: Text To Image
frequency: 17
level: strong
coverage: 0.774294
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/xinlingjitang文生视频｜灵感创作直出_2097953578789982209.json, 视频生成/文生视频/万象文武双修均衡版｜12秒横屏多参视频生成制作_2096322789388144642.json, 视频生成/文生视频/动态最强文生视频｜MiniMax H3 V1版一键生成_2095059601229176833.json, 视频生成/文生视频/动漫短剧文武双修｜MiniMax H3双采参考生视频_2096309683601633281.json, 视频生成/文生视频/双时钟8步lora极速4分钟出15秒480P｜Minimax-H3文生视频工作流_2087215608109821953.json, 视频生成/文生视频/双时钟8步高质量极速多参V1｜Minimax文生图生视频生视频工作流_2087188424548769794.json, 视频生成/文生视频/双采全能参考生视频｜MiniMax H3文戏武戏均衡工作流_2096680911407505409.json, 视频生成/文生视频/双采全能参考视频｜MiniMax H3真实电影质感文武均衡_2096297117051609090.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3宫格视频，武戏动态强文戏清爽_2099854300494262273.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3文戏不油武戏动态强_2096653036163784706.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3文生视频，文戏武戏都在线_2099868566425260033.json, 视频生成/文生视频/双采样武戏专用生成｜MiniMax-H3多参首尾帧_2095970956106887169.json, 视频生成/文生视频/文戏不油武戏动态强 MiniMax H3全能文武戏工作流_2104665855941505025.json, 视频生成/文生视频/文戏不油武戏带感 MiniMax H3双采全能参考生视频V2_2104287266226139138.json, 视频生成/文生视频/武戏专用双采样文生图｜MiniMax-H3 多参首尾帧出片_2096261692538839041.json, 视频生成/文生视频/音频驱动数字人双采工作流｜MiniMax H3 V2参考生视频_2097501642370408449.json, 视频生成/文生视频/音频驱动数字人｜MiniMax H3双采V2参考生视频，口型同步_2099865159194996737.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/xinlingjitang文生视频｜灵感创作直出_2097953578789982209.json、视频生成/文生视频/万象文武双修均衡版｜12秒横屏多参视频生成制作_2096322789388144642.json、视频生成/文生视频/动态最强文生视频｜MiniMax H3 V1版一键生成_2095059601229176833.json、视频生成/文生视频/动漫短剧文武双修｜MiniMax H3双采参考生视频_2096309683601633281.json、视频生成/文生视频/双时钟8步lora极速4分钟出15秒480P｜Minimax-H3文生视频工作流_2087215608109821953.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `ComfyMathExpression` —— 16/17 个有
- `LoadImage` —— 15/17 个有
- `LoraLoaderBypassModelOnly` —— 15/17 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 15/17 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 15/17 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 15/17 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 15/17 个有
- `ModelAttentionBackend` —— 15/17 个有
- `PrimitiveFloat` —— 15/17 个有
- `SolAttnMiniMax` —— 15/17 个有
- `CR Prompt Text` —— 14/17 个有
- `GetNode` —— 10/17 个有
- `SetNode` —— 10/17 个有
- `Float` —— 9/17 个有
- `Fast Groups Bypasser (rgthree)` —— 7/17 个有
- `LoadAudio` —— 3/17 个有
- `SaveImage` —— 3/17 个有
- `Int` —— 2/17 个有
- `MathExpression|pysssss` —— 2/17 个有
- `PreviewAny` —— 2/17 个有
- `RH_Screenwriter` —— 2/17 个有
- `WujiH3PromptEnhancer` —— 2/17 个有
- `1hew_AudioDuration` —— 1/17 个有
- `CR Load LoRA` —— 1/17 个有
- `FastGroupsBypassSwitch` —— 1/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `LayerUtility: TextJoin` —— 1/17 个有
- `PrimitiveInt` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `VHS_LoadVideo` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足

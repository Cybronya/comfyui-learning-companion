---
name: text_to_image_video_lora_sampler_44
type: Text To Image
frequency: 17
level: strong
coverage: 0.796471
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json, 视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json, 视频生成/文生视频/minimax三图工作流｜文生图生视频一键生成_2091309114570919938.json, 视频生成/文生视频/sage无损加速双bf16满血版MinimaxH3文生视频图生视频极致清晰_2088396155074990082.json, 视频生成/文生视频/sage无损加速｜MinimaxH3双bf16满血版文生图生视频全能_2089463275493875714.json, 视频生成/文生视频/万象文武双修均衡版｜12秒横屏多参视频生成制作_2096322789388144642.json, 视频生成/文生视频/二采高清放大minimaxH3工作流ENG_2087133080908816386.json, 视频生成/文生视频/动态最强文生视频｜MiniMax H3 V1版一键生成_2095059601229176833.json, 视频生成/文生视频/动漫短剧文武双修｜MiniMax H3双采参考生视频_2096309683601633281.json, 视频生成/文生视频/双采全能参考生视频｜MiniMax H3文戏武戏均衡工作流_2096680911407505409.json, 视频生成/文生视频/双采全能参考视频｜MiniMax H3真实电影质感文武均衡_2096297117051609090.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3宫格视频，武戏动态强文戏清爽_2099854300494262273.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3文戏不油武戏动态强_2096653036163784706.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3文生视频，文戏武戏都在线_2099868566425260033.json, 视频生成/文生视频/文戏不油武戏动态强 MiniMax H3全能文武戏工作流_2104665855941505025.json, 视频生成/文生视频/音频驱动数字人双采工作流｜MiniMax H3 V2参考生视频_2097501642370408449.json, 视频生成/文生视频/音频驱动数字人｜MiniMax H3双采V2参考生视频，口型同步_2099865159194996737.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json、视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json、视频生成/文生视频/minimax三图工作流｜文生图生视频一键生成_2091309114570919938.json、视频生成/文生视频/sage无损加速双bf16满血版MinimaxH3文生视频图生视频极致清晰_2088396155074990082.json、视频生成/文生视频/sage无损加速｜MinimaxH3双bf16满血版文生图生视频全能_2089463275493875714.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 16/17 个有
- `ResolutionSelector` —— 16/17 个有
- `孤海注释` —— 16/17 个有
- `CR Prompt Text` —— 15/17 个有
- `LoraLoaderBypassModelOnly` —— 15/17 个有
- `MiniMaxH3DualClockSamplerT8` —— 15/17 个有
- `ModelAttentionBackend` —— 12/17 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 11/17 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 11/17 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 11/17 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 11/17 个有
- `SolAttnMiniMax` —— 11/17 个有
- `Float` —— 8/17 个有
- `GetNode` —— 8/17 个有
- `SetNode` —— 8/17 个有
- `Fast Groups Bypasser (rgthree)` —— 5/17 个有
- `BasicScheduler` —— 3/17 个有
- `KSamplerSelect` —— 3/17 个有
- `LoadAudio` —— 2/17 个有
- `SaveImage` —— 2/17 个有
- `CR Text` —— 1/17 个有
- `ImageResizeKJv2` —— 1/17 个有
- `Int` —— 1/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有
- `PT_H3ConcatAVLatent` —— 1/17 个有
- `Text Multiline` —— 1/17 个有
- `VAEEncode` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足

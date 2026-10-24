---
name: text_to_image_lora_sampler_clip_27
type: Text To Image
frequency: 23
level: strong
coverage: 0.81213
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生·首尾帧·多参一体化（H38步双时钟）极速导演台ENG_2087117508317900801.json, 视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json, 视频生成/图生视频/图生视频基础版｜海螺Minimax_H3一键生成_2092175596649537537.json, 视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json, 视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json, 视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json, 视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json, 视频生成/图生视频/多参工作流｜minimax h3图生视频一键生成_2095085442826850306.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧创意视频_2092025540294303746.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧角色设计生成_2094785389037965314.json, 视频生成/图生视频/开源版Minimax H3视频全功能加速-turbo4步图片参考短视频生成_2087388416773283842.json, 视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json, 视频生成/文生视频/万象文武双修均衡版｜12秒横屏多参视频生成制作_2096322789388144642.json, 视频生成/文生视频/动态最强文生视频｜MiniMax H3 V1版一键生成_2095059601229176833.json, 视频生成/文生视频/动漫短剧文武双修｜MiniMax H3双采参考生视频_2096309683601633281.json, 视频生成/文生视频/双采全能参考生视频｜MiniMax H3文戏武戏均衡工作流_2096680911407505409.json, 视频生成/文生视频/双采全能参考视频｜MiniMax H3真实电影质感文武均衡_2096297117051609090.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3宫格视频，武戏动态强文戏清爽_2099854300494262273.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3文戏不油武戏动态强_2096653036163784706.json, 视频生成/文生视频/双采全能工作流V2｜MiniMax H3文生视频，文戏武戏都在线_2099868566425260033.json, 视频生成/文生视频/文戏不油武戏动态强 MiniMax H3全能文武戏工作流_2104665855941505025.json, 视频生成/文生视频/音频驱动数字人双采工作流｜MiniMax H3 V2参考生视频_2097501642370408449.json, 视频生成/文生视频/音频驱动数字人｜MiniMax H3双采V2参考生视频，口型同步_2099865159194996737.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/图生·首尾帧·多参一体化（H38步双时钟）极速导演台ENG_2087117508317900801.json、视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json、视频生成/图生视频/图生视频基础版｜海螺Minimax_H3一键生成_2092175596649537537.json、视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json、视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 22/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 22/23 个有
- `VHS_VideoCombine` —— 22/23 个有
- `MiniMaxH3DualClockSamplerT8` —— 20/23 个有
- `CR Prompt Text` —— 16/23 个有
- `ModelAttentionBackend` —— 16/23 个有
- `SolAttnMiniMax` —— 15/23 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 12/23 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 12/23 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 12/23 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 12/23 个有
- `Float` —— 8/23 个有
- `GetNode` —— 8/23 个有
- `SetNode` —— 8/23 个有
- `Fast Groups Bypasser (rgthree)` —— 5/23 个有
- `PrimitiveStringMultiline` —— 4/23 个有
- `LoadAudio` —— 2/23 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/23 个有
- `SaveImage` —— 2/23 个有
- `Text` —— 2/23 个有
- `CR Text` —— 1/23 个有
- `CreateVideo` —— 1/23 个有
- `GetImageSize` —— 1/23 个有
- `ImageResizeKJv2` —— 1/23 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/23 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/23 个有
- `RH_LLMAPI_Pro_Node` —— 1/23 个有
- `SaveVideo` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足

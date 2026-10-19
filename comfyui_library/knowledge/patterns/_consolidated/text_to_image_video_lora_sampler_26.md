---
name: text_to_image_video_lora_sampler_26
type: Text To Image
frequency: 18
level: strong
coverage: 0.862333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json, 视频生成/图生视频/图生视频基础版｜海螺Minimax_H3一键生成_2092175596649537537.json, 视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json, 视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json, 视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json, 视频生成/图生视频/多参工作流｜minimax h3图生视频一键生成_2095085442826850306.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧创意视频_2092025540294303746.json, 视频生成/图生视频/开源参考生视频｜Minimax-H3短剧漫剧角色设计生成_2094785389037965314.json, 视频生成/图生视频/开源版Minimax H3视频全功能加速-turbo4步图片参考短视频生成_2087388416773283842.json, 视频生成/图生视频/海螺H3图生视频｜8步极速加速优化t8版，角色表演流畅_2099887065814093826.json, 视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json, 视频生成/图生视频/海螺h3开源版H3数字人单人数字人图生视频口播数字人加速版MiniMax_2086453850634014722.json, 视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json, 视频生成/图生视频/自用4步加速图生视频工作流｜极速出片效率翻倍_2100850409333149698.json, 视频生成/图生视频/音频驱动音乐MV｜MiniMax H3数字人加速版V1出片快_2100122889331765250.json, 视频生成/文生视频/10Eros Beta5+FL2VA Ref2VA小脸去油二采精修视频处理工具_2102108154879369218.json, 视频生成/文生视频/MiniMax H3九图三音多参二采工作流，文生视频图生视频多参考方案_2107232675256950785.json, 视频生成/文生视频/MiniMax H3全能参考生视频 最佳动态V3极速高清版_2098706745035149314.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/图生视频Minimax_H3_ENG海螺_2087149189619863554.json、视频生成/图生视频/图生视频基础版｜海螺Minimax_H3一键生成_2092175596649537537.json、视频生成/图生视频/图生视频工作流｜MINIMAX-H3多功能视频生成_2090564776375185409.json、视频生成/图生视频/多主体生视Minimax_H3频ENG海螺_2087146580276244481.json、视频生成/图生视频/多主体生视频｜海螺Minimax_H3图生视频生成_2092178321030336513.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 18 个 workflow 都包含：
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
- `LoraLoaderBypassModelOnly` —— 17/18 个有
- `ResolutionSelector` —— 17/18 个有
- `孤海注释` —— 16/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 15/18 个有
- `CR Prompt Text` —— 9/18 个有
- `ModelAttentionBackend` —— 9/18 个有
- `SolAttnMiniMax` —— 7/18 个有
- `LoadAudio` —— 5/18 个有
- `PrimitiveStringMultiline` —— 5/18 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 4/18 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 4/18 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 4/18 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 4/18 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/18 个有
- `SaveImage` —— 3/18 个有
- `CR Text` —— 2/18 个有
- `ConcatTextOfUtils` —— 2/18 个有
- `GetNode` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `SetNode` —— 2/18 个有
- `Text` —— 2/18 个有
- `AudioCrop` —— 1/18 个有
- `CreateVideo` —— 1/18 个有
- `GetImageSize` —— 1/18 个有
- `GetVideoComponents` —— 1/18 个有
- `ImageResizeKJv2` —— 1/18 个有
- `Int` —— 1/18 个有
- `LoadVideo` —— 1/18 个有
- `RH_LLMAPI_Pro_Node` —— 1/18 个有
- `SaveVideo` —— 1/18 个有
- `SaveVideoNode` —— 1/18 个有
- `VHS_LoadVideo` —— 1/18 个有
- `Video Slice` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足

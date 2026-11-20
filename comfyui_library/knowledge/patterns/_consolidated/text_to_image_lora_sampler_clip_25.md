---
name: text_to_image_lora_sampler_clip_25
type: Text To Image
frequency: 25
level: strong
coverage: 0.88472
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json, 视频生成/图生视频/海螺h3开源版H3数字人单人数字人图生视频口播数字人加速版MiniMax_2086453850634014722.json, 视频生成/图生视频/稳定加速5参考图版｜MiniMax H3全能参考自定义音频_2091200766919925762.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3五参考图音频自定义_2090900087277973505.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3开源支持自定义音频_2091271985484623874.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3支持自定义音频_2092396498217689090.json, 视频生成/图生视频/稳定加速版｜MiniMax H3 全能参考4步加速_2089295207438307330.json, 视频生成/图生视频/自用4步加速图生视频工作流｜极速出片效率翻倍_2100850409333149698.json, 视频生成/图生视频/超级加速多图参考生视频｜Minimax_h3角色一致性角色表演工作流_2087208437443809281.json, 视频生成/图生视频/首尾帧EMinimax_H3_NG海螺图生视频_2087147808825626625.json, 视频生成/图生视频/首尾帧加速版｜MiniMaxH3开源图生视频直出_2089828334866882562.json, 视频生成/图生视频/首尾帧生视频｜海螺Minimax_H3图生视频生成_2092176988864864257.json, 视频生成/文生视频/0.8720P双时钟高质量加速文生视频视频生视频图生视频_2087431901580709890.json, 视频生成/文生视频/4步lora 1.0+sage双重加速｜MinimaxH3双bf16满血版视频生成_2089461776118280193.json, 视频生成/文生视频/4步lora 768P 10秒模板｜Minimax H3满血多参双bf16加sage加速_2088760487675781121.json, 视频生成/文生视频/4步加速lora动漫生成 Minimax H3 Dasiwa 6步快速出片_2094222041418391553.json, 视频生成/文生视频/4步加速全能参考生视频-MiniMax H3文生视频生视频_2087339437670879234.json, 视频生成/文生视频/4步加速全能参考生视频｜MiniMax H3文生图生视频_2091277215991422978.json, 视频生成/文生视频/4步加速全能参考｜MiniMax H3九图三视频三音频生视频_2091267858146877441.json, 视频生成/文生视频/H3！加速版！提速480%！全能参考！MiniMax_2085855519343996930.json, 视频生成/文生视频/Minimax H3参考生成｜多模态素材视频生成_2095229500903747585.json, 视频生成/文生视频/MinimaxH3开源版参考生视频｜9-3-3高质量生成_2095584855844278273.json, 视频生成/文生视频/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086411021345972225.json, 视频生成/文生视频/最新最快4步8步增速工作流Minimax H3文生视频图生视频_2088410988835074049.json, 视频生成/文生视频/最新最快4步和8步增速｜Minimax H3文生图生视频工作流_2088388313551040514.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json、视频生成/图生视频/海螺h3开源版H3数字人单人数字人图生视频口播数字人加速版MiniMax_2086453850634014722.json、视频生成/图生视频/稳定加速5参考图版｜MiniMax H3全能参考自定义音频_2091200766919925762.json、视频生成/图生视频/稳定加速版全能参考｜MiniMax H3五参考图音频自定义_2090900087277973505.json、视频生成/图生视频/稳定加速版全能参考｜MiniMax H3开源支持自定义音频_2091271985484623874.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 24/25 个有
- `VHS_VideoCombine` —— 22/25 个有
- `孤海注释` —— 22/25 个有
- `MiniMaxH3AudioConditioningT8` —— 21/25 个有
- `LoraLoaderBypassModelOnly` —— 18/25 个有
- `MiniMaxH3DualClockSamplerT8` —— 17/25 个有
- `MiniMaxH3AVDecodeT8` —— 15/25 个有
- `LoadAudio` —— 14/25 个有
- `PrimitiveStringMultiline` —— 12/25 个有
- `BasicScheduler` —— 11/25 个有
- `KSamplerSelect` —— 10/25 个有
- `VAEDecodeAudio` —— 10/25 个有
- `CR Prompt Text` —— 9/25 个有
- `CreateVideo` —— 9/25 个有
- `SaveVideo` —— 9/25 个有
- `GetVideoComponents` —— 7/25 个有
- `LoadVideo` —— 7/25 个有
- `MiniMaxH3ReferenceToVideo` —— 4/25 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/25 个有
- `CR Float To Integer` —— 2/25 个有
- `Label (rgthree)` —— 2/25 个有
- `LayerUtility: PurgeVRAM V2` —— 2/25 个有
- `MiniMaxH3ImageToVideo` —— 2/25 个有
- `CR Text` —— 1/25 个有
- `Int` —— 1/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/25 个有
- `ModelAttentionBackend` —— 1/25 个有
- `PainterVRAM` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（25/25 个样本）：Steps较低可能导致细节不足

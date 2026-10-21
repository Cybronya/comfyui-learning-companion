---
name: text_to_image_lora_sampler_clip_15
type: Text To Image
frequency: 27
level: strong
coverage: 0.89237
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json, 视频生成/图生视频/海螺H3图生视频｜8步极速加速优化t8版，角色表演流畅_2099887065814093826.json, 视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json, 视频生成/图生视频/海螺h3开源版H3数字人单人数字人图生视频口播数字人加速版MiniMax_2086453850634014722.json, 视频生成/图生视频/稳定加速5参考图版｜MiniMax H3全能参考自定义音频_2091200766919925762.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3五参考图音频自定义_2090900087277973505.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3开源支持自定义音频_2091271985484623874.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3支持自定义音频_2092396498217689090.json, 视频生成/图生视频/稳定加速版｜MiniMax H3 全能参考4步加速_2089295207438307330.json, 视频生成/图生视频/首尾帧加速版｜MiniMaxH3开源图生视频直出_2089828334866882562.json, 视频生成/文生视频/4步lora 1.0+sage双重加速｜MinimaxH3双bf16满血版视频生成_2089461776118280193.json, 视频生成/文生视频/4步lora 768P 10秒模板｜Minimax H3满血多参双bf16加sage加速_2088760487675781121.json, 视频生成/文生视频/4步加速lora动漫生成 Minimax H3 Dasiwa 6步快速出片_2094222041418391553.json, 视频生成/文生视频/Dasiwa动漫4步加速lora｜Minimax+H3 6步三模视频_2094587676379934721.json, 视频生成/文生视频/Dasiwa动漫多参考｜Minimax H3直出1080P生视频_2094342464118284289.json, 视频生成/文生视频/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086411021345972225.json, 视频生成/文生视频/剪枝版BF16微表情｜Minimax H3 10秒768P模板_2090578253928034305.json, 视频生成/文生视频/剪枝版BF16高动态5秒｜Minimax H3 768P视频模板_2090576848353849345.json, 视频生成/文生视频/剪枝版BF16高动态｜Minimax H3 15秒768P模板_2090575450929188866.json, 视频生成/文生视频/剪枝版BF16高动态｜Minimax H3 15秒768P视频模板_2090889192581713922.json, 视频生成/文生视频/剪枝版高动态5秒模板｜Minimax H3 BF16 768P视频生成_2090892022604455938.json, 视频生成/文生视频/动漫多参考8步加速lora Minimax H3 Dasiwa 10步出片_2094220547021426689.json, 视频生成/文生视频/动漫多参考直出1080P Minimax H3 Dasiwa文生视频_2094217735050973186.json, 视频生成/文生视频/原版BF16高动态15秒｜Minimax H3 768P视频模板_2090880996274171906.json, 视频生成/文生视频/多参考打斗视频生成｜MiniMax H3 BF16 768P lora_2095944735889383425.json, 视频生成/文生视频/多参考真实打斗生成｜MiniMax H3 Dasiwa 768P lora_2095940373528014850.json, 视频生成/文生视频/微表情10秒768P模板｜Minimax H3剪枝版BF16视频_2090893466330030082.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json、视频生成/图生视频/海螺H3图生视频｜8步极速加速优化t8版，角色表演流畅_2099887065814093826.json、视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json、视频生成/图生视频/海螺h3开源版H3数字人单人数字人图生视频口播数字人加速版MiniMax_2086453850634014722.json、视频生成/图生视频/稳定加速5参考图版｜MiniMax H3全能参考自定义音频_2091200766919925762.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 26/27 个有
- `ResolutionSelector` —— 26/27 个有
- `VHS_VideoCombine` —— 26/27 个有
- `孤海注释` —— 24/27 个有
- `BasicScheduler` —— 22/27 个有
- `KSamplerSelect` —— 21/27 个有
- `MiniMaxH3AVDecodeT8` —— 21/27 个有
- `CR Prompt Text` —— 18/27 个有
- `LayerUtility: PurgeVRAM V2` —— 15/27 个有
- `LoraLoaderBypassModelOnly` —— 9/27 个有
- `MiniMaxH3DualClockSamplerT8` —— 8/27 个有
- `PrimitiveStringMultiline` —— 8/27 个有
- `CreateVideo` —— 7/27 个有
- `SaveVideo` —— 7/27 个有
- `LoadAudio` —— 6/27 个有
- `VAEDecodeAudio` —— 6/27 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/27 个有
- `CR Text` —— 1/27 个有
- `Int` —— 1/27 个有
- `Label (rgthree)` —— 1/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/27 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/27 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/27 个有
- `SolAttnMiniMax` —— 1/27 个有

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

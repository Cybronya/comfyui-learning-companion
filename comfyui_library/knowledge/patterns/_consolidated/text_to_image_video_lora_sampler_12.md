---
name: text_to_image_video_lora_sampler_12
type: Text To Image
frequency: 31
level: strong
coverage: 0.897323
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json, 视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json, 视频生成/文生视频/minimax三图工作流｜文生图生视频一键生成_2091309114570919938.json, 视频生成/文生视频/sage无损加速双bf16满血版MinimaxH3文生视频图生视频极致清晰_2088396155074990082.json, 视频生成/文生视频/sage无损加速｜MinimaxH3双bf16满血版文生图生视频全能_2089463275493875714.json, 视频生成/文生视频/二采高清放大minimaxH3工作流ENG_2087133080908816386.json, 视频生成/文生视频/八步极速Minimax H3开源版 短剧漫剧创意视频新加速lora_2098305874950443010.json, 视频生成/文生视频/剪枝版BF16微表情｜Minimax H3 10秒768P模板_2090578253928034305.json, 视频生成/文生视频/剪枝版BF16高动态5秒｜Minimax H3 768P视频模板_2090576848353849345.json, 视频生成/文生视频/剪枝版BF16高动态｜Minimax H3 15秒768P模板_2090575450929188866.json, 视频生成/文生视频/剪枝版BF16高动态｜Minimax H3 15秒768P视频模板_2090889192581713922.json, 视频生成/文生视频/剪枝版高动态5秒模板｜Minimax H3 BF16 768P视频生成_2090892022604455938.json, 视频生成/文生视频/加速版直出｜MiniMax_H3_BF16_Turbo_Sage_ 文生图生视频高速生成_2089458798560894978.json, 视频生成/文生视频/动作增强修复双采｜Minimax H3 b25-49参数版生成_2096314410406072321.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采bf16精度稳定出片_2096530999692849154.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采参数b25精细调校版_2096529451092889602.json, 视频生成/文生视频/动漫多参考8步加速lora Minimax H3 Dasiwa 10步出片_2094220547021426689.json, 视频生成/文生视频/动漫多参考直出1080P Minimax H3 Dasiwa文生视频_2094217735050973186.json, 视频生成/文生视频/原版BF16高动态15秒｜Minimax H3 768P视频模板_2090880996274171906.json, 视频生成/文生视频/双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817.json, 视频生成/文生视频/双bf16满血版8步加速lora 1.0 sage MinimaxH3文生视频图生视频_2088389915884220418.json, 视频生成/文生视频/双bf16满血版8步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088362225546391554.json, 视频生成/文生视频/双bf16满血版sage无损加速｜MinimaxH3文生图生视频生视频_2088371118150340610.json, 视频生成/文生视频/双bf16满血版｜MinimaxH3 8步lora 1.0+sage加速视频生成_2089460273106210818.json, 视频生成/文生视频/双时钟8步lora极速4分钟出15秒480P｜Minimax-H3文生视频工作流_2087215608109821953.json, 视频生成/文生视频/多参考打斗视频生成｜MiniMax H3 BF16 768P lora_2095944735889383425.json, 视频生成/文生视频/多参考真实打斗生成｜MiniMax H3 Dasiwa 768P lora_2095940373528014850.json, 视频生成/文生视频/开源版8步极速｜MiniMax H3文生视频跳舞创意_2093813895210299394.json, 视频生成/文生视频/开源版文生视频8步极速｜Minimax H3跳舞短剧漫剧创意生成_2095558045421101058.json, 视频生成/文生视频/微表情10秒768P模板｜Minimax H3剪枝版BF16视频_2090893466330030082.json, 视频生成/文生视频/极致满血1K 10秒模板｜Minimax H3多参双bf16加sage加速25步_2088754648592248834.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json、视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json、视频生成/文生视频/minimax三图工作流｜文生图生视频一键生成_2091309114570919938.json、视频生成/文生视频/sage无损加速双bf16满血版MinimaxH3文生视频图生视频极致清晰_2088396155074990082.json、视频生成/文生视频/sage无损加速｜MinimaxH3双bf16满血版文生图生视频全能_2089463275493875714.json…）

- **类型**：Text To Image
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 31 个 workflow 都包含：
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
- `ResolutionSelector` —— 30/31 个有
- `孤海注释` —— 30/31 个有
- `CR Prompt Text` —— 29/31 个有
- `LoadImage` —— 26/31 个有
- `BasicScheduler` —— 24/31 个有
- `KSamplerSelect` —— 24/31 个有
- `LayerUtility: PurgeVRAM V2` —— 12/31 个有
- `LoraLoaderBypassModelOnly` —— 8/31 个有
- `MiniMaxH3DualClockSamplerT8` —— 8/31 个有
- `ModelAttentionBackend` —— 4/31 个有
- `LTXVConcatAVLatent` —— 3/31 个有
- `LTXVSeparateAVLatent` —— 3/31 个有
- `MinimaxH3LatentUpscaler3D` —— 3/31 个有
- `CR Text` —— 1/31 个有
- `ImageResizeKJv2` —— 1/31 个有
- `Int` —— 1/31 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/31 个有
- `PT_H3ConcatAVLatent` —— 1/31 个有
- `SaveImage` —— 1/31 个有
- `Text Multiline` —— 1/31 个有
- `VAEEncode` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 31 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 31 | 100% |
| 采样算法 | er_sde | - | 31 | 100% |
| 调度器 | beta | - | 31 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 31 | 100% |
| 宽度 | 80 | 80 - 80 | 31 | 100% |
| 高度 | 80 | 80 - 80 | 31 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/31 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，31 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，31 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，31 个样本，一致性 100%
- 调度器 最常用 beta，31 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，31 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，31 个样本，取值集中（一致性 100%）
- 高发问题（31/31 个样本）：Steps较低可能导致细节不足

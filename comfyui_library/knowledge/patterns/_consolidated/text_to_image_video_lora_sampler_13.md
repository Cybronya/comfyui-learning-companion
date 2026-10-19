---
name: text_to_image_video_lora_sampler_13
type: Text To Image
frequency: 25
level: strong
coverage: 0.90052
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [ShowAnything|Mie, CR Prompt Text]
members: [视频生成/文生视频/Minimax_H3开源版8步极速文生视频｜600步新加速LORA加持｜短剧漫剧场景特效角色设计全能_2104444733849423874.json, 视频生成/文生视频/Minimax双时钟加速版图生视频文生视频生成_2088175309471444994.json, 视频生成/文生视频/h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086259776987684865.json, 视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json, 视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json, 视频生成/文生视频/minimax三图工作流｜文生图生视频一键生成_2091309114570919938.json, 视频生成/文生视频/八步极速Minimax H3开源版 短剧漫剧创意视频新加速lora_2098305874950443010.json, 视频生成/文生视频/加速版单采参考生视频｜MiniMax H3长视频直出_2101171837278449665.json, 视频生成/文生视频/参考生成多模态视频｜Minimax H3文生视频生视频_2095567468348661762.json, 视频生成/文生视频/参考生成文生图生视频生视频｜Minimax H3视频生成工作流_2088390683336994818.json, 视频生成/文生视频/双时钟8步lora极速2分钟出5秒｜Minimax-H3图生多参生视频工作流_2087191069569146881.json, 视频生成/文生视频/开源版8步极速｜MiniMax H3文生视频跳舞创意_2093813895210299394.json, 视频生成/文生视频/开源版文生视频8步极速｜Minimax H3跳舞短剧漫剧创意生成_2095558045421101058.json, 视频生成/文生视频/极速8步开源版｜MiniMax H3跳舞漫剧角色表演文生视频_2093768920888074242.json, 视频生成/文生视频/短剧漫剧创意视频｜Minimax H3开源版8步极速文生视频（600步新加速LORA）_2090842404969598977.json, 视频生成/文生视频/短剧漫剧文生视频｜Minimax H3开源8步极速，600步新加速LORA_2099884404595314689.json, 视频生成/文生视频/短剧漫剧文生视频｜Minimax H3开源8步极速，600步新加速LORA_2104930009243799553.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2094027470818332673.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2097107105957367810.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2098918238603272193.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2106165786128773121.json, 视频生成/文生视频/跳舞短剧漫剧视频生成｜8步极速高质量文生视频_2095939063923691522.json, 视频生成/视频生视频/MiniMax H3视频复刻视频编辑视频翻拍二创与指定角色替换长视频直出方案_2106075579454943233.json, 视频生成/视频生视频/MiniMax H3视频复刻角色替换二创翻拍工作流_视频生视频图生视频方案_2106616300503134209.json, 视频生成/视频生视频/MiniMax_H3视频复刻加速版_数字人参考生视频与长视频直出工作流_2106181004804317185.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/文生视频/Minimax_H3开源版8步极速文生视频｜600步新加速LORA加持｜短剧漫剧场景特效角色设计全能_2104444733849423874.json、视频生成/文生视频/Minimax双时钟加速版图生视频文生视频生成_2088175309471444994.json、视频生成/文生视频/h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086259776987684865.json、视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json、视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 25 个 workflow 都包含：
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
- `LoraLoaderBypassModelOnly` —— 24/25 个有
- `MiniMaxH3DualClockSamplerT8` —— 24/25 个有
- `ResolutionSelector` —— 24/25 个有
- `CR Prompt Text` —— 23/25 个有
- `ModelAttentionBackend` —— 20/25 个有
- `孤海注释` —— 20/25 个有
- `LoadImage` —— 11/25 个有
- `LoadAudio` —— 4/25 个有
- `LoadVideo` —— 4/25 个有
- `SaveImage` —— 4/25 个有
- `SolAttnMiniMax` —— 4/25 个有
- `VHS_LoadVideo` —— 4/25 个有
- `GetVideoComponents` —— 2/25 个有
- `Int` —— 2/25 个有
- `PreviewImage` —— 2/25 个有
- `CR Text` —— 1/25 个有
- `DA3Inference` —— 1/25 个有
- `DA3Render` —— 1/25 个有
- `EmptyImage` —— 1/25 个有
- `ImageScaleToTotalPixels` —— 1/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/25 个有
- `LoadDA3Model` —— 1/25 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/25 个有
- `PrimitiveStringMultiline` —— 1/25 个有
- `ShowAnything|Mie` —— 1/25 个有
- `VHS_LoadVideoFFmpeg` —— 1/25 个有
- `VHS_VideoInfo` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高发问题（25/25 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ShowAnything|Mie、CR Prompt Text

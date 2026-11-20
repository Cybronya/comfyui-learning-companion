---
name: text_to_image_video_lora_sampler_50
type: Text To Image
frequency: 16
level: strong
coverage: 0.89975
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax_H3开源版8步极速文生视频｜600步新加速LORA加持｜短剧漫剧场景特效角色设计全能_2104444733849423874.json, 视频生成/文生视频/Minimax双时钟加速版图生视频文生视频生成_2088175309471444994.json, 视频生成/文生视频/h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086259776987684865.json, 视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json, 视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json, 视频生成/文生视频/minimax三图工作流｜文生图生视频一键生成_2091309114570919938.json, 视频生成/文生视频/八步极速Minimax H3开源版 短剧漫剧创意视频新加速lora_2098305874950443010.json, 视频生成/文生视频/加速版单采参考生视频｜MiniMax H3长视频直出_2101171837278449665.json, 视频生成/文生视频/参考生成多模态视频｜Minimax H3文生视频生视频_2095567468348661762.json, 视频生成/文生视频/参考生成文生图生视频生视频｜Minimax H3视频生成工作流_2088390683336994818.json, 视频生成/文生视频/双时钟8步lora极速2分钟出5秒｜Minimax-H3图生多参生视频工作流_2087191069569146881.json, 视频生成/文生视频/双时钟8步lora极速4分钟出15秒480P｜Minimax-H3文生视频工作流_2087215608109821953.json, 视频生成/文生视频/开源版8步极速｜MiniMax H3文生视频跳舞创意_2093813895210299394.json, 视频生成/文生视频/开源版文生视频8步极速｜Minimax H3跳舞短剧漫剧创意生成_2095558045421101058.json, 视频生成/视频生视频/MiniMax H3视频复刻视频编辑视频翻拍二创与指定角色替换长视频直出方案_2106075579454943233.json, 视频生成/视频生视频/MiniMax H3视频复刻角色替换二创翻拍工作流，视频生视频图生视频方案_2106616300503134209.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/Minimax_H3开源版8步极速文生视频｜600步新加速LORA加持｜短剧漫剧场景特效角色设计全能_2104444733849423874.json、视频生成/文生视频/Minimax双时钟加速版图生视频文生视频生成_2088175309471444994.json、视频生成/文生视频/h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086259776987684865.json、视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json、视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
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
- `LoraLoaderBypassModelOnly` —— 15/16 个有
- `MiniMaxH3DualClockSamplerT8` —— 15/16 个有
- `ResolutionSelector` —— 15/16 个有
- `CR Prompt Text` —— 14/16 个有
- `孤海注释` —— 13/16 个有
- `LoadImage` —— 10/16 个有
- `ModelAttentionBackend` —— 10/16 个有
- `LoadAudio` —— 4/16 个有
- `LoadVideo` —— 4/16 个有
- `SaveImage` —— 3/16 个有
- `SolAttnMiniMax` —— 3/16 个有
- `VHS_LoadVideo` —— 3/16 个有
- `GetVideoComponents` —— 2/16 个有
- `Int` —— 2/16 个有
- `CR Text` —— 1/16 个有
- `DA3Inference` —— 1/16 个有
- `DA3Render` —— 1/16 个有
- `EmptyImage` —— 1/16 个有
- `ImageScaleToTotalPixels` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `LoadDA3Model` —— 1/16 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `ShowAnything|Mie` —— 1/16 个有
- `VHS_LoadVideoFFmpeg` —— 1/16 个有
- `VHS_VideoInfo` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足

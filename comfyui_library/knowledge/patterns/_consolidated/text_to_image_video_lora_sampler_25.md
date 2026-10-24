---
name: text_to_image_video_lora_sampler_25
type: Text To Image
frequency: 22
level: strong
coverage: 0.776273
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3DualClockT8GH, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/短剧漫剧真人剧输出｜MiniMax H3多参视频含反推提示词_2093121382308732930.json, 视频生成/图生视频/MiniMax H3图生视频工作流｜一站式图生视频创作助手_2106919593049681922.json, 视频生成/图生视频/MiniMax-H3二采分块工作流｜1080p视频直出图生视频_2097821235857154050.json, 视频生成/图生视频/MiniMax-H3孤海V3｜图生视频风格化｜孤海同款氛围出片_2104825908111691777.json, 视频生成/图生视频/多图编辑多合一｜海螺H3文生图生视频换背景_2090937623283060738.json, 视频生成/图生视频/多图编辑海螺H3文生图生视频视频多合一_2090640704577040386.json, 视频生成/图生视频/智能一体化创作｜MiniMax H3图生视频生成_2091802297490829313.json, 视频生成/图生视频/智能一体化视频创作｜MiniMax H3图生视频直出_2091302697143201794.json, 视频生成/图生视频/智能一体化视频创作｜MiniMax H3图生视频直出_2091640143630393346.json, 视频生成/图生视频/海螺H3文生图生视频视频编辑多合一_2091424745895059457.json, 视频生成/图生视频/短剧漫剧真人剧多参输出｜MiniMax H3开源图生视频_2093087226048638977.json, 视频生成/文生视频/30S极简多合一｜图生文生视频编辑海螺H3孤海版_2093488975238483970.json, 视频生成/文生视频/30秒全能加速生成｜MinimaxH3开源免费GH版视频_2093487368002166786.json, 视频生成/文生视频/FZ-MinimaxH3智能一体化视频生成｜多模式一站式工作流_2097114457708257281.json, 视频生成/文生视频/H3二采分块4K直出 低显存高清视频生成工具_2099952624308150274.json, 视频生成/文生视频/H3二采分块4K直出_低显存高清视频生成工具_2100425597511098370.json, 视频生成/文生视频/H3二采分块4K直出改进版 超高清视频分块生成_2099230889371852801.json, 视频生成/文生视频/H3智能一体化视频创作 显存优化低显存适配_2100686659913338882.json, 视频生成/文生视频/MiniMax H3 4K超高清直出视频生成_2098122098672750593.json, 视频生成/文生视频/MiniMax H3二采分块2K4K直出视频生成处理工具_2101387456988934145.json, 视频生成/文生视频/MiniMax-H3二采分块4K直出｜文生图生视频生成_2097824262739550210.json, 视频生成/文生视频/MiniMax-H3智能创作平台｜二采分块4K视频直出工作流_2097822736394571778.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/短剧漫剧真人剧输出｜MiniMax H3多参视频含反推提示词_2093121382308732930.json、视频生成/图生视频/MiniMax H3图生视频工作流｜一站式图生视频创作助手_2106919593049681922.json、视频生成/图生视频/MiniMax-H3二采分块工作流｜1080p视频直出图生视频_2097821235857154050.json、视频生成/图生视频/MiniMax-H3孤海V3｜图生视频风格化｜孤海同款氛围出片_2104825908111691777.json、视频生成/图生视频/多图编辑多合一｜海螺H3文生图生视频换背景_2090937623283060738.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3DualClockT8GH`
- `MiniMaxH3IntegrationAdapterGH`
- `MiniMaxH3IntegrationGH`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 21/22 个有
- `MiniMaxH3AVDecodeT8GH` —— 21/22 个有
- `SetNode` —— 21/22 个有
- `easy ifElse` —— 21/22 个有
- `LoraLoaderBypassModelOnly` —— 20/22 个有
- `easy anythingIndexSwitch` —— 20/22 个有
- `孤海注释` —— 19/22 个有
- `SaveImage` —— 10/22 个有
- `ColorCorrect` —— 9/22 个有
- `GoohaiAnyExists` —— 9/22 个有
- `GoohaiMinimaxH3LatentUpscalerGH` —— 9/22 个有
- `GoohaiMinimaxH3TiledSampler` —— 9/22 个有
- `GoohaiUniversalSlider` —— 9/22 个有
- `SplitSigmas` —— 9/22 个有
- `MiniMaxH3AVDecodeT8` —— 5/22 个有
- `LoadImage` —— 3/22 个有
- `CM_FloatToInt` —— 1/22 个有
- `EmptyImage` —— 1/22 个有
- `PreviewImage` —— 1/22 个有
- `PrimitiveFloat` —— 1/22 个有
- `SaveAudioAdvanced` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（23/22 个样本）：Steps较低可能导致细节不足

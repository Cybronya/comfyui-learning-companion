---
name: text_to_image_video_lora_sampler_66
type: Text To Image
frequency: 11
level: strong
coverage: 0.794727
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3DualClockT8GH, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3图生视频工作流｜一站式图生视频创作助手_2106919593049681922.json, 视频生成/图生视频/多图编辑多合一｜海螺H3文生图生视频换背景_2090937623283060738.json, 视频生成/图生视频/多图编辑海螺H3文生图生视频视频多合一_2090640704577040386.json, 视频生成/图生视频/智能一体化创作｜MiniMax H3图生视频生成_2091802297490829313.json, 视频生成/图生视频/智能一体化视频创作｜MiniMax H3图生视频直出_2091302697143201794.json, 视频生成/图生视频/智能一体化视频创作｜MiniMax H3图生视频直出_2091640143630393346.json, 视频生成/图生视频/海螺H3文生图生视频视频编辑多合一_2091424745895059457.json, 视频生成/图生视频/短剧漫剧真人剧多参输出｜MiniMax H3开源图生视频_2093087226048638977.json, 视频生成/文生视频/30S极简多合一｜图生文生视频编辑海螺H3孤海版_2093488975238483970.json, 视频生成/文生视频/30秒全能加速生成｜MinimaxH3开源免费GH版视频_2093487368002166786.json, 视频生成/文生视频/ComfyUI多轮对话Skill加载｜配合MiniMax-H3智能工作台_2092077272688844801.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频工作流｜一站式图生视频创作助手_2106919593049681922.json、视频生成/图生视频/多图编辑多合一｜海螺H3文生图生视频换背景_2090937623283060738.json、视频生成/图生视频/多图编辑海螺H3文生图生视频视频多合一_2090640704577040386.json、视频生成/图生视频/智能一体化创作｜MiniMax H3图生视频生成_2091802297490829313.json、视频生成/图生视频/智能一体化视频创作｜MiniMax H3图生视频直出_2091302697143201794.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 11 个 workflow 都包含：
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
- `GetNode` —— 10/11 个有
- `LoraLoaderBypassModelOnly` —— 10/11 个有
- `MiniMaxH3AVDecodeT8GH` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `easy anythingIndexSwitch` —— 10/11 个有
- `easy ifElse` —— 10/11 个有
- `孤海注释` —— 9/11 个有
- `MiniMaxH3AVDecodeT8` —— 5/11 个有
- `LoadImage` —— 4/11 个有
- `DapaoAPIChatMaterialLibraryNode` —— 1/11 个有
- `DapaoAPIChatSettingsNode` —— 1/11 个有
- `DapaoAPILLMConfigNode` —— 1/11 个有
- `DapaoAPIMultiTurnChatNode` —— 1/11 个有
- `DapaoAPISkillLoaderNode` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `LoadVideo` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `PrimitiveString` —— 1/11 个有
- `SaveAudioAdvanced` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足

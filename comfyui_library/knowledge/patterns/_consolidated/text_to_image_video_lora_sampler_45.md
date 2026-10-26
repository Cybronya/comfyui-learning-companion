---
name: text_to_image_video_lora_sampler_45
type: Text To Image
frequency: 16
level: strong
coverage: 0.793375
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax_H3图生视频工作流｜一站式图生视频创作助手_2107988610166386690.json, 视频生成/文生视频/minimax-h3-全能参考一体化｜视频处理一键生成_2094347305259462658.json, 视频生成/文生视频/minimax-h3全能参考一体化｜视频处理一键生成_2094579504961380354.json, 视频生成/文生视频/三毛｜海螺H3文生图生视频视频编辑多合一_2090635560917495810.json, 视频生成/文生视频/优化版智能一体化视频创作｜MiniMax H3文生图生视频全能_2090817057096032257.json, 视频生成/文生视频/全能参考一体化 minimax-h3 音色形象多模态生成_2094225088278261762.json, 视频生成/文生视频/反推提示词加持｜MiniMax H3多参短剧漫剧输出_2096577354117238785.json, 视频生成/文生视频/图+音输入模式｜MiniMaxH3三模视频一键生成_2094029502358843394.json, 视频生成/文生视频/图音结合生成｜MiniMaxH3文生视频视频生视频_2093809557423349762.json, 视频生成/文生视频/孤海大佬版极简流｜海螺H3文生图生视频视频编辑多合一_2090140481610149889.json, 视频生成/文生视频/开源免费GH版加速全能版｜MinimaxH3文生图生视频生视频工作流_2088321737384615938.json, 视频生成/文生视频/智能一体化视频创作MiniMax H3文生视频图生视频视频生视频整合节点_2088374872840957953.json, 视频生成/文生视频/智能一体化视频创作｜MiniMax H3文生图生视频生视频工作流_2088343730972618753.json, 视频生成/文生视频/短剧漫剧真人剧输出｜MiniMax H3多参视频反推提示词_2096340060219207682.json, 视频生成/文生视频/短剧漫剧真人剧输出｜MiniMax H3多参视频含反推提示词_2096079215232897025.json, 视频生成/文生视频/视频创作一体化最优版｜MiniMax H3智能生成多模式_2090832029570129922.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_45

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3图生视频工作流｜一站式图生视频创作助手_2107988610166386690.json、视频生成/文生视频/minimax-h3-全能参考一体化｜视频处理一键生成_2094347305259462658.json、视频生成/文生视频/minimax-h3全能参考一体化｜视频处理一键生成_2094579504961380354.json、视频生成/文生视频/三毛｜海螺H3文生图生视频视频编辑多合一_2090635560917495810.json、视频生成/文生视频/优化版智能一体化视频创作｜MiniMax H3文生图生视频全能_2090817057096032257.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
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
- `GetNode` —— 15/16 个有
- `LoraLoaderBypassModelOnly` —— 15/16 个有
- `SetNode` —— 15/16 个有
- `easy ifElse` —— 15/16 个有
- `孤海注释` —— 14/16 个有
- `MiniMaxH3AVDecodeT8GH` —— 13/16 个有
- `MiniMaxH3DualClockT8GH` —— 13/16 个有
- `easy anythingIndexSwitch` —— 12/16 个有
- `MiniMaxH3AVDecodeT8` —— 5/16 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/16 个有
- `PlaySound|pysssss` —— 3/16 个有
- `SaveAudioAdvanced` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `LoadImage` —— 2/16 个有
- `PreviewAudio` —— 2/16 个有
- `RH_RhartImageG2OfficialImageToImage` —— 2/16 个有
- `RH_RhartImageG2OfficialTextToImage` —— 2/16 个有
- `SaveImage` —— 2/16 个有
- `VHS_LoadVideo` —— 2/16 个有
- `EmptyImage` —— 1/16 个有
- `PreviewImage` —— 1/16 个有

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
| Steps较低可能导致细节不足 | 19/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（19/16 个样本）：Steps较低可能导致细节不足

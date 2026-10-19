---
name: text_to_image_lora_sampler_clip_84
type: Text To Image
frequency: 10
level: strong
coverage: 0.9148
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadVideo, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/数字人口型同步神器｜口型语音精准对齐不穿帮_2106622328892379137.json, 视频生成/图生视频/Wan3万相多模态全参工作流｜图生视频视频生视频双模式_2108017535508639745.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099201072412848129.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099599137611272193.json, 视频生成/图生视频/Wan3多模态全参工作流_2109966575624351745.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2106855204628025346.json, 视频生成/图生视频/Wan3多模态全参工作流｜视频生视频图生视频_2095092856275951617.json, 视频生成/图生视频/参考生视频｜RH万相3.0视频生视频图生视频_2092209020676427778.json, 视频生成/图生视频/爆款短视频复刻｜一张图动作运镜节奏一键迁移MiniMax H3_2089825604421115906.json, 视频生成/文生视频/30秒直出低价版｜Wan3.0全能参考生视频生成_2093213787812876289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/数字人口型同步神器｜口型语音精准对齐不穿帮_2106622328892379137.json、视频生成/图生视频/Wan3万相多模态全参工作流｜图生视频视频生视频双模式_2108017535508639745.json、视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099201072412848129.json、视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099599137611272193.json、视频生成/图生视频/Wan3多模态全参工作流_2109966575624351745.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 8/10 个有
- `Text` —— 7/10 个有
- `SaveImage` —— 4/10 个有
- `CreateVideo` —— 2/10 个有
- `FL_CosyVoice3_ModelLoader` —— 1/10 个有
- `FL_CosyVoice3_ZeroShot` —— 1/10 个有
- `GetVideoComponents` —— 1/10 个有
- `LatentSyncNode` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `RHMiniMaxH3RefGen` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

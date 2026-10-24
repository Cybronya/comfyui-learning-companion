---
name: text_to_image_lora_sampler_clip_142
type: Text To Image
frequency: 11
level: strong
coverage: 0.916727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/数字人口型同步神器｜口型语音精准对齐不穿帮_2106622328892379137.json, 视频生成/图生视频/MiniMax H3全能参考｜图音视频多素材再生工作流_2095255547141509121.json, 视频生成/图生视频/Wan3.0参考生视频｜数字人动作迁移图生视频_2092056807425531906.json, 视频生成/图生视频/Wan3.0多参生视频｜多图参考图生视频_2097903742090825729.json, 视频生成/图生视频/Wan3万相多模态全参工作流｜图生视频视频生视频双模式_2108017535508639745.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099201072412848129.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099599137611272193.json, 视频生成/图生视频/Wan3多模态全参工作流_2109966575624351745.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2106855204628025346.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2110206029798662146.json, 视频生成/图生视频/Wan3多模态全参工作流｜视频生视频图生视频_2095092856275951617.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/数字人口型同步神器｜口型语音精准对齐不穿帮_2106622328892379137.json、视频生成/图生视频/MiniMax H3全能参考｜图音视频多素材再生工作流_2095255547141509121.json、视频生成/图生视频/Wan3.0参考生视频｜数字人动作迁移图生视频_2092056807425531906.json、视频生成/图生视频/Wan3.0多参生视频｜多图参考图生视频_2097903742090825729.json、视频生成/图生视频/Wan3万相多模态全参工作流｜图生视频视频生视频双模式_2108017535508639745.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `LoadVideo` —— 9/11 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 9/11 个有
- `孤海注释` —— 9/11 个有
- `Text` —— 7/11 个有
- `SaveImage` —— 5/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `CreateVideo` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `FL_CosyVoice3_ModelLoader` —— 1/11 个有
- `FL_CosyVoice3_ZeroShot` —— 1/11 个有
- `GetVideoComponents` —— 1/11 个有
- `LatentSyncNode` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/11 个有

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
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足

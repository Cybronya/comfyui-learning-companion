---
name: text_to_image_lora_sampler_clip_66
type: Text To Image
frequency: 16
level: strong
coverage: 0.91825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/视频超分工作流_2101989284810153986.json, 数字人/数字人/AI视频换人动作迁移 角色替换数字人视频生成_2094258030903906306.json, 数字人/数字人/AI视频换人神器｜动作迁移加角色替换一键完成_2106586431224377346.json, 数字人/数字人/DLSS5视频图片超分辨率 Video Image Super Resolution增强_2098709137747169282.json, 数字人/数字人/数字人口播Pro高清形象视频｜专业级形象生成工作流_2097037549385633794.json, 数字人/数字人/数字人口播Pro高清版｜形象视频清晰度再上一档_2097216696036708353.json, 视频生成/图生视频/Wan3.0参考生视频｜数字人动作迁移图生视频_2092056807425531906.json, 视频生成/图生视频/Wan3万相多模态全参工作流｜图生视频视频生视频双模式_2108017535508639745.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099201072412848129.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099599137611272193.json, 视频生成/图生视频/Wan3多模态全参工作流 视频生视频图生视频处理工具_2113376426140454913.json, 视频生成/图生视频/Wan3多模态全参工作流_2109966575624351745.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2106855204628025346.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2110206029798662146.json, 视频生成/图生视频/Wan3多模态全参工作流｜视频生视频图生视频_2095092856275951617.json, 视频生成/图生视频/Wan3多模态全参工作流｜视频生视频图生视频多模态上阵_2114247022919376897.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/视频超分工作流_2101989284810153986.json、数字人/数字人/AI视频换人动作迁移 角色替换数字人视频生成_2094258030903906306.json、数字人/数字人/AI视频换人神器｜动作迁移加角色替换一键完成_2106586431224377346.json、数字人/数字人/DLSS5视频图片超分辨率 Video Image Super Resolution增强_2098709137747169282.json、数字人/数字人/数字人口播Pro高清形象视频｜专业级形象生成工作流_2097037549385633794.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
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
- `LoadImage` —— 15/16 个有
- `LoadVideo` —— 13/16 个有
- `孤海注释` —— 13/16 个有
- `LoadAudio` —— 12/16 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 10/16 个有
- `Text` —— 9/16 个有
- `SaveImage` —— 8/16 个有
- `RHBerniniFullReferenceVideoToVideo` —— 2/16 个有
- `RH_KlingV2AiAvatarProImageAudioToVideo` —— 2/16 个有
- `EmptyImage` —— 1/16 个有
- `Image Comparer (rgthree)` —— 1/16 个有
- `JWInteger` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `RH_Astra` —— 1/16 个有
- `RH_DLSS5Enhance` —— 1/16 个有

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

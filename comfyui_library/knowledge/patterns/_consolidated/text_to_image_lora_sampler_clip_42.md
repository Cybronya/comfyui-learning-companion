---
name: text_to_image_lora_sampler_clip_42
type: Text To Image
frequency: 17
level: strong
coverage: 0.901647
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan3.0参考生视频｜数字人动作迁移图生视频_2092056807425531906.json, 视频生成/图生视频/Wan3.0图生视频｜数字人动作迁移一键生成_2092054082633687041.json, 视频生成/图生视频/Wan3.0多参生视频工作流｜全模态素材参考生成_2097845652163227650.json, 视频生成/图生视频/Wan3.0多参生视频｜多图参考图生视频_2097903742090825729.json, 视频生成/图生视频/Wan3.0首尾帧生视频｜图生视频一键生成直出_2092032397171838978.json, 视频生成/图生视频/Wan3万相多模态全参工作流｜图生视频视频生视频双模式_2108017535508639745.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099201072412848129.json, 视频生成/图生视频/Wan3多模态全参工作流 文生视频图生视频全能创作_2099599137611272193.json, 视频生成/图生视频/Wan3多模态全参工作流_2109966575624351745.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2106855204628025346.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2110206029798662146.json, 视频生成/图生视频/Wan3多模态全参工作流｜视频生视频图生视频_2095092856275951617.json, 视频生成/图生视频/wan3.0多参考图生视频｜图生视频一键直出_2092045899554971650.json, 视频生成/图生视频/全能视频图生视频低价版6-30秒处理生成工具_2102169806098231298.json, 视频生成/图生视频/动作迁移角色替换AI视频换人｜免改骨架直接换主角｜图生视频_2101892897812606978.json, 视频生成/图生视频/参考生视频｜RH万相3.0视频生视频图生视频_2092209020676427778.json, 视频生成/文生视频/30秒直出低价版｜Wan3.0全能参考生视频生成_2093213787812876289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/Wan3.0参考生视频｜数字人动作迁移图生视频_2092056807425531906.json、视频生成/图生视频/Wan3.0图生视频｜数字人动作迁移一键生成_2092054082633687041.json、视频生成/图生视频/Wan3.0多参生视频工作流｜全模态素材参考生成_2097845652163227650.json、视频生成/图生视频/Wan3.0多参生视频｜多图参考图生视频_2097903742090825729.json、视频生成/图生视频/Wan3.0首尾帧生视频｜图生视频一键生成直出_2092032397171838978.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 15/17 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 13/17 个有
- `LoadAudio` —— 10/17 个有
- `LoadVideo` —— 10/17 个有
- `Text` —— 8/17 个有
- `SaveImage` —— 7/17 个有
- `PrimitiveStringMultiline` —— 3/17 个有
- `EmptyImage` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `RH_AlibabaWan30ImageToVideo` —— 2/17 个有
- `RHBerniniFullReferenceVideoToVideo` —— 1/17 个有
- `RH_RhartVideoGImageToVideo` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_127
type: Text To Image
frequency: 7
level: strong
coverage: 0.892143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Text]
members: [图片生成/图生图/2102571193546133506.json, 图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json, 数字人/数字人/数字人口播Pro高清形象视频｜专业级形象生成工作流_2097037549385633794.json, 数字人/数字人/数字人口播Pro高清版｜形象视频清晰度再上一档_2097216696036708353.json, 视频生成/图生视频/Wan3.0参考生视频｜数字人动作迁移图生视频_2092056807425531906.json, 视频生成/图生视频/Wan3.0多参生视频工作流｜全模态素材参考生成_2097845652163227650.json, 视频生成/图生视频/Wan3.0多参生视频｜多图参考图生视频_2097903742090825729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102571193546133506.json、图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json、数字人/数字人/数字人口播Pro高清形象视频｜专业级形象生成工作流_2097037549385633794.json、数字人/数字人/数字人口播Pro高清版｜形象视频清晰度再上一档_2097216696036708353.json、视频生成/图生视频/Wan3.0参考生视频｜数字人动作迁移图生视频_2092056807425531906.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `LoadAudio` —— 4/7 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `RH_KlingV2AiAvatarProImageAudioToVideo` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `FishS2VoiceCloneTTS` —— 1/7 个有
- `LoadWhisperModel_` —— 1/7 个有
- `RH_RhartVideoSparkvideo20MiniImageToVideo` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `WhisperTranscribe_` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text

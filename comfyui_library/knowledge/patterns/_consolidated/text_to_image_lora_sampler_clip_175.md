---
name: text_to_image_lora_sampler_clip_175
type: Text To Image
frequency: 10
level: strong
coverage: 0.886
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频工作流｜可灵3.0 Pro多镜头最长十五秒_2100838268672757761.json, 视频生成/图生视频/图生视频首尾帧RH MiniMax-H3-Max-Turbo极速版｜锁定首尾流畅过渡_2101918968226340866.json, 视频生成/图生视频/数字人口播Pro｜照片加音频生成口播视频，带货讲解必备_2099896728131559426.json, 视频生成/图生视频/旗舰模型图片动起来｜H3 MAX图生视频工作流_2095861857969074178.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频生成_2093247372666167298.json, 视频生成/文生视频/30秒长视频多模态生成｜seedance2.5文生图生视频_2093081229213126657.json, 视频生成/文生视频/30秒长视频多模态｜seedance2.5文生图生视频生成_2093245885135286273.json, 视频生成/文生视频/Seedance2.5多模态视频全构｜文生视频图生视频视频生视频｜三通道齐活_2102299674853076994.json, 视频生成/文生视频/宽审多图多视频参考｜pipi-Seedance2.0-global生成_2095579714701316098.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_175

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/图生视频工作流｜可灵3.0 Pro多镜头最长十五秒_2100838268672757761.json、视频生成/图生视频/图生视频首尾帧RH MiniMax-H3-Max-Turbo极速版｜锁定首尾流畅过渡_2101918968226340866.json、视频生成/图生视频/数字人口播Pro｜照片加音频生成口播视频，带货讲解必备_2099896728131559426.json、视频生成/图生视频/旗舰模型图片动起来｜H3 MAX图生视频工作流_2095861857969074178.json、视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `CR Text` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `LoadVideo` —— 4/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 3/10 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 2/10 个有
- `RH_BytedanceSeedance20GlobalMultimodalVideo` —— 1/10 个有
- `RH_KlingV2AiAvatarProImageAudioToVideo` —— 1/10 个有
- `RH_KlingV30ProImageToVideo` —— 1/10 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 1/10 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 1/10 个有

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

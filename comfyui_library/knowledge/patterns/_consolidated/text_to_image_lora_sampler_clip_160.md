---
name: text_to_image_lora_sampler_clip_160
type: Text To Image
frequency: 11
level: strong
coverage: 0.888273
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频生成_2093247372666167298.json, 视频生成/文生视频/30秒直出低价版｜Wan3.0全能参考生视频生成_2093213787812876289.json, 视频生成/文生视频/30秒长视频多模态生成｜seedance2.5文生图生视频_2093081229213126657.json, 视频生成/文生视频/30秒长视频多模态｜seedance2.5文生图生视频生成_2093245885135286273.json, 视频生成/文生视频/Mini多模态视频生成｜Seedance2.0文生视频生视频_2095871844741111809.json, 视频生成/文生视频/Seedance 2.0 Global Fast多模态全能参考视频｜4K文图视频参考_2097977539267489794.json, 视频生成/文生视频/Seedance 2.0 Global Mini多模态全能参考视频｜4K文图视频参考全支持_2097900436190752770.json, 视频生成/文生视频/Seedance2.0 Mini多模态｜文生图生视频全都能跑_2106629854375534594.json, 视频生成/文生视频/多模态全能视频生成｜Seedance 2.5文生图生视频生视频工作流_2088341212158840834.json, 视频生成/文生视频/宽审多图多视频参考｜pipi-Seedance2.0-global生成_2095579714701316098.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_160

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json、视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频生成_2093247372666167298.json、视频生成/文生视频/30秒直出低价版｜Wan3.0全能参考生视频生成_2093213787812876289.json、视频生成/文生视频/30秒长视频多模态生成｜seedance2.5文生图生视频_2093081229213126657.json、视频生成/文生视频/30秒长视频多模态｜seedance2.5文生图生视频生成_2093245885135286273.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 9/11 个有
- `LoadAudio` —— 7/11 个有
- `CR Text` —— 5/11 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 3/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 2/11 个有
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo` —— 2/11 个有
- `Text` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 1/11 个有
- `RH_BytedanceSeedance20GlobalFastMultimodalVideo` —— 1/11 个有
- `RH_BytedanceSeedance20GlobalMiniMultimodalVideo` —— 1/11 个有
- `RH_BytedanceSeedance20GlobalMultimodalVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足

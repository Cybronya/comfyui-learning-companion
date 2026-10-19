---
name: text_to_image_lora_sampler_clip_30
type: Text To Image
frequency: 17
level: strong
coverage: 0.930176
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3两段式管线｜图生视频高清直出_2098701054606135298.json, 视频生成/图生视频/MiniMax H3全能参考｜图音视频多素材再生工作流_2095255547141509121.json, 视频生成/图生视频/SD2.5全能参考全参数版｜图生视频自由调控_2098757736740769793.json, 视频生成/图生视频/Seedance 2.5全参可调｜图生视频视频生视频一步到位_2099871193108140034.json, 视频生成/图生视频/Seedance 2.5全参工作流全参数输入视频生成，视频生视频图生视频方案_2105808093924909057.json, 视频生成/图生视频/Seedance 2.5全参工作流，视频生视频图生视频全覆盖方案_2106570538192822274.json, 视频生成/图生视频/Seedance 2.5动作迁移，人物场景特效图生视频_2111225027298414593.json, 视频生成/图生视频/Seedance2.5全参图生视频工作流｜视频生视频稳定出新_2108014164991102978.json, 视频生成/图生视频/Seedance2.5全参工作流｜视频生视频图生视频一网打尽_2100757319570247682.json, 视频生成/图生视频/Seedance2.5全参工作流｜视频生视频图生视频全能_2089422276826583041.json, 视频生成/图生视频/Seedance2.5全参工作流｜视频生视频图生视频全能生成_2097053723100008450.json, 视频生成/图生视频/Seedance2.5全参数视频工作流 图生视频与视频生视频_2098285496450510850.json, 视频生成/图生视频/全参工作流｜Seedance2.5视频生视频图生视频_2090599945182212098.json, 视频生成/图生视频/全参视频工作流｜Seedance2.5图生视频生视频直出_2093483002692198401.json, 视频生成/图生视频/博主直播带货照片开口卖货 数字人口播视频生成_2099915240774389761.json, 视频生成/文生视频/30秒长视频多模态生成｜seedance2.5文生图生视频_2093081229213126657.json, 视频生成/文生视频/30秒长视频多模态｜seedance2.5文生图生视频生成_2093245885135286273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3两段式管线｜图生视频高清直出_2098701054606135298.json、视频生成/图生视频/MiniMax H3全能参考｜图音视频多素材再生工作流_2095255547141509121.json、视频生成/图生视频/SD2.5全能参考全参数版｜图生视频自由调控_2098757736740769793.json、视频生成/图生视频/Seedance 2.5全参可调｜图生视频视频生视频一步到位_2099871193108140034.json、视频生成/图生视频/Seedance 2.5全参工作流全参数输入视频生成，视频生视频图生视频方案_2105808093924909057.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：93%

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 15/17 个有
- `LoadVideo` —— 15/17 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 14/17 个有
- `ttN text` —— 11/17 个有
- `SaveImage` —— 7/17 个有
- `CR Text` —— 2/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `RH_MinimaxHailuoH3ImageToVideo` —— 1/17 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/17 个有
- `RH_TopazLabs_VideoUpscale` —— 1/17 个有
- `RunningHub FlashTalk Loader` —— 1/17 个有
- `RunningHub FlashTalk Sampler` —— 1/17 个有
- `T8ShowText` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足

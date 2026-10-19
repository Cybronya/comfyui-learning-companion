---
name: text_to_image_lora_sampler_clip_47
type: Text To Image
frequency: 15
level: strong
coverage: 0.873533
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/RH Upscale双版本RH币API版视频极速高清放大，视频超分工具_2105803495495524354.json, 数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json, 数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json, 视频生成/图生视频/H3 MAX旗舰模型图生视频 工作流让静态图片动起来_2098636207260524546.json, 视频生成/图生视频/H3 MAX旗舰模型图生视频｜让静态图片自然动起来_2098699818653802497.json, 视频生成/图生视频/H3 MAX首尾帧工作流｜旗舰模型双图过渡生成_2095597681195446273.json, 视频生成/图生视频/H3 Max智能运镜工作流 AI看图自动运镜处理_2100658647239053314.json, 视频生成/图生视频/H3 Max智能运镜工作流 AI看图自动运镜处理_2100669399102476290.json, 视频生成/图生视频/H3双采口播数字人 照片加文案自动配音视频生成_2098821076301205505.json, 视频生成/图生视频/MiniMax H3 上下文参考视频+图生视频｜融合运镜与角色_2096868508067000322.json, 视频生成/图生视频/MiniMax H3上下文多参考生视频 多图融合创作_2098822713052844033.json, 视频生成/图生视频/上下文参考视频融合运镜｜MiniMax H3角色一致性图生视频_2096676491013742593.json, 视频生成/文生视频/MiniMax H3多模态视频生成 超低成本每秒两毛钱_2098276360841162754.json, 视频生成/文生视频/Seedance2.5多模态满血版 超低价格视频生成_2098267753768636418.json, 视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（数字人/数字人/RH Upscale双版本RH币API版视频极速高清放大，视频超分工具_2105803495495524354.json、数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json、数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json、视频生成/图生视频/H3 MAX旗舰模型图生视频 工作流让静态图片动起来_2098636207260524546.json、视频生成/图生视频/H3 MAX旗舰模型图生视频｜让静态图片自然动起来_2098699818653802497.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
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
- `孤海注释` —— 14/15 个有
- `LoadImage` —— 12/15 个有
- `PrimitiveStringMultiline` —— 10/15 个有
- `SaveImage` —— 7/15 个有
- `LoadVideo` —— 5/15 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 5/15 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 5/15 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 5/15 个有
- `LoadAudio` —— 4/15 个有
- `CR Prompt Text` —— 3/15 个有
- `PreviewAny` —— 3/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `RH_BytedanceDoubaoSeedAudio10` —— 2/15 个有
- `RH_BytedanceSeedance25GlobalTokenMultimodalVideo` —— 2/15 个有
- `RH_KlingV2AiAvatarStandardImageAudioToVideo` —— 2/15 个有
- `RH_RhartVideoVideoUpscaler` —— 1/15 个有
- `RH_Upscale` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足

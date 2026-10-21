---
name: text_to_image_lora_sampler_clip_146
type: Text To Image
frequency: 8
level: strong
coverage: 0.876375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/RH Upscale双版本RH币API版视频极速高清放大，视频超分工具_2105803495495524354.json, 数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json, 数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json, 视频生成/图生视频/H3双采口播数字人 照片加文案自动配音视频生成_2098821076301205505.json, 视频生成/图生视频/MiniMax H3 上下文参考视频+图生视频｜融合运镜与角色_2096868508067000322.json, 视频生成/图生视频/MiniMax H3上下文多参考生视频 多图融合创作_2098822713052844033.json, 视频生成/图生视频/上下文参考视频融合运镜｜MiniMax H3角色一致性图生视频_2096676491013742593.json, 视频生成/图生视频/博主直播带货照片开口卖货 数字人口播视频生成_2099915240774389761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_146

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/RH Upscale双版本RH币API版视频极速高清放大，视频超分工具_2105803495495524354.json、数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json、数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json、视频生成/图生视频/H3双采口播数字人 照片加文案自动配音视频生成_2098821076301205505.json、视频生成/图生视频/MiniMax H3 上下文参考视频+图生视频｜融合运镜与角色_2096868508067000322.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadImage` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 4/8 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 3/8 个有
- `LoadAudio` —— 2/8 个有
- `LoadVideo` —— 2/8 个有
- `RH_BytedanceDoubaoSeedAudio10` —— 2/8 个有
- `RH_KlingV2AiAvatarStandardImageAudioToVideo` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `RH_RhartVideoVideoUpscaler` —— 1/8 个有
- `RH_Upscale` —— 1/8 个有
- `RunningHub FlashTalk Loader` —— 1/8 个有
- `RunningHub FlashTalk Sampler` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

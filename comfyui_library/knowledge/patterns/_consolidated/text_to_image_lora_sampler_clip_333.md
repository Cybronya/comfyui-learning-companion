---
name: text_to_image_lora_sampler_clip_333
type: Text To Image
frequency: 5
level: strong
coverage: 0.8848
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/视频图像反推工作流｜反推提示词风格迁移 视频风格转换利器_2105563617381937153.json, 图片生成/图生图/AI视频变现途径汇总｜推理应用持续更新指南_2092001114597187585.json, 图片生成/图生图/Wan 2.7视频编辑换背景工作流｜一键替换场景背景｜视频处理必备_2099168088137752578.json, 图片生成/图生图/火山引擎视频去字幕流｜一键擦除画面字幕文字_2098751317052313601.json, 数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_333

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/视频图像反推工作流｜反推提示词风格迁移 视频风格转换利器_2105563617381937153.json、图片生成/图生图/AI视频变现途径汇总｜推理应用持续更新指南_2092001114597187585.json、图片生成/图生图/Wan 2.7视频编辑换背景工作流｜一键替换场景背景｜视频处理必备_2099168088137752578.json、图片生成/图生图/火山引擎视频去字幕流｜一键擦除画面字幕文字_2098751317052313601.json、数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoadImage` —— 3/5 个有
- `LoadVideo` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `easy saveText` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `Qwen3VLProcessor` —— 1/5 个有
- `RH_AlibabaWan27VideoEdit` —— 1/5 个有
- `RH_BytedanceDoubaoSeedAudio10` —— 1/5 个有
- `RH_KlingV2AiAvatarStandardImageAudioToVideo` —— 1/5 个有
- `RH_VolcSubtitleEraseProVideo` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

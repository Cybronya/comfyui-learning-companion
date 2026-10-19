---
name: text_to_image_lora_sampler_clip_85
type: Text To Image
frequency: 10
level: strong
coverage: 0.8908
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AI丝滑慢动作RIFE慢放工作流｜图生视频电影级慢镜头效果_2106222587775901698.json, 视频生成/图生视频/AI视频换脸ReActor逐帧工作流，整脸替换表情口型自然同步图生视频_2106445751026020354.json, 视频生成/图生视频/AI视频换脸ReActor逐帧工作流｜图生视频换脸自然无破绽_2106219463707287554.json, 视频生成/图生视频/FlashVSR视频超分工作流｜图生视频高清放大画质拉满_2106223984546242561.json, 视频生成/图生视频/RIFE丝滑慢动作｜视频慢放不丢帧不掉质感_2097229853106987009.json, 视频生成/图生视频/RIFE视频补帧到60帧工作流｜图生视频丝滑流畅老片焕新_2106228689913606145.json, 视频生成/图生视频/RIFE视频补帧到60帧｜卡顿画面秒变丝滑_2097228457901117441.json, 视频生成/图生视频/视频补帧到60帧工作流｜RIFE插帧画面流畅增强处理_2097165055967191041.json, 视频生成/文生视频/OCR+ProPainter+FlashVSR｜视频去水印加超分_2098772306171621378.json, 视频生成/文生视频/OCR定位结合ProPainter光流修复_视频去水印后FlashVSR超分翻倍_2098208580662026241.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/AI丝滑慢动作RIFE慢放工作流｜图生视频电影级慢镜头效果_2106222587775901698.json、视频生成/图生视频/AI视频换脸ReActor逐帧工作流，整脸替换表情口型自然同步图生视频_2106445751026020354.json、视频生成/图生视频/AI视频换脸ReActor逐帧工作流｜图生视频换脸自然无破绽_2106219463707287554.json、视频生成/图生视频/FlashVSR视频超分工作流｜图生视频高清放大画质拉满_2106223984546242561.json、视频生成/图生视频/RIFE丝滑慢动作｜视频慢放不丢帧不掉质感_2097229853106987009.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FL_RIFE` —— 5/10 个有
- `GetVideoComponents` —— 5/10 个有
- `PrimitiveFloat` —— 5/10 个有
- `Video Slice` —— 5/10 个有
- `FlashVSRNode` —— 3/10 个有
- `LoadImage` —— 2/10 个有
- `ReActorFaceSwap` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `SubtitleDetectorRapidOCR` —— 2/10 个有
- `SubtitleEraserProPainter` —— 2/10 个有

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

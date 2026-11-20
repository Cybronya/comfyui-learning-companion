---
name: text_to_image_lora_sampler_clip_525
type: Text To Image
frequency: 3
level: strong
coverage: 0.778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageLoader, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MultiTextConcatenate, RH_LLMAPI_Pro_Node, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything, solarL_SaveImagesToZip, ttN concat, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能图片G2.5一键生成专业影视分镜与关键帧全流程提示词多图版_2100644030144147458.json, 图片生成/图生图/全能图片G2.5一键生成影视分镜关键帧｜全流程提示词多图版，图生图反推不费脑_2100460642460323841.json, 图片生成/图生图/影视分镜关键帧提示词｜GP-T2.0多图版反推图生图_2092574881362833409.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_525

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全能图片G2.5一键生成专业影视分镜与关键帧全流程提示词多图版_2100644030144147458.json、图片生成/图生图/全能图片G2.5一键生成影视分镜关键帧｜全流程提示词多图版，图生图反推不费脑_2100460642460323841.json、图片生成/图生图/影视分镜关键帧提示词｜GP-T2.0多图版反推图生图_2092574881362833409.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageLoader`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MultiTextConcatenate`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `ttN concat`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG25SunburstImageToImage` —— 2/3 个有
- `easy saveText` —— 2/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_RhartImageG2ImageToImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

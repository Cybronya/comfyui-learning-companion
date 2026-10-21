---
name: text_to_image_lora_sampler_clip_319
type: Text To Image
frequency: 3
level: strong
coverage: 0.903333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/人物提取一键分离｜数字人角色抠图素材提取工作流_2093834995659005953.json, 数字人/数字人/全能图片G Image 2.5｜单图编辑模特产品展示_2101131757046296577.json, 视频生成/文生视频/全能图片PRO低价渠道版｜十图批量编辑图生图省币必囤_2103677088447426561.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_319

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/人物提取一键分离｜数字人角色抠图素材提取工作流_2093834995659005953.json、数字人/数字人/全能图片G Image 2.5｜单图编辑模特产品展示_2101131757046296577.json、视频生成/文生视频/全能图片PRO低价渠道版｜十图批量编辑图生图省币必囤_2103677088447426561.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 1/3 个有
- `ChinesePrompt_Mix` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `RH_RhartImageG25FlareImageToImage` —— 1/3 个有
- `RMBG` —— 1/3 个有

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

---
name: text_to_image_lora_sampler_clip_216
type: Text To Image
frequency: 3
level: strong
coverage: 0.885333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/视频图像反推工作流｜反推提示词风格迁移 视频风格转换利器_2105563617381937153.json, 图片生成/图生图/2102161720235089921.json, 图片生成/文生图/全自动电商出图工作流，文生图电商产品图像处理工具_2107249551341080578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_216

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/视频图像反推工作流｜反推提示词风格迁移 视频风格转换利器_2105563617381937153.json、图片生成/图生图/2102161720235089921.json、图片生成/文生图/全自动电商出图工作流，文生图电商产品图像处理工具_2107249551341080578.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/3 个有
- `Text` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `Qwen3VLProcessor` —— 1/3 个有
- `RH_RhartImageG2ImageToImage` —— 1/3 个有
- `RH_SeedreamV5ProImageToImage` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy promptLine` —— 1/3 个有
- `easy saveText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

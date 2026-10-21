---
name: text_to_image_lora_sampler_clip_253
type: Text To Image
frequency: 4
level: strong
coverage: 0.89075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/视频图像反推工作流｜反推提示词风格迁移 视频风格转换利器_2105563617381937153.json, 图片生成/图生图/2102161720235089921.json, 图片生成/文生图/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json, 图片生成/文生图/字体设计全能图片G工作流，支持参考图的文生图图生图工具_2105741976216883202.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_253

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/视频图像反推工作流｜反推提示词风格迁移 视频风格转换利器_2105563617381937153.json、图片生成/图生图/2102161720235089921.json、图片生成/文生图/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json、图片生成/文生图/字体设计全能图片G工作流，支持参考图的文生图图生图工具_2105741976216883202.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `SaveImage` —— 3/4 个有
- `RH_RhartImageG25FlareImageToImage` —— 2/4 个有
- `Text` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `MultiTextConcatenate` —— 1/4 个有
- `Qwen3VLProcessor` —— 1/4 个有
- `RH_RhartImageG2ImageToImage` —— 1/4 个有
- `RH_SeedreamV5ProImageToImage` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy saveText` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

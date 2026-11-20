---
name: text_to_image_lora_sampler_clip_427
type: Text To Image
frequency: 5
level: strong
coverage: 0.8892
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadVideo, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/视频超分放大，快速无损，2K-4K无损放大_2117190154598305793.json, 数字人/数字人/Topaz Iris版视频极速高清放大处理工具_2100310421151510530.json, 数字人/数字人/TopazLabs视频放大超清处理工作流_2101016263261777921.json, 数字人/数字人/Topaz极速高清放大Iris版 人像视频超分处理_2099947042050232322.json, 视频生成/图生视频/Topaz极速高清放大Iris版_人像视频超分处理_2101220952645390337.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_427

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/视频超分放大，快速无损，2K-4K无损放大_2117190154598305793.json、数字人/数字人/Topaz Iris版视频极速高清放大处理工具_2100310421151510530.json、数字人/数字人/TopazLabs视频放大超清处理工作流_2101016263261777921.json、数字人/数字人/Topaz极速高清放大Iris版 人像视频超分处理_2099947042050232322.json、视频生成/图生视频/Topaz极速高清放大Iris版_人像视频超分处理_2101220952645390337.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 4/5 个有
- `ImageFromBatch` —— 4/5 个有
- `Int` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `PreviewAny` —— 3/5 个有
- `RH_Astra` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `Astra` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `GH_ImageVideoComparer` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_TopazLabs_VideoUpscale` —— 1/5 个有
- `获取视频信息` —— 1/5 个有

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

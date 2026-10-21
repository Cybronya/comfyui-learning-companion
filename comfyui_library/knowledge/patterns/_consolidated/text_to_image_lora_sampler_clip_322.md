---
name: text_to_image_lora_sampler_clip_322
type: Text To Image
frequency: 3
level: strong
coverage: 0.881667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/360度旋转视频｜Wan2.1图生视频+Lora 3D卡通_2091231823711002625.json, 视频生成/文生视频/低价批量视频生成｜文生图生视频生视频模型直出_2093139939205668866.json, 视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_322

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/360度旋转视频｜Wan2.1图生视频+Lora 3D卡通_2091231823711002625.json、视频生成/文生视频/低价批量视频生成｜文生图生视频生视频模型直出_2093139939205668866.json、视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LoadImage` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `WanVideoTeaCacheKJ` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `RelayGrokImagineVideo` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有

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

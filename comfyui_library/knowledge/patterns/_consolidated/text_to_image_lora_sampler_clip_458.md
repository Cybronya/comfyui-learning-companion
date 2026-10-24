---
name: text_to_image_lora_sampler_clip_458
type: Text To Image
frequency: 4
level: strong
coverage: 0.894
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/360度旋转视频｜Wan2.1图生视频+Lora 3D卡通_2091231823711002625.json, 视频生成/图生视频/Wan3.0图生视频｜数字人动作迁移一键生成_2092054082633687041.json, 视频生成/图生视频/Wan3.0首尾帧生视频｜图生视频一键生成直出_2092032397171838978.json, 视频生成/图生视频/happyhorse1.0图生视频｜一张图就能生成动态片_2106626750871597057.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_458

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/360度旋转视频｜Wan2.1图生视频+Lora 3D卡通_2091231823711002625.json、视频生成/图生视频/Wan3.0图生视频｜数字人动作迁移一键生成_2092054082633687041.json、视频生成/图生视频/Wan3.0首尾帧生视频｜图生视频一键生成直出_2092032397171838978.json、视频生成/图生视频/happyhorse1.0图生视频｜一张图就能生成动态片_2106626750871597057.json）

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
- `SaveVideo` —— 3/4 个有
- `RH_AlibabaWan30ImageToVideo` —— 2/4 个有
- `CLIPVisionEncode` —— 1/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `RH_AlibabaHappyhorse10ImageToVideo` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有
- `WanVideoTeaCacheKJ` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

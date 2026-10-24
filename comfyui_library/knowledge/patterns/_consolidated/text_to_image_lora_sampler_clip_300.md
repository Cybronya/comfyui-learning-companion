---
name: text_to_image_lora_sampler_clip_300
type: Text To Image
frequency: 6
level: strong
coverage: 0.905
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2画质增强图生图 Turbo8步快速处理工作流_2099923071095365633.json, 图片生成/图生图/画质增强图生图｜Krea2 Turbo八步极速，写实细节翻倍_2099922159283032065.json, 图片生成/文生图/Seedance2.0 mini图生视频，其它图片处理图生图_2111879230282887170.json, 图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json, 图片生成/文生图/Seedance2.0 mini图生视频｜素材一键变动态大片_2111818999221800962.json, 图片生成/文生图/mini图生视频一键生成｜Seedance2.0图片转视频_2095874894868336642.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_300

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2画质增强图生图 Turbo8步快速处理工作流_2099923071095365633.json、图片生成/图生图/画质增强图生图｜Krea2 Turbo八步极速，写实细节翻倍_2099922159283032065.json、图片生成/文生图/Seedance2.0 mini图生视频，其它图片处理图生图_2111879230282887170.json、图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json、图片生成/文生图/Seedance2.0 mini图生视频｜素材一键变动态大片_2111818999221800962.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
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
- `LoadImage` —— 5/6 个有
- `RH_RhartVideoSparkvideo20MiniImageToVideo` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `SaveImage` —— 3/6 个有
- `EnhancedLoadDiffusionModel` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `TextEncodeKrea2` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `easy float` —— 2/6 个有
- `easy seed` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_76
type: Text To Image
frequency: 15
level: strong
coverage: 0.885533
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json, 图片生成/文生图/Image2.5全能图像文生图 高品质文本到图像生成_2098269388993548289.json, 图片生成/文生图/Seedance2.0 mini图生视频，其它图片处理图生图_2111879230282887170.json, 图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json, 图片生成/文生图/Seedance2.0 mini图生视频｜素材一键变动态大片_2111818999221800962.json, 图片生成/文生图/mini图生视频一键生成｜Seedance2.0图片转视频_2095874894868336642.json, 视频生成/图生视频/H3 Max Turbo图生视频首尾帧生成全节点注释_2100286294709596162.json, 视频生成/图生视频/MiniMax H3 Max Turbo极速版图生视频首尾帧处理工具_2102123247629332481.json, 视频生成/图生视频/MiniMax H3 Max Turbo极速版图生视频首尾帧，高速低成本流畅过渡方案_2103565859515101186.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频生成_2093247372666167298.json, 视频生成/文生视频/H3 Max Turbo图生视频首尾帧生成 全节点注释_2099926302546550786.json, 视频生成/文生视频/Seedance 2.5图生视频处理生成工具_2102525837089263617.json, 视频生成/文生视频/Seedance2.5图生视频工作流，高质量图像到视频生成方案_2103542632843669506.json, 视频生成/文生视频/Seedance2.5图生视频工作流｜高质量图像驱动视频生成_2097761537908887554.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json、图片生成/文生图/Image2.5全能图像文生图 高品质文本到图像生成_2098269388993548289.json、图片生成/文生图/Seedance2.0 mini图生视频，其它图片处理图生图_2111879230282887170.json、图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json、图片生成/文生图/Seedance2.0 mini图生视频｜素材一键变动态大片_2111818999221800962.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
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
- `LoadImage` —— 14/15 个有
- `SaveVideo` —— 13/15 个有
- `SaveImage` —— 10/15 个有
- `CR Text` —— 9/15 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 5/15 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 4/15 个有
- `RH_RhartVideoSparkvideo20MiniImageToVideo` —— 4/15 个有
- `RH_RhartImageG25FlareTextToImage` —— 1/15 个有
- `RH_Screenwriter` —— 1/15 个有
- `WujiAPI` —— 1/15 个有
- `WujiClosedSourceGenerator` —— 1/15 个有
- `WujiUpscaler2` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足

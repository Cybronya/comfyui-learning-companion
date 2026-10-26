---
name: text_to_image_lora_sampler_clip_298
type: Text To Image
frequency: 7
level: strong
coverage: 0.899429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/refMod图生图8视角生成，单图产出环绕多视图_2112320029848068098.json, 图片生成/图生图/千问图生图基础工作流｜简单高效图片处理｜新手也能一键出图_2104749587016806402.json, 图片生成/图生图/参考图一键调色图生图，色调风格秒级对齐大师级色彩_2112625189052837889.json, 图片生成/图生图/参考图一键调色工作流｜色调氛围轻松对齐超省心_2112490868165931010.json, 图片生成/文生图/Qwen 2.1基础工作流i2v t2v，文生视频图生视频双模式入门方案_2103210530956726273.json, 图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json, 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_298

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/refMod图生图8视角生成，单图产出环绕多视图_2112320029848068098.json、图片生成/图生图/千问图生图基础工作流｜简单高效图片处理｜新手也能一键出图_2104749587016806402.json、图片生成/图生图/参考图一键调色图生图，色调风格秒级对齐大师级色彩_2112625189052837889.json、图片生成/图生图/参考图一键调色工作流｜色调氛围轻松对齐超省心_2112490868165931010.json、图片生成/文生图/Qwen 2.1基础工作流i2v t2v，文生视频图生视频双模式入门方案_2103210530956726273.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/7 个有
- `ResolutionSelector` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageScale` —— 2/7 个有
- `SaveImageAdvanced` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `LayerUtility: ImageReel` —— 1/7 个有
- `LayerUtility: ImageReelComposit` —— 1/7 个有
- `easy promptLine` —— 1/7 个有
- `easy setNode` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_173
type: Text To Image
frequency: 5
level: strong
coverage: 0.9166
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json, 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json, 图片生成/文生图/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json, 图片生成/文生图/qwen image2.1文生图利器｜数字人海报制作一步搞定_2104529003418836993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_173

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json、图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json、图片生成/文生图/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json、图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json、图片生成/文生图/qwen image2.1文生图利器｜数字人海报制作一步搞定_2104529003418836993.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `BasicGuider` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `QwenImage21FunPDDLoader` —— 2/5 个有
- `RandomNoise` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `SamplerCustomAdvanced` —— 2/5 个有
- `RH_RhartImageG25FlareImageToImage` —— 1/5 个有
- `SaveImageAdvanced` —— 1/5 个有

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

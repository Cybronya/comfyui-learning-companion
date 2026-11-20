---
name: text_to_image_lora_sampler_clip_261
type: Text To Image
frequency: 8
level: strong
coverage: 0.88925
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Moss image基础加速文生图 字体热门IP图像生成工具_2112999720082821121.json, 图片生成/文生图/Moss文生图2K分辨率直出｜文字渲染清晰细节拉满_2113891798274891777.json, 图片生成/文生图/Moss文生图2K直出 高分辨率图像快速生成工具_2114141520369639425.json, 图片生成/文生图/Z-Image Turbo特定风格人像大作文生图处理工具_2101751504242831361.json, 图片生成/文生图/flux3_image_klein文生图，创意形象高效直出_2111545656975384578.json, 图片生成/文生图/flux3_image_klein文生图｜学AI曹同学同款直出流_2111340043469156354.json, 图片生成/文生图/flux3_klein文生图方案，高质量创意出图轻松搞定_2111539683925774338.json, 图片生成/文生图/flux3_klein文生图极简版｜简洁流出一手好图_2111317480894455809.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_261

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Moss image基础加速文生图 字体热门IP图像生成工具_2112999720082821121.json、图片生成/文生图/Moss文生图2K分辨率直出｜文字渲染清晰细节拉满_2113891798274891777.json、图片生成/文生图/Moss文生图2K直出 高分辨率图像快速生成工具_2114141520369639425.json、图片生成/文生图/Z-Image Turbo特定风格人像大作文生图处理工具_2101751504242831361.json、图片生成/文生图/flux3_image_klein文生图，创意形象高效直出_2111545656975384578.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 7/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `SkipLayerGuidanceDiTSimple` —— 3/8 个有
- `TextGenerate` —— 2/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `FloatConstant` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足

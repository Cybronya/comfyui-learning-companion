---
name: image_to_image_lora_sampler_clip_11
type: Image To Image
frequency: 13
level: strong
coverage: 0.932538
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人物线稿提取_2031290016340647937.json, 图片生成/图生图/星蝶风格一键转换_1991833267762688001.json, 图片生成/图生图/老照片修复flux_kontext全自动修复_2095321572251881474.json, 图片生成/图生图/老照片修复flux_kontext全自动修复_2095425023170400258.json, 图片生成/图生图/老照片修复（flux kontext全自动修复）_1990974918315679745.json, 图片生成/图生图/老照片修复（flux kontext全自动修复））_2017623484586790914.json, 图片生成/图生图/课件20：kontext老照片一键修复_2099656538049826818.json, 图片生成/图生图/陶瓷浮雕_2032083602745331713.json, 平台全量/人物饰品高清精修_2040518742760759298.json, 平台全量/星蝶风格一键转换_1964687575959130114.json, 平台全量/老照片修复全自动修复_2047634990728486913.json, 平台全量/老照片修复（flux kontext全自动修复）_1958052623196835841.json, 平台全量/老照片修复（flux kontext全自动修复）_2020688399820136450.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/人物线稿提取_2031290016340647937.json、图片生成/图生图/星蝶风格一键转换_1991833267762688001.json、图片生成/图生图/老照片修复flux_kontext全自动修复_2095321572251881474.json、图片生成/图生图/老照片修复flux_kontext全自动修复_2095425023170400258.json、图片生成/图生图/老照片修复（flux kontext全自动修复）_1990974918315679745.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RepeatLatentBatch` —— 12/13 个有
- `Image Comparer (rgthree)` —— 11/13 个有
- `UNETLoader` —— 10/13 个有
- `RH_Translator` —— 4/13 个有
- `EnhancedLoadDiffusionModel` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `Text` —— 3/13 个有
- `DifferentialDiffusion` —— 2/13 个有
- `easy imageScaleDownToSize` —— 2/13 个有
- `ColorCorrectOfUtils` —— 1/13 个有
- `easy indexAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 13 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，13 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）

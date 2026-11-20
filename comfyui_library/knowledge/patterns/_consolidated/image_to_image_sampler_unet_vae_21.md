---
name: image_to_image_sampler_unet_vae_21
type: Image To Image
frequency: 10
level: strong
coverage: 0.915
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2511换头换脸_完美一致真实光影_2027294538380877825.json, 图片生成/图生图/千问图片编辑工作流_1986050948818751490.json, 图片生成/图生图/单图编辑_2067956866138857473.json, 图片生成/图生图/单图编辑_qwen2511_2084533535242809346.json, 图片生成/图生图/双图编辑_2067958028665704449.json, 图片生成/图生图/图像编辑模型测试-Qwen Image Edit 2511_2110543678782664706.json, 图片生成/图生图/图像转HDR ｜可调整曝光、恢复更多细节｜Qwen Image Edit 2511_2048131777956417538.json, 图片生成/图生图/换头换脸 一致性真实光影_2010913688546451458.json, 图片生成/图生图/漫剧必备-一键生成人物四视图_2077374977283813377.json, 平台全量/2511换头换脸-完美一致性真实光影--laoxuaistudio_2009897697569935361.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_21

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-2511换头换脸_完美一致真实光影_2027294538380877825.json、图片生成/图生图/千问图片编辑工作流_1986050948818751490.json、图片生成/图生图/单图编辑_2067956866138857473.json、图片生成/图生图/单图编辑_qwen2511_2084533535242809346.json、图片生成/图生图/双图编辑_2067958028665704449.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 9/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 9/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `ModelSamplingAuraFlow` —— 6/10 个有
- `ConditioningZeroOut` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `LayerMask: PersonMaskUltra V2` —— 3/10 个有
- `RHHiddenNodes` —— 3/10 个有
- `SetLatentNoiseMask` —— 3/10 个有
- `PreviewImage` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `GearColorGrade` —— 1/10 个有
- `GearLogC3DecodeSaveEXR` —— 1/10 个有
- `SUPIR_Upscale` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 60% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足

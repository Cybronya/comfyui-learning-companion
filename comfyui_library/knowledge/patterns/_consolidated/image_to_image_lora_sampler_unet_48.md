---
name: image_to_image_lora_sampler_unet_48
type: Image To Image
frequency: 13
level: moderate
coverage: 0.844
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物手办简单玩法_1971909657885339650.json, 图片生成/图生图/产品去标贴_1971522569771892738.json, 图片生成/图生图/修图师必备一键去瑕疵_2018971979549777922.json, 图片生成/图生图/修图师早点下班_2001217985199173634.json, 图片生成/图生图/修图师精修专用_2000844949270786050.json, 图片生成/图生图/千问超级版（去水印抹除物体、添加模特，一致性人物，更改服装，）_1959594362835513345.json, 图片生成/图生图/物品人物生成手办动漫摆放电脑前万物手办简单玩法_2068932630082576385.json, 图片生成/图生图/老金驿站】Qwen单图溶图4步极速工作流_1958797125020774402.json, 图片生成/图生图/融图原版（产品标贴会变）_2034564115947069442.json, 平台全量/fusion v2_1967419094213517314.json, 平台全量/产品与场景的融合_2026918184837713922.json, 平台全量/产品祛除标贴、瑕疵_2036981380885782529.json, 平台全量/修图师早点下班_1963490839417933826.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_48

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/万物手办简单玩法_1971909657885339650.json、图片生成/图生图/产品去标贴_1971522569771892738.json、图片生成/图生图/修图师必备一键去瑕疵_2018971979549777922.json、图片生成/图生图/修图师早点下班_2001217985199173634.json、图片生成/图生图/修图师精修专用_2000844949270786050.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 12/13 个有
- `Image Comparer (rgthree)` —— 12/13 个有
- `easy cleanGpuUsed` —— 10/13 个有
- `FluxKontextImageScale` —— 9/13 个有
- `SeedVR2` —— 9/13 个有
- `SeedVR2BlockSwap` —— 9/13 个有
- `Fast Groups Bypasser (rgthree)` —— 3/13 个有
- `RH_Translator` —— 3/13 个有
- `ImageResizeKJv2` —— 2/13 个有
- `ImageScaleToTotalPixels` —— 2/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 25 | 13 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 13 | 35% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 25，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，13 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）

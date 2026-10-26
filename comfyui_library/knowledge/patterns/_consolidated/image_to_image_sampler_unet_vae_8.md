---
name: image_to_image_sampler_unet_vae_8
type: Image To Image
frequency: 15
level: moderate
coverage: 0.846133
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN图像编辑lora加速版_1958348241307910145.json, "图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982061261863174146.json", "图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982359589297496065.json", 图片生成/图生图/Qwen Edit 4步 加速 图像编辑_1967372813134913537.json, 图片生成/图生图/Qwen Edit 8步加速 图像编辑_1967376109622976514.json, 图片生成/图生图/Qwen Edit MeiTu 图像美学及指令遵从增加图像编辑V1_1982105490522030081.json, 图片生成/图生图/Qwen Edit MeiTu 图像美学及指令遵从增加图像编辑V1_1984427493174165506.json, 图片生成/图生图/Qwen Edit 图像编辑_1966322447366696961.json, 图片生成/图生图/Qwen Edit-R1 Diffusion负感知微调图像编辑V1_1982107681945198593.json, 图片生成/图生图/Qwen Edit8步加速版（自用）（换装前置）_1965400072588546049.json, 图片生成/图生图/Qwen Edit万 8步加速版2（换装前置）_1965423005448945665.json, 图片生成/图生图/Qwen Edit二阶段+换装8步加速（自用）_1965408134586056705.json, 图片生成/图生图/Qwen Edit图像编辑4步新版LighningV2超级加速版_1965777502977306626.json, 图片生成/图生图/Qwen Edit多种分辨率修正方式主体编辑稳定性测试_1960007479117688833.json, 图片生成/图生图/（自用）Qwen Edit8步加速版3（换装前置）_1965423190451343362.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/QWEN图像编辑lora加速版_1958348241307910145.json、图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982061261863174146.json、图片生成/图生图/Qwen Edit 3模型对比（Meitu,原版,R1）_1982359589297496065.json、图片生成/图生图/Qwen Edit 4步 加速 图像编辑_1967372813134913537.json、图片生成/图生图/Qwen Edit 8步加速 图像编辑_1967376109622976514.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `CR Prompt Text` —— 11/15 个有
- `PreviewImage` —— 11/15 个有
- `ImageConcanate` —— 10/15 个有
- `TT_img_enc` —— 5/15 个有
- `AddLabel` —— 4/15 个有
- `JjkText` —— 3/15 个有
- `ImageResize+` —— 1/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `Note Plus (mtb)` —— 1/15 个有
- `TextInput_` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 15 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 15 | 58% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（17/15 个样本）：Steps较低可能导致细节不足

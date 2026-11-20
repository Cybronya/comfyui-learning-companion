---
name: unknown_workflow_sampler_unet_vae_184
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.797714
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FIBO 2 图片编辑，改字扩图合成_2116516810089648129.json, 图片生成/图生图/FIBO_2_图片编辑，改字扩图合成，样例提示词_2116356901280768002.json, 图片生成/图生图/FIBO_2_图片编辑，改字扩图合成，样例提示词_2116368695432929282.json, 图片生成/图生图/Fibo2-edit-图像编辑_2114732505034215425.json, 图片生成/图生图/【LG】QWEN2511极简极低偏移换装_2004542473714237441.json, 平台全量/FIBO 2 图片编辑，改字扩图合成，样例提示词_2115729390519799810.json, 平台全量/图片扩图后自由裁剪出不同尺寸（竖屏转横屏）_2117815120456937473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_184

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FIBO 2 图片编辑，改字扩图合成_2116516810089648129.json、图片生成/图生图/FIBO_2_图片编辑，改字扩图合成，样例提示词_2116356901280768002.json、图片生成/图生图/FIBO_2_图片编辑，改字扩图合成，样例提示词_2116368695432929282.json、图片生成/图生图/Fibo2-edit-图像编辑_2114732505034215425.json、图片生成/图生图/【LG】QWEN2511极简极低偏移换装_2004542473714237441.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `TextEncodeFibo2` —— 6/7 个有
- `PixaromaOutpaint` —— 5/7 个有
- `JjkText` —— 2/7 个有
- `AFL:QwenEditPlusFastuseV2` —— 1/7 个有
- `ImageCrop+` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `MyFixedSizeImageCrop` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 7 | 43% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，7 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足

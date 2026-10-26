---
name: unknown_workflow_sampler_unet_vae_202
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8166
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FIBO2_Image_Edit 图像编辑 ComfyUI 工作流_2114558633513152513.json, 图片生成/图生图/Qwen-image2.1-材质迁移_2102376704630149121.json, 图片生成/图生图/Qwen-image2.1-透明图层抠图_2102747243479658497.json, 图片生成/图生图/Qwen2.1_动漫转写实_2105154791876947970.json, 图片生成/图生图/Qwen_Image_2_1_Outpainting 图像外绘编辑+自然曝光Lora工作流_2104584979157180417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_202

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FIBO2_Image_Edit 图像编辑 ComfyUI 工作流_2114558633513152513.json、图片生成/图生图/Qwen-image2.1-材质迁移_2102376704630149121.json、图片生成/图生图/Qwen-image2.1-透明图层抠图_2102747243479658497.json、图片生成/图生图/Qwen2.1_动漫转写实_2105154791876947970.json、图片生成/图生图/Qwen_Image_2_1_Outpainting 图像外绘编辑+自然曝光Lora工作流_2104584979157180417.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `TextEncodeQwenImage21` —— 4/5 个有
- `Label (rgthree)` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `ImagePadKJ` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `QwenImage21Cache` —— 1/5 个有
- `TextEncodeFibo2` —— 1/5 个有
- `Textbox` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 40 | 5 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 40，5 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

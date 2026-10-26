---
name: image_to_image_upscale_sampler_clip_21
type: Image To Image
frequency: 6
level: strong
coverage: 0.785333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageResizeKJ, ImageScaleBy, KSampler, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Florence2反推提示词+Z-image洗图，SeedVR2高清放大工作流_2012003634023768065.json, 图片生成/图生图/QWEN3.5反推Z-image洗图高相似度_2079104428015185922.json, 图片生成/图生图/QWEN3反推提示+Z-image图生图_1994028675670753281.json, 图片生成/图生图/Z-iamge图生图+提示词反推+图像高清放大_2015635523389362178.json, 图片生成/文生图/Z-Image-反推洗图-网感美女生成_1994955449533390850.json, 图片生成/文生图/Z-iamge图生图++文生图+提示词反推+图像高清放大_2035728548727627777.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Florence2反推提示词+Z-image洗图，SeedVR2高清放大工作流_2012003634023768065.json、图片生成/图生图/QWEN3.5反推Z-image洗图高相似度_2079104428015185922.json、图片生成/图生图/QWEN3反推提示+Z-image图生图_1994028675670753281.json、图片生成/图生图/Z-iamge图生图+提示词反推+图像高清放大_2015635523389362178.json、图片生成/文生图/Z-Image-反推洗图-网感美女生成_1994955449533390850.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageResizeKJ`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `easy anythingIndexSwitch` —— 4/6 个有
- `Qwen3_VQA` —— 3/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `Int` —— 2/6 个有
- `Qwen3VL_Advanced` —— 2/6 个有
- `Florence2ModelLoader` —— 1/6 个有
- `Florence2Run` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）

---
name: text_to_image_controlnet_sampler_clip_4
type: Text To Image
frequency: 8
level: moderate
coverage: 0.8955
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/ControlNet — pose 姿态控制+线稿生成_1914469798615678977.json, 图片生成/图生图/ControlNet— pose 姿态控制_1914286715534569473.json, 图片生成/图生图/SD1.5- 多ControlNet官方工作流_1930242296812355585.json, 图片生成/图生图/SD1.5-Controlnet-OpenPose官方工作流_1930213476415782914.json, 图片生成/图生图/SD1.5-OpenPose（V2.0）官方工作流_1930214688452198401.json, 图片生成/图生图/一键线稿上色-小白适用 V1.5_1915059782980698114.json, 图片生成/图生图/一键线稿上色-小白适用 V2.0_1915412670747709442.json, 图片生成/文生图/清甜水果风_1973294635470729217.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/ControlNet — pose 姿态控制+线稿生成_1914469798615678977.json、图片生成/图生图/ControlNet— pose 姿态控制_1914286715534569473.json、图片生成/图生图/SD1.5- 多ControlNet官方工作流_1930242296812355585.json、图片生成/图生图/SD1.5-Controlnet-OpenPose官方工作流_1930213476415782914.json、图片生成/图生图/SD1.5-OpenPose（V2.0）官方工作流_1930214688452198401.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/8 个有
- `ConditioningCombine` —— 4/8 个有
- `OpenposePreprocessor` —— 4/8 个有
- `ImageInvert` —— 3/8 个有
- `LineArtPreprocessor` —— 3/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `LineartStandardPreprocessor` —— 2/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `LoraLoader` —— 1/8 个有
- `ReActorFaceSwap` —— 1/8 个有
- `easy positive` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 8 | 100% |
| 采样步数 | 30 | 30 - 30 | 8 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 2 - 6 | 8 | 51% |
| 采样算法 | dpmpp_2m | - | 8 | 50% |
| 调度器 | karras | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 512 | 512 - 928 | 8 | 76% |
| 高度 | 768 | 768 - 1232 | 8 | 80% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 0.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 2 - 6，8 个样本
- 采样算法 最常用 dpmpp_2m，8 个样本，一致性 50%
- 调度器 最常用 karras，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 928，8 个样本
- 高度 中位数 768，观测区间 768 - 1232，8 个样本，取值集中（一致性 80%）

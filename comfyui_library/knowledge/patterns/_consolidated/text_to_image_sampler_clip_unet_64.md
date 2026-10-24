---
name: text_to_image_sampler_clip_unet_64
type: Text To Image
frequency: 10
level: strong
coverage: 0.9307
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/线稿上色_z-image-trubo_2095092335230144513.json, 图片生成/图生图/线稿上色_z-image-trubo_2097175505438076930.json, 图片生成/图生图/线稿上色_z-image-trubo_2097514082390863873.json, 图片生成/文生图/3D人物编辑器应用系列之一——Z image Turbo的openpose_2019553633838309377.json, 图片生成/文生图/Z Image_精准动作设计_ControlNet应用_1996391560990310401.json, 图片生成/文生图/Z Image_精准动作设计之二_双人搏斗_ControlNet应用_1998728780791304193.json, 图片生成/文生图/Z image的Controlnet的Canny_1996385835375280130.json, 图片生成/文生图/Z image的Controlnet的Depth_1996388981573042178.json, 图片生成/文生图/Z image的Controlnet的openpose_1995081250421583873.json, 图片生成/文生图/Z-image-trubo_深度控制_2090688273374081025.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/线稿上色_z-image-trubo_2095092335230144513.json、图片生成/图生图/线稿上色_z-image-trubo_2097175505438076930.json、图片生成/图生图/线稿上色_z-image-trubo_2097514082390863873.json、图片生成/文生图/3D人物编辑器应用系列之一——Z image Turbo的openpose_2019553633838309377.json、图片生成/文生图/Z Image_精准动作设计_ControlNet应用_1996391560990310401.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `QwenImageDiffsynthControlnet` —— 6/10 个有
- `PreviewImage` —— 4/10 个有
- `ZImageFunControlnet` —— 4/10 个有
- `CR SDXL Aspect Ratio` —— 3/10 个有
- `ImageConcanate` —— 3/10 个有
- `LineartStandardPreprocessor` —— 3/10 个有
- `DWPreprocessor` —— 1/10 个有
- `OpenposePreprocessor` —— 1/10 个有
- `Zoe-DepthMapPreprocessor` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 10 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1024 | 768 - 1824 | 10 | 70% |
| 高度 | 1024 | 720 - 1280 | 10 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，10 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1824，10 个样本
- 高度 中位数 1024，观测区间 720 - 1280，10 个样本，取值集中（一致性 88%）

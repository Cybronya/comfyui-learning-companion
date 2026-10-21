---
name: text_to_image_sampler_clip_unet_40
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9933
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1文生图基础流_2025773663856893953.json, 图片生成/文生图/2-1-z-image-文生图-角色生成_2061349711671554049.json, 图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json, 图片生成/文生图/3D人物编辑器应用系列之一——Z image Turbo的openpose_2019553633838309377.json, 图片生成/文生图/Z Image_精准动作设计_ControlNet应用_1996391560990310401.json, 图片生成/文生图/Z Image_精准动作设计之二_双人搏斗_ControlNet应用_1998728780791304193.json, 图片生成/文生图/Z image的Controlnet的Canny_1996385835375280130.json, 图片生成/文生图/Z image的Controlnet的Depth_1996388981573042178.json, 图片生成/文生图/Z image的Controlnet的openpose_1995081250421583873.json, 图片生成/文生图/动作编辑器应用系列之二——Z Image Turbo_2022827863912751105.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1文生图基础流_2025773663856893953.json、图片生成/文生图/2-1-z-image-文生图-角色生成_2061349711671554049.json、图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json、图片生成/文生图/3D人物编辑器应用系列之一——Z image Turbo的openpose_2019553633838309377.json、图片生成/文生图/Z Image_精准动作设计_ControlNet应用_1996391560990310401.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/10 个有
- `ModelSamplingAuraFlow` —— 8/10 个有
- `ModelPatchLoader` —— 7/10 个有
- `QwenImageDiffsynthControlnet` —— 7/10 个有
- `CR SDXL Aspect Ratio` —— 3/10 个有
- `DWPreprocessor` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `OpenposePreprocessor` —— 1/10 个有
- `RH_Nano_Banana2_Image2Image` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 1024 - 1920 | 10 | 74% |
| 高度 | 1024 | 720 - 1920 | 10 | 70% |
| 采样步数 | 10 | 9 - 20 | 10 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 10 | 50% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 1024 - 1920，10 个样本
- 高度 中位数 1024，观测区间 720 - 1920，10 个样本
- 采样步数 中位数 10，观测区间 9 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）

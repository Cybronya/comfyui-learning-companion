---
name: image_to_image_sampler_unet_vae_5
type: Image To Image
frequency: 17
level: weak
coverage: 0.900882
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QIANWEN图像编辑_2088896217135800321.json, 图片生成/图生图/QWEN-最新编辑模型_2003645392963158018.json, 图片生成/图生图/QWEN2511+重打光(Relight)_2018262241644126210.json, 图片生成/图生图/QWEN2511+重打光l(Relight)ora强化版_2014561496826646530.json, 图片生成/图生图/QWEN角度随心换升级版本_2010187591118757890.json, 图片生成/图生图/QWEN角度随心换升级版本_2027345865211387906.json, 图片生成/图生图/Qwen 2511 edit 多视角镜头拍摄 智能多角度生成 qwen image edit_2010692605092306946.json, 图片生成/图生图/Qwen 2511 多角度 + Z-Image-Turbo_2010904385815056386.json, 图片生成/图生图/Qwen 2511 镜头控制插件_2009786830929010690.json, "图片生成/图生图/Qwen Edit 2511+镜头多角度控制,一张图片变换多个角度_2052204567022063617.json", "图片生成/图生图/Qwen Edit 2511+镜头多角度控制,一张图片变换多个角度_2052916903613607937.json", 图片生成/图生图/Qwen Edit 2511： Multiangle Camera 镜头选择（直观简单好用）_2009796133521989633.json, 图片生成/图生图/Qwen Image Edit 2511+镜头选择 不同视角+镜头选择（柯基大佬版）_2012169391844102146.json, 图片生成/图生图/Qwen Image Edit 2511+镜头选择 不同视角_2011062220834213890.json, 图片生成/图生图/Qwen multiple angle2511+多镜头选择_2009799321264328706.json, 图片生成/图生图/Qwen-Edit2511人物多角度生成_2009909041430011905.json, 图片生成/文生图/Z-Image-Turbo 多角度学习_2039927595122298882.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/QIANWEN图像编辑_2088896217135800321.json、图片生成/图生图/QWEN-最新编辑模型_2003645392963158018.json、图片生成/图生图/QWEN2511+重打光(Relight)_2018262241644126210.json、图片生成/图生图/QWEN2511+重打光l(Relight)ora强化版_2014561496826646530.json、图片生成/图生图/QWEN角度随心换升级版本_2010187591118757890.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 16/17 个有
- `LoraLoaderModelOnly` —— 16/17 个有
- `EmptySD3LatentImage` —— 13/17 个有
- `QwenMultiangleCameraNode` —— 13/17 个有
- `easy showAnything` —— 13/17 个有
- `ImageScaleToTotalPixels` —— 12/17 个有
- `easy promptList` —— 11/17 个有
- `PreviewImage` —— 3/17 个有
- `CLIPTextEncode` —— 2/17 个有
- `ConditioningZeroOut` —— 2/17 个有
- `LayerUtility: PurgeVRAM` —— 2/17 个有
- `PreviewAny` —— 2/17 个有
- `QwenMultiangleLightningNode` —— 2/17 个有
- `EmptyLatentImage` —— 1/17 个有
- `FluxKontextImageScale` —— 1/17 个有
- `ShowText` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 17 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 17 | 58% |
| 采样算法 | euler | - | 17 | 88% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 0.4 - 1 | 17 | 79% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，17 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，17 个样本
- 采样算法 最常用 euler，17 个样本，一致性 88%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，17 个样本
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足

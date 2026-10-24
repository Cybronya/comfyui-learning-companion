---
name: image_to_image_sampler_unet_vae_24
type: Image To Image
frequency: 9
level: strong
coverage: 0.895111
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptList, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-Edit-2511 图像多角度控制生成 V1.0_2010632419312934913.json, 图片生成/图生图/Qwen2511 image edit+镜头视角无极选择器_2010617810262695938.json, 图片生成/图生图/Qwen2511 多角度镜头自由切换_2079613700566241281.json, 图片生成/图生图/Qwen2511 多角度镜头自由切换（谢柯基大佬）_2009817207995375618.json, 图片生成/图生图/Qwen2511图片编辑自由视角_2011815143591649281.json, 图片生成/图生图/Qwen2511自由摄像机角度分镜生成器（动作自由编辑）_2009784618572058626.json, 图片生成/图生图/Qwen2511镜头控制无限多角度_2030880865328304129.json, 图片生成/图生图/qwenimg-edit2511智能多角度生成_2009829830128308225.json, 图片生成/图生图/人物一致性-快速三视图_2022028386276745218.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_24

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-image-Edit-2511 图像多角度控制生成 V1.0_2010632419312934913.json、图片生成/图生图/Qwen2511 image edit+镜头视角无极选择器_2010617810262695938.json、图片生成/图生图/Qwen2511 多角度镜头自由切换_2079613700566241281.json、图片生成/图生图/Qwen2511 多角度镜头自由切换（谢柯基大佬）_2009817207995375618.json、图片生成/图生图/Qwen2511图片编辑自由视角_2011815143591649281.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptList`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `QwenMultiangleCameraNode` —— 7/9 个有
- `SaveImage` —— 7/9 个有
- `EmptySD3LatentImage` —— 6/9 个有
- `PreviewImage` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `VNCCS_VisualPositionControl` —— 2/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LayerUtility: TextJoin` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `Power Lora Loader (rgthree)` —— 1/9 个有
- `SaveImageGrid` —— 1/9 个有
- `SaveImagePlus` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy promptConcat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

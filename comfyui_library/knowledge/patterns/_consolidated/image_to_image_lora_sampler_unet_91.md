---
name: image_to_image_lora_sampler_unet_91
type: Image To Image
frequency: 7
level: moderate
coverage: 0.984429
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511 多视角效果转换工作流_2038916153908666369.json, 图片生成/图生图/Qwen-Edit-2511-图片无限多视角转换_2011064723831263234.json, 图片生成/图生图/Qwen-Edit-2511-多图编辑_2003681947601805313.json, 图片生成/图生图/Qwen-Edit-2511-换脸工作流_2004526917825032193.json, 图片生成/图生图/Qwen-Edit-2511可视化视角编辑 直观改变万物视角_2010541642947764225.json, 图片生成/图生图/Qwen-Edit-2511姿态迁移_2012123669828472833.json, 图片生成/图生图/【🛫书墨】姿态构图迁移v3-anypose_2010972516814168065.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_91

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511 多视角效果转换工作流_2038916153908666369.json、图片生成/图生图/Qwen-Edit-2511-图片无限多视角转换_2011064723831263234.json、图片生成/图生图/Qwen-Edit-2511-多图编辑_2003681947601805313.json、图片生成/图生图/Qwen-Edit-2511-换脸工作流_2004526917825032193.json、图片生成/图生图/Qwen-Edit-2511可视化视角编辑 直观改变万物视角_2010541642947764225.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `QwenMultiangleCameraNode` —— 3/7 个有
- `ColorCorrect` —— 2/7 个有
- `ImageBlend` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `SDPoseOODLoader` —— 2/7 个有
- `SDPoseOODProcessor` —— 2/7 个有
- `easy promptList` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `KOOK_SaveJPGImage` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 7 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 7 | 69% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

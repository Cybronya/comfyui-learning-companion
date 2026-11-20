---
name: image_to_image_sampler_clip_unet_30
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8048
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, INTConstant, ImageScaleDownToSize, ImageScaleToTotalPixels, ImageSharpen, KSampler, KSamplerSelect, LayerFilter: Sharp & Soft, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/05 wenshengtusanheyi_2048562124812722178.json, 图片生成/反推提示词/5bzszngobzp_2059682891268976642.json, 图片生成/反推提示词/7ofqmazscup_2059683461824339970.json, 图片生成/反推提示词/批量洗图 多角度展示 Z_Image_Turbo+FLUX.2-klein-9b图像反推生图+高清放_2038791651585429505.json, 图片生成/图生图/Z image base 3合1 高清放大+文生图+图生图  满血版 反推出图 极致真实，抖音小红书_2039575881663909890.json, 图片生成/图生图/zimage+klein图像反推生图+高清放大_2037440968860897282.json, 图片生成/文生图/3合1=高清放大+文生图生图=Z image base！B站艾橘溪_2036421892235595778.json, 图片生成/文生图/Z image base三合一：文生图+图生图+高清放大_2036692926176169986.json, 图片生成/文生图/文生图+图生图+高清放大=Z image base三合一！_2036695524622995457.json, 图片生成/文生图/高清放大+文生图+图生图 Z image base 3合1   满血版 反推出图 极致真实，抖音小红_2039588818780688386.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/05 wenshengtusanheyi_2048562124812722178.json、图片生成/反推提示词/5bzszngobzp_2059682891268976642.json、图片生成/反推提示词/7ofqmazscup_2059683461824339970.json、图片生成/反推提示词/批量洗图 多角度展示 Z_Image_Turbo+FLUX.2-klein-9b图像反推生图+高清放_2038791651585429505.json、图片生成/图生图/Z image base 3合1 高清放大+文生图+图生图  满血版 反推出图 极致真实，抖音小红书_2039575881663909890.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `INTConstant`
- `ImageScaleDownToSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler`
- `KSamplerSelect`
- `LayerFilter: Sharp & Soft`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `JjkText` —— 8/10 个有
- `LayerUtility: BooleanOperator` —— 8/10 个有
- `LayerUtility: If ` —— 8/10 个有
- `PreviewAny` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `llama_cpp_instruct_adv` —— 8/10 个有
- `llama_cpp_model_loader` —— 8/10 个有
- `RTXVideoSuperResolution` —— 3/10 个有
- `EmptyFlux2LatentImage` —— 2/10 个有
- `Flux2Scheduler` —— 2/10 个有
- `GetImageSize+` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `ShellAgentPluginOutputText` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `TextGenerateLTX2Prompt` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 44 | 10 - 50 | 10 | 63% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 10 | 69% |
| 采样算法 | res_multistep | - | 10 | 80% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 44，观测区间 10 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，10 个样本
- 采样算法 最常用 res_multistep，10 个样本，一致性 80%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）

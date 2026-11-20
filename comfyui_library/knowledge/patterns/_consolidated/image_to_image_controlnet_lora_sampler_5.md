---
name: image_to_image_controlnet_lora_sampler_5
type: Image To Image
frequency: 3
level: strong
coverage: 0.853667
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, ImageScaleToTotalPixels, JJC_JoyCaption, KSampler, LineartStandardPreprocessor, LoadImage, LoraLoaderModelOnly, ModelSamplingFluxNormalized, PreviewImage, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/joy_beta_one反推_pd_1933521957457674241.json, 图片生成/图生图/joy_beta_one反推_pd_2114317629140848641.json, 图片生成/文生图/joy_beta_one反推+线稿生图_1914709174859825153.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/joy_beta_one反推_pd_1933521957457674241.json、图片生成/图生图/joy_beta_one反推_pd_2114317629140848641.json、图片生成/文生图/joy_beta_one反推+线稿生图_1914709174859825153.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `JJC_JoyCaption`
- `KSampler`
- `LineartStandardPreprocessor`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFluxNormalized`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）

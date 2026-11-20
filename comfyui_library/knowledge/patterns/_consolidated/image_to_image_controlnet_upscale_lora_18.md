---
name: image_to_image_controlnet_upscale_lora_18
type: Image To Image
frequency: 2
level: weak
coverage: 0.841
common_nodes: [AIO_Preprocessor, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, DF_Image_scale_to_side, DiffControlNetLoader, GetNode, ImageGenResolutionFromImage, ImageOnlyCheckpointLoader, ImageResize+, ImageScale, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoader, LoraLoaderModelOnly, PreviewImage, Range(Num Steps) - Float, SaveImage, SetNode, StableZero123_Conditioning, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/三视图_1782238317866168322.json, 平台全量/多视图_1783763007076048898.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/三视图_1782238317866168322.json、平台全量/多视图_1783763007076048898.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `DF_Image_scale_to_side`
- `DiffControlNetLoader`
- `GetNode`
- `ImageGenResolutionFromImage`
- `ImageOnlyCheckpointLoader`
- `ImageResize+`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Range(Num Steps) - Float`
- `SaveImage`
- `SetNode`
- `StableZero123_Conditioning`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy globalSeed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | exponential | - | 2 | 100% |
| 重绘幅度 | 0.5 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 exponential，2 个样本，一致性 100%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

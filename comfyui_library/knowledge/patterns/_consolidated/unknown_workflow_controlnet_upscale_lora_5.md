---
name: unknown_workflow_controlnet_upscale_lora_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.961
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize, INTConstant, ImageConcanate, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerAdvanced, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, Seed (rgthree), UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image+Controlnet视频首帧动态控制生图_2000971709572317185.json, 图片生成/文生图/Z-image+control_2001795995862220802.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image+Controlnet视频首帧动态控制生图_2000971709572317185.json、图片生成/文生图/Z-image+control_2001795995862220802.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `INTConstant`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

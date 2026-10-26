---
name: unknown_workflow_controlnet_lora_sampler_16
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7915
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/z-image_base+turbo图生图_增加细节+定制成图_2039632903042240514.json, 图片生成/图生图/人物一致性洗图Z-Image_turbo+base 双重采样增加细节_2022890695295508481.json, 图片生成/图生图/图生图，定制人物，z-image_base+turbo增加细节成图_2019422246560866305.json, 图片生成/图生图/图生图，定制人物，z-image_base+turbo增加细节成图_2021398418060484610.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/z-image_base+turbo图生图_增加细节+定制成图_2039632903042240514.json、图片生成/图生图/人物一致性洗图Z-Image_turbo+base 双重采样增加细节_2022890695295508481.json、图片生成/图生图/图生图，定制人物，z-image_base+turbo增加细节成图_2019422246560866305.json、图片生成/图生图/图生图，定制人物，z-image_base+turbo增加细节成图_2021398418060484610.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Qwen3VL_Chat` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Qwen3VL_Advanced` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 4 | 100% |
| 采样算法 | 4 | 3 - 4 | 4 | 88% |
| 调度器 | er_sde | - | 4 | 100% |
| 重绘幅度 | sgm_uniform | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，观测区间 3 - 4，4 个样本，取值集中（一致性 88%）
- 调度器 最常用 er_sde，4 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

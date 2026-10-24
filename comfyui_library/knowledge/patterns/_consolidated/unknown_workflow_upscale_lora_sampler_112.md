---
name: unknown_workflow_upscale_lora_sampler_112
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.64
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image-turb可出真实感多图_2076105517755363330.json, 图片生成/文生图/熟颜世绘-日系轻熟御姐人像_2072120581000097793.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image-turb可出真实感多图_2076105517755363330.json、图片生成/文生图/熟颜世绘-日系轻熟御姐人像_2072120581000097793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LazySwitch1way` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `ModelPassThrough` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy int` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 19 | - | 2 | 42% |
| 采样算法 | 2 | - | 2 | 50% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 1040 | - | 2 | 96% |
| 高度 | 1912 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 19，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 1040，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 高度 中位数 1912，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

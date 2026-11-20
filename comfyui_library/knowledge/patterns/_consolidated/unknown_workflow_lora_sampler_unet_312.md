---
name: unknown_workflow_lora_sampler_unet_312
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.666
common_nodes: [CFGGuider, CLIPLoader, EmptyLatentImage, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json, 视频生成/图生视频/Qwen Image 2.1｜Turbo 8步 VS 原版25步·11组画质横评与极速生成_2109547716111060993.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_312

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json、视频生成/图生视频/Qwen Image 2.1｜Turbo 8步 VS 原版25步·11组画质横评与极速生成_2109547716111060993.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `QwenImage21Cache` —— 1/2 个有
- `SeedNode` —— 1/2 个有
- `TextGenerate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1112 | - | 2 | 92% |
| 高度 | 1312 | - | 2 | 78% |
| 采样步数 | fixed | - | 1 | 100% |
| Prompt 约束强度(CFG) | 25 | - | 1 | 100% |
| 采样算法 | 3.5 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1112，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1312，样本不足，未给区间，2 个样本
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

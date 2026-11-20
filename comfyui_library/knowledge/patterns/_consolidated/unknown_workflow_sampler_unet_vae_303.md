---
name: unknown_workflow_sampler_unet_vae_303
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.83675
common_nodes: [CFGGuider, CLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/qwen-image2.1一键抠图_2117504818246934529.json, 平台全量/qwen-image2.1局部重绘（遮罩）_2117851080687177730.json, 平台全量/qwen-image2.1扩图-2k高清出图_2117590562235838465.json, 视频生成/图生视频/Qwen Image 2.1｜Turbo 8步 VS 原版25步·11组画质横评与极速生成_2109547716111060993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_303

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/qwen-image2.1一键抠图_2117504818246934529.json、平台全量/qwen-image2.1局部重绘（遮罩）_2117851080687177730.json、平台全量/qwen-image2.1扩图-2k高清出图_2117590562235838465.json、视频生成/图生视频/Qwen Image 2.1｜Turbo 8步 VS 原版25步·11组画质横评与极速生成_2109547716111060993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `GetImageSize` —— 1/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SeedNode` —— 1/4 个有
- `TextInput_` —— 1/4 个有

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

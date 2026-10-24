---
name: unknown_workflow_lora_sampler_unet_199
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.908333
common_nodes: [Canny, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F.1通过线稿，生成室内效果图+放大_1908319381733187585.json, 图片生成/图生图/F.1通过线稿，生成室内效果图_1908530217424400386.json, 图片生成/图生图/FLUX+CN丨canny+Depth丨深度 线稿 lora_1898940711260082177.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/F.1通过线稿，生成室内效果图+放大_1908319381733187585.json、图片生成/图生图/F.1通过线稿，生成室内效果图_1908530217424400386.json、图片生成/图生图/FLUX+CN丨canny+Depth丨深度 线稿 lora_1898940711260082177.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `Canny`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 2/3 个有
- `ImageResize` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `BaiduTranslateNode` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 28 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 28，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

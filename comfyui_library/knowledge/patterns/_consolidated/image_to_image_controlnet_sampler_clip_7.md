---
name: image_to_image_controlnet_sampler_clip_7
type: Image To Image
frequency: 4
level: strong
coverage: 0.869
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX1_CN_Union_Pro同时实现线条_姿势_深度控制_1907309489064665090.json, 图片生成/图生图/Kontext+Controlnet姿态改变工作流_1961098437326475265.json, 图片生成/图生图/人物姿势改变_2001166342361411586.json, 图片生成/图生图/商用模特姿态改变工作流_1967747323386368001.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX1_CN_Union_Pro同时实现线条_姿势_深度控制_1907309489064665090.json、图片生成/图生图/Kontext+Controlnet姿态改变工作流_1961098437326475265.json、图片生成/图生图/人物姿势改变_2001166342361411586.json、图片生成/图生图/商用模特姿态改变工作流_1967747323386368001.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetLoader` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `FluxKontextImageScale` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `Seed Everywhere` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1.5 | 0.7 - 1.5 | 4 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.5，观测区间 0.7 - 1.5，4 个样本

---
name: text_to_image_controlnet_lora_sampler_21
type: Text To Image
frequency: 3
level: strong
coverage: 0.822667
common_nodes: [CLIPTextEncode, ConcatStringSingle, ControlNetApplySD3, ControlNetLoader, DualCLIPLoaderGGUF, EmptyLatentImage, FluxGuidance, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RH_Prompter, SaveImage, SetUnionControlNetType, ShowText|pysssss, TilePreprocessor, UnetLoaderGGUF, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/Flux 生成角色多视图_1916004576124665858.json, 平台全量/Flux 多帧电影角色一致性生成_1839006356753031170.json, 平台全量/Flux 生成游戏角色一致性多视图_1839123673948078082.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux 生成角色多视图_1916004576124665858.json、平台全量/Flux 多帧电影角色一致性生成_1839006356753031170.json、平台全量/Flux 生成游戏角色一致性多视图_1839123673948078082.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConcatStringSingle`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoaderGGUF`
- `EmptyLatentImage`
- `FluxGuidance`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Prompter`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TilePreprocessor`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `FaceDetailer` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `UltralyticsDetectorProvider` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy imageSplitGrid` —— 1/3 个有
- `easy imagesSplitImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1472 | 1472 - 1472 | 3 | 100% |
| 高度 | 1472 | 1472 - 1472 | 3 | 100% |
| ControlNet 权重 | 0.53 | 0.53 - 0.53 | 3 | 100% |
| 采样步数 | 20 | 15 - 20 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 0.59 - 1 | 3 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1472，观测区间 1472 - 1472，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1472，观测区间 1472 - 1472，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.53，观测区间 0.53 - 0.53，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 15 - 20，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.59 - 1，3 个样本

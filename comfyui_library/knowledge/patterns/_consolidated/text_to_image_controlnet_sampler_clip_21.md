---
name: text_to_image_controlnet_sampler_clip_21
type: Text To Image
frequency: 3
level: strong
coverage: 0.895667
common_nodes: [Anything Everywhere3, CLIPTextEncode, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GoogleTranslateTextNode, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy boolean, easy cleanGpuUsed, easy int, easy positive, easy seed]
problems: []
missing: []
members: [图片生成/文生图/Kontext-双人脸融合-打造新IP新角角_1943716400794046466.json, 图片生成/文生图/图生人脸一致性角色_1941829971805683714.json, 数字人/数字人/双人脸融合 人脸设计  人物面部设计 数字人生成 防撞脸 角色ip设计_2018571332446851073.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Kontext-双人脸融合-打造新IP新角角_1943716400794046466.json、图片生成/文生图/图生人脸一致性角色_1941829971805683714.json、数字人/数字人/双人脸融合 人脸设计  人物面部设计 数字人生成 防撞脸 角色ip设计_2018571332446851073.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GoogleTranslateTextNode`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy int`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `FaceCombine` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `ImageSmartSharpen+` —— 1/3 个有
- `InfiniteYouApply` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1440 | 512 - 1440 | 3 | 61% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1440，观测区间 512 - 1440，3 个样本

---
name: image_to_image_lora_sampler_unet_29
type: Image To Image
frequency: 14
level: moderate
coverage: 0.874571
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511-AnyPose用参考图实现姿势控制_2065718964432494594.json, 图片生成/图生图/Qwen-Edit-2509-白底图转模特展示_1989690060327014401.json, 图片生成/图生图/Qwen-Image-2511-AnyPose用参考图实现姿势控制_2006282960210763777.json, 图片生成/图生图/Qwen_千问一键丰胸工作流_2003473370219986945.json, 图片生成/图生图/yj丰胸_2011686538739982337.json, 图片生成/图生图/一键丰胸神器，即刻变美！_2005605400391151618.json, 图片生成/图生图/一键丰胸神器，完美丰胸！_2033013429618872322.json, 图片生成/图生图/一键改变人物视角_1991135857899864066.json, 图片生成/图生图/一键生成图片视角转变_2049739021416443905.json, 图片生成/图生图/一键生成图片视角转变_2049751286458884098.json, 图片生成/图生图/产品六视图生成-直接宫格_2043952379636228098.json, 图片生成/图生图/产品六视图生成-组合图分析_2044290263606104065.json, 图片生成/图生图/姿势控制 Qwen2511-AnyPose_2065745202484170754.json, 图片生成/图生图/胸部增强模型-丰胸自动流程-qwen2511新模型_2014336544496164865.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/2511-AnyPose用参考图实现姿势控制_2065718964432494594.json、图片生成/图生图/Qwen-Edit-2509-白底图转模特展示_1989690060327014401.json、图片生成/图生图/Qwen-Image-2511-AnyPose用参考图实现姿势控制_2006282960210763777.json、图片生成/图生图/Qwen_千问一键丰胸工作流_2003473370219986945.json、图片生成/图生图/yj丰胸_2011686538739982337.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 12/14 个有
- `ImageScaleToTotalPixels` —— 11/14 个有
- `ImageUpscaleWithModel` —— 9/14 个有
- `UpscaleModelLoader` —— 9/14 个有
- `PreviewImage` —— 8/14 个有
- `easy imageSize` —— 7/14 个有
- `ImageResizeKJv2` —— 2/14 个有
- `ImageTile+` —— 2/14 个有
- `ImageUntile+` —— 2/14 个有
- `PIP_图像联结` —— 2/14 个有
- `RMBG` —— 2/14 个有
- `Anything Everywhere` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 14 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 14 | 57% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，14 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（20/14 个样本）：Steps较低可能导致细节不足

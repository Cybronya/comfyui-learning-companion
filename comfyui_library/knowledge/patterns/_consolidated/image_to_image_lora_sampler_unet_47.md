---
name: image_to_image_lora_sampler_unet_47
type: Image To Image
frequency: 12
level: strong
coverage: 0.961917
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/laoA 单姿态控制_2083568675835174913.json, 图片生成/图生图/mutiangle旋转摄像头生成多角度人物图片_2021198244126138369.json, 图片生成/图生图/产品多视角_2029792715122155522.json, 图片生成/图生图/人物场景多角度分镜图生成（镜头角度可调整）_2054953876385746946.json, 图片生成/图生图/人设一致性多角度_2011272687615741953.json, 图片生成/图生图/亿薪AI多角度摄像控制（96种机位选择）+直观便捷操作_2013894548686114817.json, 图片生成/图生图/千问三图编辑_2015629342180642817.json, 图片生成/图生图/千问图像编辑2511  单图编辑_2003720550470066177.json, 图片生成/图生图/千问图像编辑2511  双图编辑_2003696896738770946.json, 图片生成/图生图/单角度摄像控制（背面专属版）+直观便捷操作_2064296017763332098.json, 图片生成/图生图/多角度2511一致性分镜_2069622645976559618.json, 图片生成/文生图/多角度摄像控制（96种机位选择）+直观便捷操作_2036073760159174657.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/laoA 单姿态控制_2083568675835174913.json、图片生成/图生图/mutiangle旋转摄像头生成多角度人物图片_2021198244126138369.json、图片生成/图生图/产品多视角_2029792715122155522.json、图片生成/图生图/人物场景多角度分镜图生成（镜头角度可调整）_2054953876385746946.json、图片生成/图生图/人设一致性多角度_2011272687615741953.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 10/12 个有
- `KepStringList` —— 8/12 个有
- `QwenMultiangleCameraNode` —— 8/12 个有
- `easy showAnything` —— 8/12 个有
- `EmptySD3LatentImage` —— 6/12 个有
- `Int` —— 6/12 个有
- `Text Concatenate` —— 4/12 个有
- `easy string` —— 4/12 个有
- `TextInput_` —— 3/12 个有
- `ZML_LimitImageAspect` —— 3/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `SeedVR2` —— 1/12 个有
- `SeedVR2BlockSwap` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `easy promptLine` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 12 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 12 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，12 个样本，取值集中（一致性 97%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_lora_sampler_unet_52
type: Image To Image
frequency: 12
level: strong
coverage: 0.915083
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, Text Concatenate, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511多角度可视化控制流-单图版_2010738889564098561.json, 图片生成/图生图/Qwen2511多角度可视化控制流（多图直出版）_2010554072843165697.json, 图片生成/图生图/QwenImage-Edit-2511-多角度编辑APP_2009969851430866946.json, 图片生成/图生图/qwen2511多角度提示词控制_2059192086624296961.json, 图片生成/图生图/多角度控制拍摄_2010308549825536001.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2009893150126514178.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2011827730614067202.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2036733513197690881.json, 图片生成/图生图/多角度摄像控制（96种机位选择）+直观便捷操作_2055634329270792194.json, 图片生成/图生图/多角度镜头控制（人像摄影 漫剧镜头 场景）_2050550918256578562.json, 图片生成/文生图/智能会展空间设计 任意角度 3D交互方案工作流 V2.0_2011120346996412418.json, 平台全量/【功能】Qwen2511多角度镜头_1982746479649538050.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_52

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen2511多角度可视化控制流-单图版_2010738889564098561.json、图片生成/图生图/Qwen2511多角度可视化控制流（多图直出版）_2010554072843165697.json、图片生成/图生图/QwenImage-Edit-2511-多角度编辑APP_2009969851430866946.json、图片生成/图生图/qwen2511多角度提示词控制_2059192086624296961.json、图片生成/图生图/多角度控制拍摄_2010308549825536001.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `KepStringList` —— 8/12 个有
- `easy string` —— 8/12 个有
- `PreviewImage` —— 5/12 个有
- `CR Text` —— 4/12 个有
- `GetNode` —— 3/12 个有
- `JDCN_StringToList` —— 3/12 个有
- `MemoryCleaner` —— 3/12 个有
- `CR Text Concatenate` —— 2/12 个有
- `ConditioningZeroOut` —— 2/12 个有
- `EmptySD3LatentImage` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `RH_Nano_Banana2_Image2Image` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 12 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，12 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足

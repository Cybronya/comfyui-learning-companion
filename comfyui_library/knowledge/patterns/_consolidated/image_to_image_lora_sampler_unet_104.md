---
name: image_to_image_lora_sampler_unet_104
type: Image To Image
frequency: 6
level: strong
coverage: 0.9045
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Multiangle主体多视角转换分镜生成_2010162501878550530.json, 图片生成/图生图/Qwen 2511 Multiangle Camera 角度可视化镜头控制 更新2026.5.17_2010587672741416961.json, 图片生成/图生图/Qwen-Multiangle 多角度分镜工作流_2016062576681029633.json, 图片生成/图生图/Qwen-Multiangle-任意角度镜头切换_2026976393363460098.json, 图片生成/图生图/Qwen2511多角度可视化控制流-单图版_2010738889564098561.json, 图片生成/图生图/Qwen2511多角度可视化控制流（多图直出版）_2010554072843165697.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_104

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Multiangle主体多视角转换分镜生成_2010162501878550530.json、图片生成/图生图/Qwen 2511 Multiangle Camera 角度可视化镜头控制 更新2026.5.17_2010587672741416961.json、图片生成/图生图/Qwen-Multiangle 多角度分镜工作流_2016062576681029633.json、图片生成/图生图/Qwen-Multiangle-任意角度镜头切换_2026976393363460098.json、图片生成/图生图/Qwen2511多角度可视化控制流-单图版_2010738889564098561.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 5/6 个有
- `TextEncodeQwenImageEditPlus` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `KepStringList` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `Text Concatenate` —— 2/6 个有
- `easy imageConcat` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/6 个有
- `basicIn_int` —— 1/6 个有
- `easy string` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

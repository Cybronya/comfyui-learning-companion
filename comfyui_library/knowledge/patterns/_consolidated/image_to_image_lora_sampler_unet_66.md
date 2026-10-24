---
name: image_to_image_lora_sampler_unet_66
type: Image To Image
frequency: 9
level: strong
coverage: 0.93
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Multiangle主体多视角转换分镜生成_2010162501878550530.json, 图片生成/图生图/Qwen 2511 Multiangle Camera 角度可视化镜头控制 更新2026.5.17_2010587672741416961.json, 图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_1953384744518123521.json, 图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_2052365470401089538.json, 图片生成/图生图/Qwen-Multiangle 多角度分镜工作流_2016062576681029633.json, 图片生成/图生图/Qwen-edit-2511-人像多角度随意调整_2008543202546028546.json, 图片生成/图生图/Qwen-image-edit2511多角度一致性-标准版-(必收藏)_2050953090811080705.json, 图片生成/图生图/Qwen2511-AI漫剧分镜视角生成（极速版）_2010535252258725889.json, 图片生成/图生图/Qwen_Flux _ 一键多角度控制 可自动 可手动 精准构图_2057547027516579841.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_66

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Multiangle主体多视角转换分镜生成_2010162501878550530.json、图片生成/图生图/Qwen 2511 Multiangle Camera 角度可视化镜头控制 更新2026.5.17_2010587672741416961.json、图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_1953384744518123521.json、图片生成/图生图/Qwen Multiangle 千问多角度一致性工作流_2052365470401089538.json、图片生成/图生图/Qwen-Multiangle 多角度分镜工作流_2016062576681029633.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
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
- `TextEncodeQwenImageEditPlus` —— 8/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 7/9 个有
- `KepStringList` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `ImageScaleToTotalPixels` —— 3/9 个有
- `easy promptList` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `CLIPTextEncode` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/9 个有
- `basicIn_int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

---
name: image_to_image_lora_sampler_unet_93
type: Image To Image
frequency: 8
level: strong
coverage: 0.916875
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Multiangle主体多视角转换分镜生成_2010162501878550530.json, 图片生成/图生图/Qwen 2511 Multiangle Camera 角度可视化镜头控制 更新2026.5.17_2010587672741416961.json, 图片生成/图生图/Qwen-Multiangle 多角度分镜工作流_2016062576681029633.json, 图片生成/图生图/Qwen-image-edit2511多角度一致性-标准版-(必收藏)_2050953090811080705.json, 图片生成/图生图/Qwen2511多角度可视化控制流_2009977063985385474.json, 图片生成/图生图/mutiangle旋转摄像头生成多角度人物图片_2021198244126138369.json, 图片生成/文生图/Qwen2511多角度可视化控制流可调节_2010509977156329474.json, 平台全量/图像多角度生成，手动调节，不用手写提示词_2018498179112636418.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Multiangle主体多视角转换分镜生成_2010162501878550530.json、图片生成/图生图/Qwen 2511 Multiangle Camera 角度可视化镜头控制 更新2026.5.17_2010587672741416961.json、图片生成/图生图/Qwen-Multiangle 多角度分镜工作流_2016062576681029633.json、图片生成/图生图/Qwen-image-edit2511多角度一致性-标准版-(必收藏)_2050953090811080705.json、图片生成/图生图/Qwen2511多角度可视化控制流_2009977063985385474.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
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
- `KepStringList` —— 7/8 个有
- `TextEncodeQwenImageEditPlus` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `ImpactMakeAnyList` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/8 个有
- `basicIn_int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 8 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，8 个样本，取值集中（一致性 97%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

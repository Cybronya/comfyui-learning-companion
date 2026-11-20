---
name: image_to_image_lora_sampler_unet_82
type: Image To Image
frequency: 9
level: strong
coverage: 0.873444
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图图RefineAnything真实替换与局部精修工作流_2073640112583434242.json, 图片生成/图生图/多角度_qwen2511_2084173106301726722.json, 图片生成/图生图/多角度修图工作流_2043211965497090050.json, 图片生成/图生图/多角度生成_2068685654430666753.json, 图片生成/图生图/建筑效果图角度调整神仙工作流_2010179182180962306.json, 图片生成/图生图/电商生成任意角度镜头_2012073874376105985.json, 图片生成/图生图/视角转换_2012751136897372161.json, 平台全量/精细化编辑｜单图涂抹编辑｜+RefineAny 局部优化 LoRA_2044839878495571970.json, 平台全量/精细化编辑｜单图编辑 + 1 张参考图｜+RefineAny 局部优化 LoRA_2044832593970995201.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_82

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/图图RefineAnything真实替换与局部精修工作流_2073640112583434242.json、图片生成/图生图/多角度_qwen2511_2084173106301726722.json、图片生成/图生图/多角度修图工作流_2043211965497090050.json、图片生成/图生图/多角度生成_2068685654430666753.json、图片生成/图生图/建筑效果图角度调整神仙工作流_2010179182180962306.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 7/9 个有
- `TextEncodeQwenImageEditPlus` —— 6/9 个有
- `QwenMultiangleCameraNode` —— 5/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `MaskToImage` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `RefineAnything_Pasteback` —— 3/9 个有
- `RefineAnything_PreImg` —— 3/9 个有
- `TextEncodeQwenImageEditPlus_NoAppend` —— 3/9 个有
- `easy showAnything` —— 2/9 个有
- `RunningHub Deepcleaner` —— 1/9 个有
- `easy promptLine` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 9 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，9 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_lora_sampler_unet_32
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.830929
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, Textbox, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit Plus人物姿态迁移_1971077216199155713.json, 图片生成/图生图/QwenEdit Plus新版双图编辑人物互动偏移修正版V1_1971376025932382209.json, 图片生成/图生图/QwenEdit Plus新版双图编辑人物互动偏移修正版V2_1970891254328397826.json, 图片生成/图生图/QwenEdit Plus新版双图编辑人物套装更换偏移修正版V1_1971379271564509186.json, 图片生成/图生图/QwenEdit Plus新版双图编辑人物套装更换偏移修正版V2_1970880365474811906.json, 图片生成/图生图/QwenEdit Plus新版双图编辑人物套装更换偏移修正版V3(Lora加强)_1971921027959812098.json, 图片生成/图生图/QwenEdit Plus新版双图编辑人物姿态参考偏移修正版V1_1971373771607195649.json, 图片生成/图生图/QwenEdit Plus新版双图编辑人物姿态参考偏移修正版V2_1970881798769123329.json, 图片生成/图生图/QwenEdit Plus新版双图编辑双人交互偏移修正版V1_1971375270219464705.json, 图片生成/图生图/QwenEdit Plus新版双图编辑双人交互偏移修正版V2_1970888766275624961.json, 图片生成/图生图/优化偏移-人物一致性image Plus三图融合_1970522423198162945.json, 图片生成/图生图/千问QwenEdit 2511一致性双图编辑_2003756229585477634.json, 图片生成/图生图/千问QwenEdit plus一致性双图编辑_1970887152890482689.json, 图片生成/图生图/🦖QwenEdit Plus姿势迁移_1971109381418979329.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_32

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/QwenEdit Plus人物姿态迁移_1971077216199155713.json、图片生成/图生图/QwenEdit Plus新版双图编辑人物互动偏移修正版V1_1971376025932382209.json、图片生成/图生图/QwenEdit Plus新版双图编辑人物互动偏移修正版V2_1970891254328397826.json、图片生成/图生图/QwenEdit Plus新版双图编辑人物套装更换偏移修正版V1_1971379271564509186.json、图片生成/图生图/QwenEdit Plus新版双图编辑人物套装更换偏移修正版V2_1970880365474811906.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 13/14 个有
- `Text Concatenate` —— 11/14 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 11/14 个有
- `easy showAnything` —— 11/14 个有
- `DF_Get_image_size` —— 10/14 个有
- `EmptySD3LatentImage` —— 10/14 个有
- `RH_Captioner` —— 7/14 个有
- `DWPreprocessor` —— 5/14 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 3/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足

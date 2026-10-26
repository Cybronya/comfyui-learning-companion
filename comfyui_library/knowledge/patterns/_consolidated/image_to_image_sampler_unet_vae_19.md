---
name: image_to_image_sampler_unet_vae_19
type: Image To Image
frequency: 8
level: strong
coverage: 0.8675
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2-Klein实现人物不同视角的白底照片【晨晨的AI应用包007】_2013884427834757122.json, 图片生成/图生图/Flux Klein 图生图工作流_2018899055077761025.json, 图片生成/图生图/Flux-Klein 真人转动漫_2033832402732191745.json, 图片生成/图生图/Flux2-klein-9B-人像一致性写真_2012875333439070209.json, 图片生成/图生图/Flux2-klein-9B-电影分镜9宫格图_2015764587139833857.json, 图片生成/图生图/Klein-true-V2-单图编辑+一致性lora_2047831635298619393.json, 图片生成/图生图/Qwen-Edit-2511图生分镜_电影、短片人物一致性_2043969511224778753.json, 图片生成/文生图/Qwen-Edit-2511 一张图生成分镜一致性电影、短片_2003730564337311745.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein实现人物不同视角的白底照片【晨晨的AI应用包007】_2013884427834757122.json、图片生成/图生图/Flux Klein 图生图工作流_2018899055077761025.json、图片生成/图生图/Flux-Klein 真人转动漫_2033832402732191745.json、图片生成/图生图/Flux2-klein-9B-人像一致性写真_2012875333439070209.json、图片生成/图生图/Flux2-klein-9B-电影分镜9宫格图_2015764587139833857.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `CLIPTextEncode` —— 6/8 个有
- `ReferenceLatent` —— 6/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `Text` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `easy promptLine` —— 3/8 个有
- `AILab_QwenVL` —— 2/8 个有
- `CFGNorm` —— 2/8 个有
- `JDCN_StringToList` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `ProcessString` —— 2/8 个有
- `QZ_ResolutionPreset` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 2/8 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 8 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_lora_sampler_vae_16
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.941857
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511 multi angle可视化角度编辑V2_2009735363601895426.json, 图片生成/图生图/Qwen Image Edit 2511-三图编辑_2004027345054932994.json, 图片生成/图生图/Qwen-Image-Edit-2509 下一个镜头_场景_2030202076516585473.json, 图片生成/图生图/Qwen2511-multi angle-精准控制图像镜头_2009798078206844929.json, 图片生成/图生图/Qwenedit-2511 多角度可视化角度编辑_2010887390902095874.json, 图片生成/图生图/可视化分镜角度编辑Qwen 2511 multi angle-V2_2011338342184525826.json, 图片生成/图生图/可视化角度编辑 （多机位）Qwen 2511 multi angle_2010360280441692162.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen 2511 multi angle可视化角度编辑V2_2009735363601895426.json、图片生成/图生图/Qwen Image Edit 2511-三图编辑_2004027345054932994.json、图片生成/图生图/Qwen-Image-Edit-2509 下一个镜头_场景_2030202076516585473.json、图片生成/图生图/Qwen2511-multi angle-精准控制图像镜头_2009798078206844929.json、图片生成/图生图/Qwenedit-2511 多角度可视化角度编辑_2010887390902095874.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 6/7 个有
- `CheckpointLoaderSimple` —— 5/7 个有
- `EmptySD3LatentImage` —— 5/7 个有
- `QwenMultiangleCameraNode` —— 5/7 个有
- `easy promptList` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `CR SDXL Aspect Ratio` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `ShowText` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_lora_sampler_unet_80
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.838
common_nodes: [Anything Everywhere3, CFGNorm, CLIPLoader, CR Prompt Text, EmptySD3LatentImage, ImageConcatMulti, KSampler, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoraLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Face Swap换头换脸_2095324882908307457.json, 图片生成/图生图/Face+Swap换脸换头+换脸 Head Swap 4K版_2101844906145832961.json, 图片生成/图生图/Qwen2511换装换头换脸_多图编辑_高清修复_2068287861228658690.json, "图片生成/图生图/换脸换头 换脸pro Face Swap, Head Swap写实人物一致性 4K版_2100758115913388034.json", "图片生成/图生图/换脸换头 换脸pro Face Swap, Head Swap写实人物一致性 4K版_2101286359330807809.json", 图片生成/图生图/换装换头换脸_多图编辑_高清修复_Best-Face-Swap_2062858305428606977.json, 平台全量/换头换脸 无色差 BFS-Best-Face-Swap Qwen-Image-Edit-2511_2069977881954045954.json, 平台全量/换头换脸-BFS-Best-Face-Swap-Workflow_2041333319018749954.json, 平台全量/换装换头换脸 多图编辑 高清修复   Best-Face-Swap_2056544007479709698.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_80

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Face Swap换头换脸_2095324882908307457.json、图片生成/图生图/Face+Swap换脸换头+换脸 Head Swap 4K版_2101844906145832961.json、图片生成/图生图/Qwen2511换装换头换脸_多图编辑_高清修复_2068287861228658690.json、图片生成/图生图/换脸换头 换脸pro Face Swap, Head Swap写实人物一致性 4K版_2100758115913388034.json、图片生成/图生图/换脸换头 换脸pro Face Swap, Head Swap写实人物一致性 4K版_2101286359330807809.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `ImageConcatMulti`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `AspectRatioSelect` —— 3/9 个有
- `RH_RhartImageG2ImageToImage` —— 3/9 个有
- `easy imageColorMatch` —— 3/9 个有
- `Int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

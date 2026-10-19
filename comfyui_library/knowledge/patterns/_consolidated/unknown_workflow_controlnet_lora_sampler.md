---
name: unknown_workflow_controlnet_lora_sampler
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.868417
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2BlockSwap, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Image Compare (mtb), LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1960723959954247682.json, 图片生成/文生图/1960733292200955906.json, 图片生成/文生图/1960733829457752065.json, 图片生成/文生图/1960762262350966785.json, 图片生成/文生图/1960762268713717762.json, 图片生成/文生图/1960762275642707970.json, 图片生成/文生图/1960886656419205122.json, 图片生成/文生图/1961397908115537922.json, 图片生成/文生图/1963885408525570050.json, 图片生成/文生图/1964919288882712578.json, 图片生成/文生图/1965712466367967233.json, 图片生成/文生图/1977759228209364994.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1960723959954247682.json、图片生成/文生图/1960733292200955906.json、图片生成/文生图/1960733829457752065.json、图片生成/文生图/1960762262350966785.json、图片生成/文生图/1960762268713717762.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 11/12 个有
- `SaveLatent` —— 11/12 个有
- `SeedVR2GGUF` —— 11/12 个有
- `DepthAnything_V2` —— 8/12 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 8/12 个有
- `AIO_Preprocessor` —— 3/12 个有
- `OpenposePreprocessor` —— 3/12 个有
- `Image Compare (mtb)` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `LoraLoader` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | 0.75 - 1 | 12 | 87% |
| 采样步数 | 8 | 4 - 12 | 12 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | res_2s | - | 12 | 100% |
| 调度器 | beta57 | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.75，观测区间 0.75 - 1，12 个样本，取值集中（一致性 87%）
- 采样步数 中位数 8，观测区间 4 - 12，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，12 个样本，一致性 100%
- 调度器 最常用 beta57，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（15/12 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Image Compare (mtb)、LayerUtility: ImageScaleByAspectRatio V2

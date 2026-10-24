---
name: unknown_workflow_controlnet_sampler_clip
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.869182
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, ImageConcanate, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2BlockSwap, SeedVR2GGUF, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image InstantX Controlnet 控制集合_1961108839028428802.json, 图片生成/文生图/Qwen Image InstantX Controlnet姿势控制V1_1960762262350966785.json, 图片生成/文生图/Qwen Image InstantX Controlnet深度控制V1_1960762268713717762.json, 图片生成/文生图/Qwen Image InstantX Controlnet线稿控制V1_1960762275642707970.json, 图片生成/文生图/（写实版）Qwen Image 4步V2新版本文生图_1965712466367967233.json, 图片生成/文生图/（贞贞写实版）Qwen Image文生图_1963885408525570050.json, 图片生成/文生图/（贞贞写实版）Qwen Image文生图（滑冰版）_1964919288882712578.json, 图片生成/文生图/（贞贞版3方式）Qwen Image InstantX Controlnet线稿控制V1_1960723959954247682.json, 图片生成/文生图/（贞贞版）Qwen Image InstantX Controlnet姿势控制V1_1960733829457752065.json, 图片生成/文生图/（贞贞版）Qwen Image InstantX Controlnet深度控制V1_1960733292200955906.json, 图片生成/文生图/（贞贞版）Qwen Image文生图_1961397908115537922.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Qwen Image InstantX Controlnet 控制集合_1961108839028428802.json、图片生成/文生图/Qwen Image InstantX Controlnet姿势控制V1_1960762262350966785.json、图片生成/文生图/Qwen Image InstantX Controlnet深度控制V1_1960762268713717762.json、图片生成/文生图/Qwen Image InstantX Controlnet线稿控制V1_1960762275642707970.json、图片生成/文生图/（写实版）Qwen Image 4步V2新版本文生图_1965712466367967233.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `SaveLatent` —— 10/11 个有
- `DepthAnything_V2` —— 6/11 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 6/11 个有
- `AIO_Preprocessor` —— 3/11 个有
- `OpenposePreprocessor` —— 3/11 个有
- `Image Compare (mtb)` —— 2/11 个有
- `GetImageSize` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/11 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | 0.75 - 1 | 11 | 86% |
| 采样步数 | 8 | 4 - 20 | 11 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | res_2s | - | 11 | 100% |
| 调度器 | beta57 | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.75，观测区间 0.75 - 1，11 个样本，取值集中（一致性 86%）
- 采样步数 中位数 8，观测区间 4 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，11 个样本，一致性 100%
- 调度器 最常用 beta57，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_video_sampler_unet_92
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.843
common_nodes: [AppendStringsToList, CLIPLoader, EmptyImage, Float, GetImageSizeAndCount, ImageConcanate, ImageResizeKJv2, KSampler, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, PreviewImage, RH_LLMAPI_NODE, RH_Translator, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy anythingIndexSwitch, easy int, easy outputToList, easy positive, easy saveText, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/视频-视频双海报自动(中英文)-Qwen-Image-2.1_2103796336226295810.json, 平台全量/视频-视频双海报自动(中英文)_2009252760159522817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_92

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频-视频双海报自动(中英文)-Qwen-Image-2.1_2103796336226295810.json、平台全量/视频-视频双海报自动(中英文)_2009252760159522817.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AppendStringsToList`
- `CLIPLoader`
- `EmptyImage`
- `Float`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy anythingIndexSwitch`
- `easy int`
- `easy outputToList`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `TextEncodeQwenImage21` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `TextGenerateLTX2Prompt` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | - | 2 | 28% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，样本不足，未给区间，2 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

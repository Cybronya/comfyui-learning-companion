---
name: unknown_workflow_video_upscale_lora_24
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.808333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR String To Combo, Fast Groups Muter (rgthree), FluxGuidance, GetRandomIntegerInRange, ImageUpscaleWithModel, ImpactStringSelector, Int, KSampler, LayerUtility: BooleanOperator, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, RH_Captioner, RH_LLMAPI_NODE, SplitStringByDelimiter, Text Find and Replace, TextBox, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ, easy cleanGpuUsed, easy ifElse, easy int, easy showAnything]
problems: []
missing: []
members: [平台全量/运镜 _ WAN2.1-10种拍摄运镜方式_1970672070436790273.json, 视频生成/图生视频/人物情绪 _ WAN2.1_1930863289075740674.json, 视频生成/图生视频/运镜 _ WAN2.1（10种拍摄运镜方式）_1930256998841925634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/运镜 _ WAN2.1-10种拍摄运镜方式_1970672070436790273.json、视频生成/图生视频/人物情绪 _ WAN2.1_1930863289075740674.json、视频生成/图生视频/运镜 _ WAN2.1（10种拍摄运镜方式）_1930256998841925634.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR String To Combo`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GetRandomIntegerInRange`
- `ImageUpscaleWithModel`
- `ImpactStringSelector`
- `Int`
- `KSampler`
- `LayerUtility: BooleanOperator`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `SplitStringByDelimiter`
- `Text Find and Replace`
- `TextBox`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `Model Input Switch` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `PrimitiveString` —— 2/3 个有
- `RH_Prompter` —— 2/3 个有
- `CR Model Input Switch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

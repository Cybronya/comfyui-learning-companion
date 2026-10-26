---
name: unknown_workflow_controlnet_sampler_clip_13
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92725
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image洗图_2002354201495760898.json, 图片生成/图生图/Z-image洗图_2007831795965890562.json, 图片生成/图生图/Z-image洗图_2066396543179116545.json, 图片生成/图生图/Z-lmage Turbo 结构守护者：一键生成未来墅境_2011725976450899970.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-image洗图_2002354201495760898.json、图片生成/图生图/Z-image洗图_2007831795965890562.json、图片生成/图生图/Z-image洗图_2066396543179116545.json、图片生成/图生图/Z-lmage Turbo 结构守护者：一键生成未来墅境_2011725976450899970.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy imageColorMatch` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `GetImageSize+` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/4 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1080 | 4 | 74% |
| 高度 | 1920 | 512 - 1920 | 4 | 61% |
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | res_multistep | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1080，4 个样本
- 高度 中位数 1920，观测区间 512 - 1920，4 个样本
- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%

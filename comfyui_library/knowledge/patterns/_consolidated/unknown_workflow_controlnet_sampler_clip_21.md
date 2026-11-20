---
name: unknown_workflow_controlnet_sampler_clip_21
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.92775
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSizeAndCount, INTConstant, ImageConcanate, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchLoader, PreviewImage, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy anythingIndexSwitch, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/生图-图生图控制姿态2.1-Z_Image_1996867719981146113.json, 图片生成/图生图/生图-图生图控制姿态2.1-Z_Image_2066055918607200256.json, 图片生成/图生图/生图-图生图遮罩区域重绘-Z_Image_2003301510870138881.json, 平台全量/生图-视频帧姿态生参考图2.1-Z_Image_2001856485124653058.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/生图-图生图控制姿态2.1-Z_Image_1996867719981146113.json、图片生成/图生图/生图-图生图控制姿态2.1-Z_Image_2066055918607200256.json、图片生成/图生图/生图-图生图遮罩区域重绘-Z_Image_2003301510870138881.json、平台全量/生图-视频帧姿态生参考图2.1-Z_Image_2001856485124653058.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcanate`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchLoader`
- `PreviewImage`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `RH_Captioner` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `MaskToImage` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 75%

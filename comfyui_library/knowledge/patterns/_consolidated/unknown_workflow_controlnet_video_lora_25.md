---
name: unknown_workflow_controlnet_video_lora_25
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.964
common_nodes: [ADE_AnimateDiffLoaderWithContext, ADE_StandardStaticContextOptions, AIO_Preprocessor, BNK_CLIPTextEncodeAdvanced, CLIPLoader, CLIPSetLastLayer, CheckpointLoaderSimple, CogVideoDecode, CogVideoImageEncode, CogVideoSampler, CogVideoTextEncode, ControlNetApplyAdvanced, ControlNetLoader, ControlNetLoaderAdvanced, DWPreprocessor, DownloadAndLoadCogVideoModel, FreeU_V2, GetImageSizeAndCount, ImageConcanate, ImageConcatMulti, ImageResizeKJ, ImageScale, KSamplerAdvanced //Inspire, LoadWanVideoT5TextEncoder, LoraLoader, PreviewImage, RIFE VFI, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/视频生视频工作流（Wan2.1工作流+CogVideoX-5B工作流）_1986260724970389505.json, 视频生成/文生视频/文生视频  wan2.2真人转动漫_2041329650097463297.json, 视频生成/文生视频/真人转动漫 文生视频_2046502279716544514.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_25

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/视频生视频工作流（Wan2.1工作流+CogVideoX-5B工作流）_1986260724970389505.json、视频生成/文生视频/文生视频  wan2.2真人转动漫_2041329650097463297.json、视频生成/文生视频/真人转动漫 文生视频_2046502279716544514.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `ADE_AnimateDiffLoaderWithContext`
- `ADE_StandardStaticContextOptions`
- `AIO_Preprocessor`
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPLoader`
- `CLIPSetLastLayer`
- `CheckpointLoaderSimple`
- `CogVideoDecode`
- `CogVideoImageEncode`
- `CogVideoSampler`
- `CogVideoTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ControlNetLoaderAdvanced`
- `DWPreprocessor`
- `DownloadAndLoadCogVideoModel`
- `FreeU_V2`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `ImageScale`
- `KSamplerAdvanced //Inspire`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `PreviewImage`
- `RIFE VFI`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 3 | 100% |
| 采样算法 | 7 | 7 - 7 | 3 | 100% |
| 调度器 | dpmpp_2m | - | 3 | 100% |
| 重绘幅度 | karras | - | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 7，观测区间 7 - 7，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m，3 个样本，一致性 100%
- 重绘幅度 最常用 karras，3 个样本，一致性 100%
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

---
name: unknown_workflow_video_lora_sampler_966
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6475
common_nodes: [AIO_Preprocessor, AddLabel, ColorMatch, Compare, DWPreprocessor, EmptyImage, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBlend, ImageConcanate, ImageConcatMulti, ImageResizeKJ, ImpactStringSelector, LoadWanVideoT5TextEncoder, PreviewImage, Primitive integer [Crystools], RH_Captioner, RH_Translator, RandomInt, SaveImage, SetNode, ShowText|pysssss, String Replace (mtb), Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy ifElse, easy showAnything]
problems: []
missing: []
members: [平台全量/23种风VACE万相视频转绘_转绘神器(Kontext）_1941413180801445890.json, 视频生成/图生视频/23种风VACE万相视频转绘_支持随机抽卡和用户自定义风格全能转绘神器(Kontext）_1929256563398316034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_966

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/23种风VACE万相视频转绘_转绘神器(Kontext）_1941413180801445890.json、视频生成/图生视频/23种风VACE万相视频转绘_支持随机抽卡和用户自定义风格全能转绘神器(Kontext）_1929256563398316034.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `ColorMatch`
- `Compare`
- `DWPreprocessor`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBlend`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `ImpactStringSelector`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `RH_Translator`
- `RandomInt`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `String Replace (mtb)`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImagePadKJ` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RH_ComfyFluxKontext` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

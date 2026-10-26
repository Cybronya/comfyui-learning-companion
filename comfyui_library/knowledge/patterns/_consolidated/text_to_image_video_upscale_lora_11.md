---
name: text_to_image_video_upscale_lora_11
type: Text To Image
frequency: 2
level: weak
coverage: 0.882
common_nodes: [Anything Everywhere, Anything Everywhere3, ApplyFBCacheOnModel, Bjornulf_FreeVRAM, CFGZeroStarAndInit, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DownloadAndLoadGIMMVFIModel, DualCLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, GIMMVFI_interpolate, GetImageSizeAndCount, ImageUpscaleWithModel, Int, Joy_caption, Joy_caption_load, KSampler, LayerUtility: TextJoin, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, SaveImage, ShowText|pysssss, TextInputBasic, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy forLoopEnd, easy forLoopStart, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/抖音美女同款图生图，图生视频_1914569260054605826.json, 视频生成/图生视频/抖音自拍图生图，图生视频一体_1914576244527300609.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/抖音美女同款图生图，图生视频_1914569260054605826.json、视频生成/图生视频/抖音自拍图生图，图生视频一体_1914576244527300609.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `ApplyFBCacheOnModel`
- `Bjornulf_FreeVRAM`
- `CFGZeroStarAndInit`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DownloadAndLoadGIMMVFIModel`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `ImageUpscaleWithModel`
- `Int`
- `Joy_caption`
- `Joy_caption_load`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `SaveImage`
- `ShowText|pysssss`
- `TextInputBasic`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1500 | - | 2 | 72% |
| 高度 | 1500 | - | 2 | 72% |
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1500，样本不足，未给区间，2 个样本
- 高度 中位数 1500，样本不足，未给区间，2 个样本
- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

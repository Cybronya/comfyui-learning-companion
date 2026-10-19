---
name: unknown_workflow_video_lora_sampler_749
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9455
common_nodes: [AIO_Preprocessor, CR Text Concatenate, ColorMatch, GetImageSizeAndCount, ImageResizeKJ, JWInteger, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_Translator, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy int, easy textSwitch]
problems: []
missing: []
members: [视频生成/图生视频/1938243040110903297.json, 视频生成/图生视频/1937759191832662018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_749

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1938243040110903297.json、视频生成/图生视频/1937759191832662018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CR Text Concatenate`
- `ColorMatch`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `JWInteger`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_Translator`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy int`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

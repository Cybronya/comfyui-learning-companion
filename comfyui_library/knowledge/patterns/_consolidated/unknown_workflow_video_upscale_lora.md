---
name: unknown_workflow_video_upscale_lora
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.824875
common_nodes: [BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, DownloadAndLoadGIMMVFIModel, DualCLIPLoader, Fast Groups Bypasser (rgthree), GIMMVFI_interpolate, Image Comparer (rgthree), KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoader, LyingSigmaSampler, ModelSamplingFlux, PreviewImage, UNETLoader, UltimateSDUpscaleCustomSample, UpscaleModelLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/1936315199089463298.json, 视频生成/图生视频/1939167024537128962.json, 视频生成/图生视频/1939163413023281153.json, 视频生成/图生视频/1939178766813839361.json, 视频生成/图生视频/1937845770739716097.json, 视频生成/图生视频/1937842796491358209.json, 视频生成/图生视频/1935698602532462594.json, 视频生成/图生视频/1937139193686466561.json, 视频生成/图生视频/1933388878445195265.json, 视频生成/图生视频/1933379047416049666.json, 视频生成/图生视频/1935685313358389249.json, 视频生成/图生视频/1935681642642272257.json, 视频生成/图生视频/1938321001929183234.json, 视频生成/图生视频/1938170176401489921.json, 视频生成/图生视频/1935687902431277057.json, 视频生成/图生视频/1934100002748682241.json, 视频生成/图生视频/1933778192144752641.json, 视频生成/图生视频/1938063161952243713.json, 视频生成/图生视频/1935654735695249409.json, 视频生成/图生视频/1935610511423897602.json, 视频生成/图生视频/1938458312801476609.json, 视频生成/图生视频/1935716513280421889.json, 视频生成/图生视频/1936300828120502273.json, 视频生成/图生视频/1937134593935876098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/1936315199089463298.json、视频生成/图生视频/1939167024537128962.json、视频生成/图生视频/1939163413023281153.json、视频生成/图生视频/1939178766813839361.json、视频生成/图生视频/1937845770739716097.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DownloadAndLoadGIMMVFIModel`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GIMMVFI_interpolate`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `LyingSigmaSampler`
- `ModelSamplingFlux`
- `PreviewImage`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `UpscaleModelLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToMegapixels` —— 21/24 个有
- `ImageSmartSharpen+` —— 21/24 个有
- `GetNode` —— 3/24 个有
- `SetNode` —— 3/24 个有
- `AddLabel` —— 2/24 个有
- `BasicGuider` —— 2/24 个有
- `CLIPTextEncode` —— 2/24 个有
- `CR Image Grid Panel` —— 2/24 个有
- `EmptyLatentImage` —— 2/24 个有
- `FluxGuidance` —— 2/24 个有
- `ImageListToBatch+` —— 2/24 个有
- `LoraLoaderModelOnly` —— 2/24 个有
- `MathExpression|pysssss` —— 2/24 个有
- `RandomNoise` —— 2/24 个有
- `SamplerCustomAdvanced` —— 2/24 个有
- `SaveImage` —— 2/24 个有
- `SomethingToString` —— 2/24 个有
- `VAEDecode` —— 2/24 个有
- `easy batchAnything` —— 2/24 个有
- `easy float` —— 2/24 个有
- `easy forLoopEnd` —— 2/24 个有
- `easy forLoopStart` —— 2/24 个有
- `easy outputToList` —— 2/24 个有
- `Int` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 24 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）

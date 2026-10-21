---
name: unknown_workflow_video_sampler_vae_24
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.969769
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: [String Literal]
members: [视频生成/图生视频/1909172301974089729.json, 视频生成/图生视频/1907301627349622785.json, 视频生成/图生视频/2043935340162981889.json, 视频生成/图生视频/1926800707893010433.json, 视频生成/图生视频/2044216380353945602.json, 视频生成/图生视频/2044595167281291265.json, 视频生成/图生视频/1923033044188319745.json, 视频生成/图生视频/2044749490703310849.json, 视频生成/文生视频/1922920161509261314.json, 视频生成/文生视频/1923393888814624770.json, 视频生成/文生视频/1933051482759630849.json, 视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_2072999770106667008.json, 视频生成/文生视频/Self Forcing-文生图&图生视频_2072999743447670784.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1909172301974089729.json、视频生成/图生视频/1907301627349622785.json、视频生成/图生视频/2043935340162981889.json、视频生成/图生视频/1926800707893010433.json、视频生成/图生视频/2044216380353945602.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 13 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 12/13 个有
- `INTConstant` —— 11/13 个有
- `String Literal` —— 11/13 个有
- `ImageResizeKJ` —— 10/13 个有
- `LoadImage` —— 10/13 个有
- `GetImageSizeAndCount` —— 8/13 个有
- `WanVideoVACEStartToEndFrame` —— 8/13 个有
- `WanVideoSLG` —— 7/13 个有
- `WanVideoTeaCache` —— 7/13 个有
- `WanVideoVACEModelSelect` —— 7/13 个有
- `PreviewImage` —— 6/13 个有
- `MaskPreview+` —— 5/13 个有
- `AIO_Preprocessor` —— 2/13 个有
- `RH_Captioner` —— 2/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `WanVideoLoraSelect` —— 2/13 个有
- `TextInput_` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal

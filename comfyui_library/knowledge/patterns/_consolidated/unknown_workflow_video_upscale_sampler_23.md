---
name: unknown_workflow_video_upscale_sampler_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9185
common_nodes: [ColorMatch, DownloadAndLoadGIMMVFIModel, Fast Groups Bypasser (rgthree), GIMMVFI_interpolate, ImageConcanate, ImageSmartSharpen+, ImageUpscaleWithModel, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], Text Multiline, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生视频FX模型3分钟急速版_1934534192887701505.json, 视频生成/图生视频/超级图生视频人物一致1分钟生成_1933355475016818690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/图生视频FX模型3分钟急速版_1934534192887701505.json、视频生成/图生视频/超级图生视频人物一致1分钟生成_1933355475016818690.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `ColorMatch`
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Bypasser (rgthree)`
- `GIMMVFI_interpolate`
- `ImageConcanate`
- `ImageSmartSharpen+`
- `ImageUpscaleWithModel`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoMagCache` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_lora_sampler_760
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.798667
common_nodes: [JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, PrimitiveStringMultiline, SaveLatent, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/正在测试lora  -_1944651399730745345.json, 视频生成/图生视频/正在测试lora  -_1944662370163544065.json, 视频生成/图生视频/（自用）N-API 14B图生视频超级加速版V1_1937513401944051713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_760

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/正在测试lora  -_1944651399730745345.json、视频生成/图生视频/正在测试lora  -_1944662370163544065.json、视频生成/图生视频/（自用）N-API 14B图生视频超级加速版V1_1937513401944051713.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveLatent`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_TextConcatenate` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/3 个有
- `GIMMVFI_interpolate` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `LoadLatent` —— 1/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

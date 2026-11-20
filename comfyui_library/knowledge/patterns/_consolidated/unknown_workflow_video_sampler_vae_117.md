---
name: unknown_workflow_video_sampler_vae_117
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5758
common_nodes: [AIO_Preprocessor, DWPreprocessor, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/【视频转成宫崎骏画风！】Kontext+VACE完美转绘视频风格，图像编辑+首尾帧实现宫崎骏画风_1936841995463610369.json, 平台全量/🔥 AI复刻「辟邪剑谱」！一键把林平之换成你！_1941187194113703937.json, 视频生成/图生视频/【用AI复刻武侠绝学】Vace+FusionX练成降龙十八掌，姿势+深度+抠图实现人物动作迁移_2057994609967583234.json, 视频生成/图生视频/完美换人图生视频Wan-VACE_V2V_1930978728523051010.json, 视频生成/图生视频/最强高一致性图像参考+姿态引导_1934120963867107329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_117

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/【视频转成宫崎骏画风！】Kontext+VACE完美转绘视频风格，图像编辑+首尾帧实现宫崎骏画风_1936841995463610369.json、平台全量/🔥 AI复刻「辟邪剑谱」！一键把林平之换成你！_1941187194113703937.json、视频生成/图生视频/【用AI复刻武侠绝学】Vace+FusionX练成降龙十八掌，姿势+深度+抠图实现人物动作迁移_2057994609967583234.json、视频生成/图生视频/完美换人图生视频Wan-VACE_V2V_1930978728523051010.json、视频生成/图生视频/最强高一致性图像参考+姿态引导_1934120963867107329.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `DWPreprocessor`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 4/5 个有
- `LayerMask: LoadSegmentAnythingModels` —— 4/5 个有
- `LayerMask: SegmentAnythingUltra V3` —— 4/5 个有
- `MaskToImage` —— 4/5 个有
- `Mix Color By Mask` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `VHS_VideoInfo` —— 4/5 个有
- `WanVideoExperimentalArgs` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `WanVideoApplyNAG` —— 3/5 个有
- `WanVideoTextEncodeSingle` —— 3/5 个有
- `RMBG` —— 2/5 个有
- `WanVideoMagCache` —— 2/5 个有
- `WanVideoTextEncode` —— 2/5 个有
- `WanVideoVACEModelSelect` —— 2/5 个有
- `Bjornulf_ShowInt` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `StringConstantMultiline` —— 1/5 个有
- `WanVideoEnhanceAVideo` —— 1/5 个有
- `WanVideoLoraSelect` —— 1/5 个有
- `WanVideoVACEStartToEndFrame` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

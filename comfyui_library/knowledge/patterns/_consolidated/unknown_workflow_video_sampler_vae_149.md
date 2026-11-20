---
name: unknown_workflow_video_sampler_vae_149
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86575
common_nodes: [Anything Everywhere, CR Text, ImageFromBatch+, ImageResizeKJ, Int, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/视频生成001_1927999757036470273.json, 平台全量/视频生成002_1927867191377707009.json, 平台全量/视频生成002_1928000604898246657.json, 数字人/数字人/v1_1928127007216025602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_149

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频生成001_1927999757036470273.json、平台全量/视频生成002_1927867191377707009.json、平台全量/视频生成002_1928000604898246657.json、数字人/数字人/v1_1928127007216025602.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `CR Text`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageMaskScaleAs` —— 3/4 个有
- `RepeatImageBatch` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `OpenposePreprocessor` —— 2/4 个有
- `Text List` —— 2/4 个有
- `Text List to Text` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `LayerUtility: CropByMask` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/4 个有
- `WanVideoUniAnimatePoseInput` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_sampler_29
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8404
common_nodes: [LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFlashVSRInput, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [平台全量/wanvideo-FlashVSR视频高清放大_1978717016997695489.json, 平台全量/wanvideo_1_3B_FlashVSR_upscale_1978731009237733377.json, 平台全量/视频变高清_FlashVSR_upscale_example_1987756849841811458.json, 平台全量/视频放大指定放大倍数+KJ_Wan_Flash_VSR+全节点注释_2059521563585765378.json, 视频生成/文生视频/Flash VSR视频超分辨率_1979451793736372225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/wanvideo-FlashVSR视频高清放大_1978717016997695489.json、平台全量/wanvideo_1_3B_FlashVSR_upscale_1978731009237733377.json、平台全量/视频变高清_FlashVSR_upscale_example_1987756849841811458.json、平台全量/视频放大指定放大倍数+KJ_Wan_Flash_VSR+全节点注释_2059521563585765378.json、视频生成/文生视频/Flash VSR视频超分辨率_1979451793736372225.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFlashVSRInput`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `GetImageSizeAndCount` —— 3/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `AILab_MiniCPM_4_V` —— 1/5 个有
- `ColorMatch` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `WanVideoBlockSwap` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

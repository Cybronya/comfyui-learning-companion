---
name: unknown_workflow_video_lora_sampler_910
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.454667
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【阡陌】Ditto只需一句话视频风格转绘_1984179008936050689.json, 视频生成/文生视频/03-14-01-WAN2.1-视频风格转换-ditto_1989939354082660353.json, 视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_910

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【阡陌】Ditto只需一句话视频风格转绘_1984179008936050689.json、视频生成/文生视频/03-14-01-WAN2.1-视频风格转换-ditto_1989939354082660353.json、视频生成/文生视频/ComfyUI Wan 2.1 VACE 多条件 - 更好的 ControlNet 控图视频生成_1931329103214129154.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 3 个 workflow 都包含：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

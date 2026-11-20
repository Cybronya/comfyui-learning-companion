---
name: unknown_workflow_video_lora_sampler_355
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.66425
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Ditto-视频风格转绘(超强30+)_1980646949659561986.json, 平台全量/Ditto_动漫视频转真人工作流_1980819570653052929.json, 平台全量/Ditto_视频风格转换工作流_1980925477508567042.json, 平台全量/Ditto视频风格转绘_1960617916809043969.json, 平台全量/Ditto：傻瓜式视频编辑大模型，AI一键把视频主角变成黄金雕塑！_1980320966066810882.json, 平台全量/Wan2.1 Ditto视频风格转绘_1980640342271770625.json, 平台全量/【风格转绘】Ditto-视频风格转绘(动漫转真人)_1980805782801399809.json, 平台全量/视频多风格转绘_2082700347369410562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_355

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Ditto-视频风格转绘(超强30+)_1980646949659561986.json、平台全量/Ditto_动漫视频转真人工作流_1980819570653052929.json、平台全量/Ditto_视频风格转换工作流_1980925477508567042.json、平台全量/Ditto视频风格转绘_1960617916809043969.json、平台全量/Ditto：傻瓜式视频编辑大模型，AI一键把视频主角变成黄金雕塑！_1980320966066810882.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 8 个 workflow 都包含：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/8 个有
- `JWInteger` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `CR Text` —— 2/8 个有
- `GetImageSizeAndCount` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `VHS_VideoInfo` —— 2/8 个有
- `Bjornulf_ShowInt` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `VHS_VideoInfoLoaded` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

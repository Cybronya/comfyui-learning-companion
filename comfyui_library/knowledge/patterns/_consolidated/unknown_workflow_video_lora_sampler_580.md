---
name: unknown_workflow_video_lora_sampler_580
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6464
common_nodes: [LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wanvace视频动作参考转绘_1958568346285404162.json, 平台全量/ditto_comfyui_workflow_global_edit_1980477577573937154.json, 平台全量/ditto视频批量风格转换工作流_2013501377070239746.json, 平台全量/ditto视频转绘工作流_1980636437588692994.json, 平台全量/ditto视频风格转换_1989887810817716226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_580

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/Wanvace视频动作参考转绘_1958568346285404162.json、平台全量/ditto_comfyui_workflow_global_edit_1980477577573937154.json、平台全量/ditto视频批量风格转换工作流_2013501377070239746.json、平台全量/ditto视频转绘工作流_1980636437588692994.json、平台全量/ditto视频风格转换_1989887810817716226.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 5 个 workflow 都包含：
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
- `GetNode` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `CR Prompt List` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `Int` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `String Literal` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

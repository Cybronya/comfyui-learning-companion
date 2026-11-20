---
name: unknown_workflow_video_lora_sampler_496
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.673833
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/一键视频转绘_1983554543327846402.json, 平台全量/视频一键转绘_1980552466741809153.json, 平台全量/视频转换视频风格转换ditto视频风格转换加速版（10s以上）_1980568740637134849.json, 平台全量/视频转绘-转真人_1997956555716878338.json, 平台全量/视频转绘视频风格转换ditto视频风格转换加速版（10s以上）_1980558222274809857.json, 平台全量/视频风格转绘加速版（10s以上）_2001670639868080129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_496

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/一键视频转绘_1983554543327846402.json、平台全量/视频一键转绘_1980552466741809153.json、平台全量/视频转换视频风格转换ditto视频风格转换加速版（10s以上）_1980568740637134849.json、平台全量/视频转绘-转真人_1997956555716878338.json、平台全量/视频转绘视频风格转换ditto视频风格转换加速版（10s以上）_1980558222274809857.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Int` —— 5/6 个有
- `WanVideoSLG` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `ImageConcanate` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `CLIPTextEncode` —— 2/6 个有
- `MathExpression_UTK` —— 2/6 个有
- `ImageStitch` —— 1/6 个有
- `JWStringMultiline` —— 1/6 个有
- `VHS_VideoInfo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

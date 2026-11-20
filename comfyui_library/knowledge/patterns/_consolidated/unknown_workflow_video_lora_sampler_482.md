---
name: unknown_workflow_video_lora_sampler_482
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.683667
common_nodes: [ImageResizeKJv2, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/58.tonnie-Ditto视频风格转绘（效果不好）_2008694710507937794.json, 平台全量/Ditto视频转绘（内置几十种风格任选）_1995489402400997377.json, 平台全量/Ditto视频转绘（内置几十种风格任选）_2064313700726689794.json, 平台全量/Ditto视频风格转换_1981976450750390274.json, 平台全量/ditto+wan2.2最强视频风格转换_1980305437578997761.json, 平台全量/ditto+wan2.2最强视频风格转换_2018164623127617538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_482

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/58.tonnie-Ditto视频风格转绘（效果不好）_2008694710507937794.json、平台全量/Ditto视频转绘（内置几十种风格任选）_1995489402400997377.json、平台全量/Ditto视频转绘（内置几十种风格任选）_2064313700726689794.json、平台全量/Ditto视频风格转换_1981976450750390274.json、平台全量/ditto+wan2.2最强视频风格转换_1980305437578997761.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/6 个有
- `WanVideoSLG` —— 4/6 个有
- `INTConstant` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `RIFE VFI` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `WanVideoEnhanceAVideo` —— 2/6 个有
- `WanVideoExperimentalArgs` —— 2/6 个有
- `SimpleMath+` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
